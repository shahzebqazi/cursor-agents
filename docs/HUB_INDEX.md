# Agent hub index

**cursor-agents** = public **skills, MCP notes, rules, and agent packages** (doctl, Pi, macOS, Linux, Mastodon, MPD, …).

**my-cursor-config** (private) = personalizations, machine workspaces, and infra/repo routing.

## Packages in this monorepo

| Package | Directory | Role |
|---------|-----------|------|
| Music / MPD | [`music-streaming-agent/`](../music-streaming-agent/) | Pi LAN MPD product agent |
| Music library ingest | [`music-library-agent/`](../music-library-agent/) | Picard CLI, quarantine, metadata, dragon ingest |
| Mastodon | [`mastodon-agent/`](../mastodon-agent/) submodule | Product repo **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** |
| Mastodon (Cursor) | [`mastodon-agent-cursor/`](../mastodon-agent-cursor/) | Cursor charter for submodule |
| DigitalOcean | [`digitalocean-agent/`](../digitalocean-agent/) | `doctl` skills + MCP (stub) |
| Pi platform | [`pi-platform-agent/`](../pi-platform-agent/) | SSH/systemd/Docker patterns (stub) |
| macOS platform | [`macos-platform-agent/`](../macos-platform-agent/) | macOS dev patterns (stub) |
| Linux platform | [`linux-platform-agent/`](../linux-platform-agent/) | Linux patterns (stub) |

Skills/MCP convention: [`MCP_AND_SKILLS.md`](MCP_AND_SKILLS.md) · Platform table: [`PLATFORM_AGENTS.md`](PLATFORM_AGENTS.md).

## Not in this repo (by design)

| Need | Use instead |
|------|-------------|
| `~/Git` clone list, Pi cron, steward scripts | **[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** — `PI_SERVER/` (clone dir often `cursor-config/`) |
| Pi production scripts, Nextcloud, nginx | **[my-pi-server-config](https://github.com/shahzebqazi/my-pi-server-config)** (private; clone dir often `pi-server/`) |
| Mac Nix + satellites | **[my-mac-config](https://github.com/shahzebqazi/my-mac-config)** (private) |
| Public Mac patterns | **[mac-config](https://github.com/shahzebqazi/mac-config)** (public) |

## Migrated standalone repos

| Former name | Today |
|-------------|--------|
| `cursor-music-streaming-agent` | `music-streaming-agent/` |
| `mastodon-cursor-agent` | **mastodon-agent** + submodule + `mastodon-agent-cursor/` |
| `cursor-agent-config`, `cursor-config` (GitHub rename) | **my-cursor-config** (private) |
| `iconoclast-server`, `pi-server` (GitHub rename) | **my-pi-server-config** (private) |
| `git-meta-agent`, `home-meta-agent` | **my-cursor-config/PI_SERVER/** (local Pi clones retired) |
