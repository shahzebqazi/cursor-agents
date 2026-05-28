# cursor-agents

Public **Cursor agent toolkit**: skills, MCP notes, charters, and small runnable packages.

**Not in this repo:** machine names, tokens, or personal infra — see [`docs/employer/ARCHITECTURE.md`](docs/employer/ARCHITECTURE.md).

## Start here (by problem)

| I want to… | Package |
|------------|---------|
| Fix git sync / dirty trees / multi-repo layout | [`tooling/git-workspace-agent/`](tooling/git-workspace-agent/) |
| Find which package owns my task | [`meta/cursor-guide-agent/`](meta/cursor-guide-agent/) |
| Use `doctl` read-first on DigitalOcean | [`platform/digitalocean-agent/`](platform/digitalocean-agent/) |
| Run headless agent patterns on a Pi | [`platform/pi-platform-agent/`](platform/pi-platform-agent/) |
| Prune archived Cursor chats on macOS | [`platform/macos-platform-agent/`](platform/macos-platform-agent/) |
| Control LAN MPD / music streaming | [`music-streaming-agent/`](music-streaming-agent/) |
| Batch-tag a music library (Picard) | [`music-library-agent/`](music-library-agent/) |
| Post Mastodon drafts from git | [`mastodon-agent/`](mastodon-agent/) + [`mastodon-agent-cursor/`](mastodon-agent-cursor/) |

Full index: [`docs/HUB_INDEX.md`](docs/HUB_INDEX.md) · Platform table: [`docs/PLATFORM_AGENTS.md`](docs/PLATFORM_AGENTS.md)

## Monorepo v2 (in progress)

Categories: **`tooling/`** · **`meta/`** · **`platform/`** · **`products/`** (products migration: [#8](https://github.com/shahzebqazi/cursor-agents/issues/8))

- Roadmap: [`docs/MONOREPO_V2_ROADMAP.md`](docs/MONOREPO_V2_ROADMAP.md)
- Kanban: [GitHub Project #16](https://github.com/users/shahzebqazi/projects/16)
- Contribute: [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`AGENTS.md`](AGENTS.md)

## For reviewers

[`docs/employer/README.md`](docs/employer/README.md)

## GitHub Pages

[shahzebqazi.github.io/cursor-agents/](https://shahzebqazi.github.io/cursor-agents/)

```bash
git clone --recurse-submodules https://github.com/shahzebqazi/cursor-agents.git
```

## Related repos

| Repo | Role |
|------|------|
| [cursor-config](https://github.com/shahzebqazi/cursor-config) | Public workspace docs (no secrets) |
| my-cursor-config (private) | Operator workspaces, Pi sync |

## License

MIT — see [LICENSE](LICENSE).
