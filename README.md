# cursor-agents

Public catalog of **Cursor agent integration**: skills, MCP guidance, rules, and small runnable packages (`doctl`, Pi, macOS, Linux, Mastodon, MPD, …).

**Not in this repo:** your machine names, tokens, `~/Git` layout, or private infra — those live in **[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** (private).

## Product agents (active)

| Package | Path | What it does |
|---------|------|--------------|
| **music-streaming-agent** | [`music-streaming-agent/`](music-streaming-agent/) | LAN MPD control (`music_agent` CLI + optional HTTP) |
| **mastodon-agent** | [`mastodon-agent/`](mastodon-agent/) (submodule) | Post from UTF-8 drafts — **[shahzebqazi/mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** |
| **mastodon-agent (Cursor)** | [`mastodon-agent-cursor/`](mastodon-agent-cursor/) | Cursor charter for Mastodon submodule |

## Platform agents (skills + MCP stubs)

| Package | Path | Scope |
|---------|------|--------|
| **digitalocean-agent** | [`digitalocean-agent/`](digitalocean-agent/) | `doctl`, droplets, DNS, App Platform |
| **pi-platform-agent** | [`pi-platform-agent/`](pi-platform-agent/) | Pi SSH, systemd, Docker patterns |
| **macos-platform-agent** | [`macos-platform-agent/`](macos-platform-agent/) | macOS dev / WM patterns (not personal dotfiles) |
| **linux-platform-agent** | [`linux-platform-agent/`](linux-platform-agent/) | Linux desktop / server patterns |

See [`docs/PLATFORM_AGENTS.md`](docs/PLATFORM_AGENTS.md) and [`docs/MCP_AND_SKILLS.md`](docs/MCP_AND_SKILLS.md).

## Hub layout

- [`docs/HUB_INDEX.md`](docs/HUB_INDEX.md) — full index
- [`docs/RETIRED_REPOS.md`](docs/RETIRED_REPOS.md) — renamed GitHub repos

## GitHub Pages

- [shahzebqazi.github.io/cursor-agents/](https://shahzebqazi.github.io/cursor-agents/)

```bash
git clone --recurse-submodules https://github.com/shahzebqazi/cursor-agents.git
```

## Private operator config

**[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** — personalizations, per-machine workspaces, `PI_SERVER/` sync, MacBook bundle. Home lab handoff: `my-cursor-config/docs/WORKSPACE_AGENTS.md`. Pi deploy notes (redacted): `my-cursor-config/docs/CURSOR_AGENTS_ON_PI.md` (private clone only; local dir may be `~/Git/cursor-config/`).

## License

MIT — see [LICENSE](LICENSE).
