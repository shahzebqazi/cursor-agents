"""MPD control port: subprocess `mpc` only (dependency inversion via protocol)."""

from __future__ import annotations

import os
import re
import subprocess
from collections.abc import Sequence
from typing import Protocol

from .situation import Situation


class MpcPort(Protocol):
    def run(self, args: Sequence[str]) -> tuple[int, str, str]: ...

    def snapshot(self) -> Situation: ...


class SubprocessMpc:
    def __init__(self, env: dict[str, str] | None = None) -> None:
        self._env = {**os.environ, **(env or {})}

    def run(self, args: Sequence[str]) -> tuple[int, str, str]:
        p = subprocess.run(
            ["mpc", *args],
            capture_output=True,
            text=True,
            check=False,
            env=self._env,
        )
        return p.returncode, p.stdout or "", p.stderr or ""

    def snapshot(self) -> Situation:
        code, st, _ = self.run(["status"])
        _, cur, _ = self.run(["current"])
        code_p, pl_out, _ = self.run(["playlist"])
        playlist_len = len([ln for ln in pl_out.splitlines() if ln.strip()]) if code_p == 0 else None
        return _parse_status_block(st.strip(), cur.strip(), playlist_len)


def _parse_status_block(status: str, current: str, playlist_len: int | None) -> Situation:
    vol: int | None = None
    repeat = single = consume = random = None
    state = "stopped"
    pos = dur = None
    for line in status.splitlines():
        m = re.match(r"volume:\s*(\d+)%", line, re.I)
        if m:
            vol = int(m.group(1))
        m = re.match(r"repeat:\s*(on|off)", line, re.I)
        if m:
            repeat = m.group(1).lower() == "on"
        m = re.match(r"single:\s*(on|off)", line, re.I)
        if m:
            single = m.group(1).lower() == "on"
        m = re.match(r"consume:\s*(on|off)", line, re.I)
        if m:
            consume = m.group(1).lower() == "on"
        m = re.match(r"random:\s*(on|off)", line, re.I)
        if m:
            random = m.group(1).lower() == "on"
        m = re.search(r"\[(\w+)\].*?(\d+):(\d+)/(\d+):(\d+)", line)
        if m:
            st = m.group(1).lower()
            if st == "playing":
                state = "playing"
            elif st == "paused":
                state = "paused"
            pos = int(m.group(2)) * 60 + int(m.group(3))
            dur = int(m.group(4)) * 60 + int(m.group(5))
    if state == "stopped" and current:
        # mpc often omits bracket state when idle but still prints last song on some builds
        if "playing" in status.lower():
            state = "playing"
        elif "paused" in status.lower():
            state = "paused"
    return Situation(
        state=state,
        volume=vol,
        repeat=repeat,
        single=single,
        consume=consume,
        random=random,
        playlist_len=playlist_len,
        current_song=current or None,
        position_sec=pos,
        duration_sec=dur,
        raw_status=status,
    )
