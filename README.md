# cursor-agents

Public **Cursor agent toolkit**: skills, MCP notes, charters, and small runnable packages. Built for **Cursor users** who want copy-paste workflows; structured so **reviewers** can audit boundaries and proof without your private repos.

**Not in this repo:** machine names, tokens, or personal infra — see [`docs/employer/ARCHITECTURE.md`](docs/employer/ARCHITECTURE.md).

## Start here (by problem)

| I want to… | Package |
|------------|---------|
| Fix git sync / dirty trees / multi-repo layout | [`tooling/git-workspace-agent/`](tooling/git-workspace-agent/) |
| Find which package owns my task | [`meta/cursor-guide-agent/`](meta/cursor-guide-agent/) |
| Use `doctl` read-first on DigitalOcean | [`digitalocean-agent/`](digitalocean-agent/) |
| Run headless agent patterns on a Pi | [`pi-platform-agent/`](pi-platform-agent/) |
| Prune archived Cursor chats on macOS | [`macos-platform-agent/`](macos-platform-agent/) |
| Control LAN MPD / music streaming | [`music-streaming-agent/`](music-streaming-agent/) |
| Batch-tag a music library (Picard) | [`music-library-agent/`](music-library-agent/) |
| Post Mastodon drafts from git | [`mastodon-agent/`](mastodon-agent/) + [`mastodon-agent-cursor/`](mastodon-agent-cursor/) |

## Monorepo v2 (in progress)

Categories: **`tooling/`** · **`meta/`** · **`platform/`** *(migration pending)* · **`products/`** *(migration pending)*

- Roadmap: [`docs/MONOREPO_V2_ROADMAP.md`](docs/MONOREPO_V2_ROADMAP.md)
- Kanban: [GitHub Project #16](https://github.com/users/shahzebqazi/projects/16)
- Contribute: [`CONTRIBUTING.md`](CONTRIBUTING.md) · Agent rules: [`AGENTS.md`](AGENTS.md)

Legacy top-level paths (`music-streaming-agent/`, etc.) remain until migration PRs merge.

## Product agents

| Package | Path | What it does |
|---------|------|--------------|
| **music-streaming-agent** | [`music-streaming-agent/`](music-streaming-agent/) | LAN MPD control (`music_agent` CLI + optional HTTP) |
| **music-library-agent** | [`music-library-agent/`](music-library-agent/) | Picard ingest, metadata, quarantine |
| **mastodon-agent** | [`mastodon-agent/`](mastodon-agent/) (submodule) | Post from UTF-8 drafts — **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** |
| **mastodon-agent (Cursor)** | [`mastodon-agent-cursor/`](mastodon-agent-cursor/) | Cursor charter for submodule |

## Platform agents

| Package | Path | Scope |
|---------|------|--------|
| **digitalocean-agent** | [`digitalocean-agent/`](digitalocean-agent/) | `doctl`, droplets, DNS, App Platform |
| **pi-platform-agent** | [`pi-platform-agent/`](pi-platform-agent/) | Pi SSH, systemd, Docker, headless invoke |
| **macos-platform-agent** | [`macos-platform-agent/`](macos-platform-agent/) | macOS dev patterns, chat prune skill |
| **linux-platform-agent** | [`linux-platform-agent/`](linux-platform-agent/) | Linux desktop / server patterns |

See [`docs/PLATFORM_AGENTS.md`](docs/PLATFORM_AGENTS.md) and [`docs/MCP_AND_SKILLS.md`](docs/MCP_AND_SKILLS.md).

## For reviewers

Hiring managers and recruiters: [`docs/employer/README.md`](docs/employer/README.md) (case cards + architecture).

## Hub docs

- [`docs/HUB_INDEX.md`](docs/HUB_INDEX.md) — full index
- [`docs/RETIRED_REPOS.md`](docs/RETIRED_REPOS.md) — renamed GitHub repos

## GitHub Pages

- [shahzebqazi.github.io/cursor-agents/](https://shahzebqazi.github.io/cursor-agents/)

```bash
git clone --recurse-submodules https://github.com/shahzebqazi/cursor-agents.git
```

## Workspace config

| Repo | Role |
|------|------|
| **[cursor-config](https://github.com/shahzebqazi/cursor-config)** | Public workspace docs, examples, patterns (no secrets) |
| **my-cursor-config** (private) | Operator layer: workspaces, Pi sync, publish policy |

## License

MIT — see [LICENSE](LICENSE).
