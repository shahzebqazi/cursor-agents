# cursor-agents

Public catalog of **Cursor-friendly agent tools** — small, boring, composable packages you can run without private dotfiles.

| Package | Path | What it does |
|---------|------|--------------|
| **mastodon-agent** | [`mastodon-agent/`](mastodon-agent/) | Post Mastodon statuses from UTF-8 draft files; `.env` for credentials |
| **music-streaming-agent** | [`music-streaming-agent/`](music-streaming-agent/) | LAN MPD control agent (`music_agent` CLI + optional HTTP chat) |

## Hub layout

- **Index:** [`docs/HUB_INDEX.md`](docs/HUB_INDEX.md) — packages vs private config vs Mac harness
- **Retired repo names:** [`docs/RETIRED_REPOS.md`](docs/RETIRED_REPOS.md)

## GitHub Pages

- **Catalog:** [shahzebqazi.github.io/cursor-agents/](https://shahzebqazi.github.io/cursor-agents/)
- **Mastodon mini-site (hero art preserved):** […/cursor-agents/docs/mastodon/](https://shahzebqazi.github.io/cursor-agents/docs/mastodon/)

Enable Pages on this repo: **Settings → Pages → `/docs` on `main`**.

## Personal Cursor configuration

Optional private rules and workflow notes live in **[cursor-config](https://github.com/shahzebqazi/cursor-config)** (private). Nothing in this catalog requires that repo.

**Home lab (`~/Git` on Pi):** clone this repo as `cursor-agents/`; use **`music-streaming-agent/`** for MPD agent work. Workspace handoff: **`cursor-config/docs/WORKSPACE_AGENTS.md`**.

**Home lab (`~/Git` on Pi):** clone this repo as `cursor-agents/`; use **`music-streaming-agent/`** for MPD agent work. Workspace handoff and clone sync policy: **`cursor-config/docs/WORKSPACE_AGENTS.md`**.

## Migrated repositories

These former standalone repos now redirect here:

- `mastodon-cursor-agent` → `mastodon-agent/`
- `cursor-music-streaming-agent` → `music-streaming-agent/`

## License

MIT — see [LICENSE](LICENSE). Package-level licenses match unless noted in subdirectories.
