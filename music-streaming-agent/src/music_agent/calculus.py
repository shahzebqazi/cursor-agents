"""Legality checks: situation-calculus-style preconditions over fluents (pure)."""

from __future__ import annotations

import re

from .effects import Effect
from .situation import Situation, active_transport


def legal(effect: Effect, s: Situation) -> tuple[bool, str | None]:
    """Return (ok, reason_if_not)."""
    op = effect.op
    if op in {"seek_abs", "seek_rel"} and not active_transport(s):
        return False, "Transport is not active; cannot seek."
    if op == "seek_abs" and not (effect.arg or "").strip():
        return False, "Seek target required."
    if op == "volume_abs":
        if effect.arg is None:
            return False, "Missing volume target."
        try:
            v = int(effect.arg)
        except ValueError:
            return False, "Volume must be an integer 0–100."
        if not 0 <= v <= 100:
            return False, "Volume must be between 0 and 100."
    if op == "volume_delta":
        if effect.arg is None:
            return False, "Missing volume delta (+N or -N)."
        if not re.fullmatch(r"[+-]\d+", effect.arg):
            return False, "Volume delta must look like +5 or -5."
    if op in {"load_playlist", "append_playlist"} and not (effect.arg or "").strip():
        return False, "Playlist name required."
    if op == "search_add_first" and not (effect.arg or "").strip():
        return False, "Search query required."
    if op == "db_update":
        # empty arg means full library update
        if effect.arg is None:
            return False, "Update path required (use empty string for full update)."
    if op == "set_crossfade":
        if effect.arg is None:
            return False, "Crossfade seconds required."
        try:
            int(effect.arg)
        except ValueError:
            return False, "Crossfade must be integer seconds."
    if op in {"set_random", "set_repeat", "set_consume", "set_single"}:
        if effect.arg not in {"on", "off"}:
            return False, "Mode must be on or off."
    if op == "toggle_output":
        if not (effect.arg or "").strip():
            return False, "Output id required."
        if effect.arg2 not in {"enable", "disable"}:
            return False, "Output mode must be enable or disable."
    if op == "volume_profile_remember":
        if not (effect.arg or "").strip():
            return False, "device_id required."
        if effect.arg2 is None:
            return False, "volume level required."
    return True, None
