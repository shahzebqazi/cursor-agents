"""Chat tone presets (text-only, no model calls)."""

from __future__ import annotations

from collections.abc import Callable

ToneFn = Callable[[str], str]

_PRESETS: dict[str, ToneFn] = {
    "formal": lambda body: "Understood.\n\n" + body.strip(),
    "concise": lambda body: body.strip(),
    "warm": lambda body: "Here is what I did:\n\n" + body.strip(),
}


def render(tone: str, body: str) -> str:
    fn = _PRESETS.get(tone, _PRESETS["formal"])
    return fn(body)


def tones() -> tuple[str, ...]:
    return tuple(sorted(_PRESETS.keys()))
