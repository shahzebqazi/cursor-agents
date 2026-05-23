# cursor-agents

Public catalog of **Cursor-friendly agent tools** — small, boring, composable packages you can run without private dotfiles.

| Package | Path | What it does |
|---------|------|--------------|
| **mastodon-agent** | [`mastodon-agent/`](mastodon-agent/) (submodule) | Post Mastodon statuses from UTF-8 drafts — canonical repo **[shahzebqazi/mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** |
| **mastodon-agent (Cursor)** | [`mastodon-agent-cursor/`](mastodon-agent-cursor/) | Cursor rules charter; points at submodule + [`docs/SPEC.md`](mastodon-agent/docs/SPEC.md) |
| **music-streaming-agent** | [`music-streaming-agent/`](music-streaming-agent/) | LAN MPD control agent (`music_agent` CLI + optional HTTP chat) |

## Hub layout

- **Index:** [`docs/HUB_INDEX.md`](docs/HUB_INDEX.md) — packages vs private config vs Mac harness
- **Retired repo names:** [`docs/RETIRED_REPOS.md`](docs/RETIRED_REPOS.md)

## GitHub Pages

- **Catalog:** [shahzebqazi.github.io/cursor-agents/](https://shahzebqazi.github.io/cursor-agents/)
- **Mastodon product site (hero art):** [shahzebqazi.github.io/mastodon-agent/](https://shahzebqazi.github.io/mastodon-agent/) — [`docs/mastodon/`](docs/mastodon/) redirects here

Enable Pages on this repo: **Settings → Pages → `/docs` on `main`**.

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/shahzebqazi/cursor-agents.git
```

## Personal Cursor configuration

Optional private rules and workflow notes live in **[cursor-config](https://github.com/shahzebqazi/cursor-config)** (private). Nothing in this catalog requires that repo.

**Home lab (`~/Git` on Pi):** clone this repo as `cursor-agents/`; use **`music-streaming-agent/`** for MPD agent work. Workspace handoff and clone sync policy: **`cursor-config/docs/WORKSPACE_AGENTS.md`**.

## Migrated repositories

| Former standalone | Today |
|-------------------|--------|
| `mastodon-cursor-agent` | **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** (submodule) + `mastodon-agent-cursor/` here |
| `cursor-music-streaming-agent` | `music-streaming-agent/` |

## License

MIT — see [LICENSE](LICENSE). Package-level licenses match unless noted in subdirectories.
