"""Algebraic effect descriptions (no IO). Each core capability maps to one or more Effect values."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

EffectOp = Literal[
    "play",
    "pause",
    "stop",
    "next",
    "prev",
    "seek_abs",
    "seek_rel",
    "volume_abs",
    "volume_delta",
    "toggle_consume",
    "toggle_single",
    "toggle_repeat",
    "toggle_random",
    "set_random",
    "set_repeat",
    "set_consume",
    "set_single",
    "clear_queue",
    "load_playlist",
    "append_playlist",
    "search_add_first",
    "list_playlists",
    "show_queue",
    "db_update",
    "set_crossfade",
    "list_outputs",
    "toggle_output",
    "status_snapshot",
    "volume_profile_remember",
]


@dataclass(frozen=True)
class Effect:
    """Side-effect request the runtime applies via `mpc` (and tiny local state for volumes)."""

    op: EffectOp
    arg: str | None = None
    arg2: str | None = None
