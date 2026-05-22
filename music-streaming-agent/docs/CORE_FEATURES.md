# Core features (v0): situation predicates × effect types

Each row is a **capability**: **fluent predicates** (what must hold / what we observe) and the **Effect** opcode the runtime executes via `mpc` (or a tiny JSON sidecar for volume memory).

| # | Capability | Typical predicates (Situation) | Effect `op` |
|---:|---|---|---|
| 1 | Read transport + tags | always | `status_snapshot` |
| 2 | Resume playback | `not playing` optional | `play` |
| 3 | Pause | `playing` typical | `pause` |
| 4 | Stop | always legal | `stop` |
| 5 | Next track | queue non-empty typical | `next` |
| 6 | Previous track | queue non-empty typical | `prev` |
| 7 | Seek absolute | `active_transport` | `seek_abs` |
| 8 | Seek relative | `active_transport` | `seek_rel` |
| 9 | Set absolute volume | arg 0–100 | `volume_abs` |
| 10 | Nudge volume | delta `±N` | `volume_delta` |
| 11 | Shuffle on | — | `set_random` `on` |
| 12 | Shuffle off | — | `set_random` `off` |
| 13 | Repeat on/off | — | `set_repeat` |
| 14 | Consume on/off | — | `set_consume` |
| 15 | Single on/off | — | `set_single` |
| 16 | Toggle shuffle/repeat/consume/single | — | `toggle_*` |
| 17 | Clear queue | — | `clear_queue` |
| 18 | Replace queue from stored playlist | playlist exists | `load_playlist` |
| 19 | Append stored playlist | playlist exists | `append_playlist` |
| 20 | Add first search hit | match exists | `search_add_first` |
| 21 | List stored playlists | — | `list_playlists` |
| 22 | Show queue | — | `show_queue` |
| 23 | Refresh library index | path valid / empty for full | `db_update` |
| 24 | Crossfade seconds | non-negative int | `set_crossfade` |
| 25 | Outputs + enable/disable | output id valid | `list_outputs` / `toggle_output` |

**Sidecar (not `mpc`)**: `volume_profile_remember` stores per-device defaults under `XDG_DATA_HOME/music-agent/volume_profiles.json`.

**v0 router**: deterministic phrase patterns in [`src/music_agent/pipeline.py`](../src/music_agent/pipeline.py) (no on-device LLM). Cursor / future Ollama can sit upstream and emit the same structured phrases.
