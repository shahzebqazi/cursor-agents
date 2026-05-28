"""Natural-language-ish routing (v0): pure parse + plan using fluents (no network IO here)."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .effects import Effect
from .situation import Situation


@dataclass(frozen=True)
class PlanResult:
    effects: tuple[Effect, ...]
    notes: tuple[str, ...]


def parse_plan(message: str, situation: Situation, device_id: str | None) -> PlanResult:
    """Map user text + fluents to a batch of Effects (situation-calculus-style planning)."""
    raw = message.strip()
    if not raw:
        return PlanResult((), ("Empty message.",))

    low = raw.lower()

    # --- explicit structured commands (prefer machine-like phrases for v0) ---
    if low in {"status", "np", "now playing", "nowplaying"}:
        return PlanResult((Effect("status_snapshot"),), ())

    m = re.match(r"^volume\s+(\d{1,3})\s*$", low)
    if m:
        v = int(m.group(1))
        effs: list[Effect] = [Effect("volume_abs", str(v))]
        if device_id:
            effs.append(Effect("volume_profile_remember", device_id, str(v)))
        return PlanResult(tuple(effs), ())

    if low in {"louder", "volume up", "vol up"}:
        return PlanResult((Effect("volume_delta", "+5"),), ())
    if low in {"quieter", "volume down", "vol down"}:
        return PlanResult((Effect("volume_delta", "-5"),), ())

    m = re.match(r"^remember\s+volume\s+(\d{1,3})\s*$", low)
    if m:
        if not device_id:
            return PlanResult(
                (),
                ("device_id is required in JSON to remember per-device volume.",),
            )
        v = int(m.group(1))
        return PlanResult(
            (
                Effect("volume_abs", str(v)),
                Effect("volume_profile_remember", device_id, str(v)),
            ),
            (),
        )

    if low in {"play", "resume"}:
        return PlanResult((Effect("play"),), ())
    if low in {"pause", "hold"}:
        return PlanResult((Effect("pause"),), ())
    if low in {"stop"}:
        return PlanResult((Effect("stop"),), ())
    if low in {"next", "skip", "forward track"}:
        return PlanResult((Effect("next"),), ())
    if low in {"prev", "previous", "back"}:
        return PlanResult((Effect("prev"),), ())

    m = re.match(r"^seek\s+(\d+)s\s*$", low)
    if m:
        sec = int(m.group(1))
        mm, ss = divmod(sec, 60)
        return PlanResult((Effect("seek_abs", f"{mm}:{ss:02d}"),), ())

    m = re.match(r"^seek\s+([+-]?\d+)\s*$", low)
    if m:
        return PlanResult((Effect("seek_abs", m.group(1)),), ())

    m = re.match(r"^seek\s+([+-]?\d+)s\s*$", low)
    if m:
        sec = int(m.group(1))
        sign = "+" if sec >= 0 else "-"
        s = abs(sec)
        mm, ss = divmod(s, 60)
        return PlanResult((Effect("seek_rel", f"{sign}{mm}:{ss:02d}"),), ())

    m = re.match(r"^load\s+playlist\s+(.+)$", raw, re.I)
    if m:
        name = m.group(1).strip()
        return PlanResult((Effect("load_playlist", name),), ())

    m = re.match(r"^append\s+playlist\s+(.+)$", raw, re.I)
    if m:
        name = m.group(1).strip()
        return PlanResult((Effect("append_playlist", name),), ())

    m = re.match(r"^add\s+(.+)$", raw, re.I)
    if m:
        q = m.group(1).strip()
        return PlanResult((Effect("search_add_first", q),), ())

    if low in {"list playlists", "playlists"}:
        return PlanResult((Effect("list_playlists"),), ())
    if low in {"queue", "show queue", "playlist"}:
        return PlanResult((Effect("show_queue"),), ())

    if low in {"clear", "clear queue"}:
        return PlanResult((Effect("clear_queue"),), ())

    if low in {"shuffle on", "random on"}:
        return PlanResult((Effect("set_random", "on"),), ())
    if low in {"shuffle off", "random off"}:
        return PlanResult((Effect("set_random", "off"),), ())

    if low in {"repeat on"}:
        return PlanResult((Effect("set_repeat", "on"),), ())
    if low in {"repeat off"}:
        return PlanResult((Effect("set_repeat", "off"),), ())

    if low in {"consume on"}:
        return PlanResult((Effect("set_consume", "on"),), ())
    if low in {"consume off"}:
        return PlanResult((Effect("set_consume", "off"),), ())

    if low in {"single on"}:
        return PlanResult((Effect("set_single", "on"),), ())
    if low in {"single off"}:
        return PlanResult((Effect("set_single", "off"),), ())

    m = re.match(r"^crossfade\s+(\d+)\s*$", low)
    if m:
        return PlanResult((Effect("set_crossfade", m.group(1)),), ())

    m = re.match(r"^update\s+db\s*(.*)$", low)
    if m:
        path = m.group(1).strip()
        return PlanResult((Effect("db_update", path),), ())

    if low in {"outputs", "list outputs"}:
        return PlanResult((Effect("list_outputs"),), ())

    m = re.match(r"^(enable|disable)\s+output\s+(\d+)\s*$", low)
    if m:
        mode, oid = m.group(1), m.group(2)
        return PlanResult((Effect("toggle_output", oid, "enable" if mode == "enable" else "disable"),), ())

    # toggles (explicit)
    if low == "toggle shuffle":
        return PlanResult((Effect("toggle_random"),), ())
    if low == "toggle repeat":
        return PlanResult((Effect("toggle_repeat"),), ())
    if low == "toggle consume":
        return PlanResult((Effect("toggle_consume"),), ())
    if low == "toggle single":
        return PlanResult((Effect("toggle_single"),), ())

    return PlanResult((), (f"No v0 route for: {raw!r}. Try: status | play | pause | next | volume 40 | load playlist <name>",))
