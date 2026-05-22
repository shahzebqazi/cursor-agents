"""Situation snapshot + fluent predicates (pure data and pure functions)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Situation:
    """Fluents derived from `mpc` at a single instant (text-first for minimal CPU)."""

    state: str  # playing | paused | stopped (best-effort)
    volume: int | None
    repeat: bool | None
    single: bool | None
    consume: bool | None
    random: bool | None
    playlist_len: int | None
    current_song: str | None
    position_sec: int | None
    duration_sec: int | None
    raw_status: str


def playing(s: Situation) -> bool:
    return s.state == "playing"


def paused(s: Situation) -> bool:
    return s.state == "paused"


def stopped(s: Situation) -> bool:
    return s.state == "stopped"


def active_transport(s: Situation) -> bool:
    """Transport is active enough to seek or skip meaningfully."""
    return playing(s) or paused(s)


def has_queue(s: Situation) -> bool:
    return (s.playlist_len or 0) > 0


def volume_known(s: Situation) -> bool:
    return s.volume is not None
