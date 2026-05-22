"""Apply Effect values via `mpc` and minimal local JSON (only place with IO)."""

from __future__ import annotations

import json
import os
from pathlib import Path

from .effects import Effect
from .mpc_client import MpcPort


def _volume_store_path() -> Path:
    base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    d = base / "music-agent"
    d.mkdir(parents=True, exist_ok=True)
    return d / "volume_profiles.json"


def _one(mpc: MpcPort, args: list[str]) -> str:
    code, out, err = mpc.run(args)
    tail = (out or "").strip() or (err or "").strip()
    if code != 0:
        return f"mpc {' '.join(args)} failed ({code}): {tail}"
    return tail or "ok"


def execute(mpc: MpcPort, effect: Effect) -> str:
    op = effect.op
    if op == "play":
        return _one(mpc, ["play"])
    if op == "pause":
        return _one(mpc, ["pause"])
    if op == "stop":
        return _one(mpc, ["stop"])
    if op == "next":
        return _one(mpc, ["next"])
    if op == "prev":
        return _one(mpc, ["prev"])
    if op == "seek_abs" and effect.arg is not None:
        return _one(mpc, ["seek", effect.arg])
    if op == "seek_rel" and effect.arg is not None:
        return _one(mpc, ["seekthrough", effect.arg])
    if op == "volume_abs" and effect.arg is not None:
        return _one(mpc, ["volume", effect.arg])
    if op == "volume_delta" and effect.arg is not None:
        return _one(mpc, ["volume", effect.arg])
    if op == "toggle_consume":
        return _one(mpc, ["consume"])
    if op == "toggle_single":
        return _one(mpc, ["single"])
    if op == "toggle_repeat":
        return _one(mpc, ["repeat"])
    if op == "toggle_random":
        return _one(mpc, ["random"])
    if op == "set_random" and effect.arg in {"on", "off"}:
        return _one(mpc, ["random", effect.arg])
    if op == "set_repeat" and effect.arg in {"on", "off"}:
        return _one(mpc, ["repeat", effect.arg])
    if op == "set_consume" and effect.arg in {"on", "off"}:
        return _one(mpc, ["consume", effect.arg])
    if op == "set_single" and effect.arg in {"on", "off"}:
        return _one(mpc, ["single", effect.arg])
    if op == "clear_queue":
        return _one(mpc, ["clear"])
    if op == "load_playlist" and effect.arg:
        c1 = _one(mpc, ["clear"])
        c2 = _one(mpc, ["load", effect.arg])
        return f"{c1}; {c2}"
    if op == "append_playlist" and effect.arg:
        code, out, err = mpc.run(["playlist", effect.arg])
        if code != 0:
            return f"playlist listing failed: {(err or out).strip()}"
        lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
        if not lines:
            return "Playlist empty."
        parts: list[str] = []
        for uri in lines:
            parts.append(_one(mpc, ["add", uri]))
        return f"added {len(lines)} tracks: " + "; ".join(parts[:3]) + ("…" if len(parts) > 3 else "")
    if op == "search_add_first" and effect.arg:
        q = effect.arg
        code, out, err = mpc.run(["search", "any", q])
        if code != 0:
            return f"search failed: {(err or out).strip()}"
        first = next((ln.strip() for ln in out.splitlines() if ln.strip()), "")
        if not first:
            return "No match."
        return _one(mpc, ["add", first])
    if op == "list_playlists":
        return _one(mpc, ["lsplaylists"])
    if op == "show_queue":
        return _one(mpc, ["playlist"])
    if op == "db_update":
        path = effect.arg or ""
        args = ["update"] if path == "" else ["update", path]
        return _one(mpc, args)
    if op == "set_crossfade" and effect.arg is not None:
        return _one(mpc, ["crossfade", effect.arg])
    if op == "list_outputs":
        return _one(mpc, ["outputs"])
    if op == "toggle_output" and effect.arg:
        # arg is output id; arg2 "enable" or "disable" if set, else toggle via outputs parse - keep simple: require arg2
        if effect.arg2 == "enable":
            return _one(mpc, ["enable", effect.arg])
        if effect.arg2 == "disable":
            return _one(mpc, ["disable", effect.arg])
        return "toggle_output requires arg2 enable|disable and arg output id"
    if op == "status_snapshot":
        snap = mpc.snapshot()
        return snap.raw_status + ("\n" + (snap.current_song or "") if snap.current_song else "")
    if op == "volume_profile_remember" and effect.arg and effect.arg2 is not None:
        path = _volume_store_path()
        data: dict[str, object] = {}
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                data = {}
        if not isinstance(data, dict):
            data = {}
        data[effect.arg] = {"volume": int(effect.arg2)}
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return f"remembered volume for device {effect.arg!r}"
    return f"unhandled effect: {op}"
