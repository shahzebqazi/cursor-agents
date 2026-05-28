# Agent specification (autonomy knobs)

You retain control. Autonomy is **declared here** and in [`SOUL.md`](SOUL.md), not inferred by the runtime.

## v0 guarantees

- The HTTP surface (`music-agent serve`) only executes **explicit `Effect` values** produced by `parse_plan` + `legal` checks.
- **No cloud LLM** is contacted by this package.
- **Destructive / expensive** operations exposed in v0:
  - `db_update` (library scan)
  - `load_playlist` / `clear_queue` (queue replacement)
  - `toggle_output` (hardware routing)

## Autonomy levels (fill in as you evolve the agent)

| Domain | Default | Notes |
|---|---|---|
| Playback transport | manual via chat | `play`/`pause`/… |
| Queue edits | manual | `clear`, `load playlist`, `append playlist` |
| Library maintenance | manual | `update db …` |
| Output routing | manual | `enable/disable output …` |

Future: add “suggest-only” mode where the agent returns `Effect` JSON but does not execute until approved.
