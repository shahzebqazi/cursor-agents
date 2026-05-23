# Agent hub index

**cursor-agents** = public **skills, MCP notes, rules, and agent packages** (doctl, Pi, macOS, Linux, Mastodon, MPD, …).

**my-cursor-config** = private **personalizations**, machine workspaces, and infra/repo routing.

## Packages in this monorepo

| Package | Directory | Role |
|---------|-----------|------|
| Music / MPD | [`music-streaming-agent/`](../music-streaming-agent/) | Pi LAN MPD product agent |
| Mastodon | [`mastodon-agent/`](../mastodon-agent/) submodule | Product repo + Cursor charter |
| DigitalOcean | [`digitalocean-agent/`](../digitalocean-agent/) | `doctl` skills + MCP (stub) |
| Pi platform | [`pi-platform-agent/`](../pi-platform-agent/) | SSH/systemd/Docker patterns (stub) |
| macOS platform | [`macos-platform-agent/`](../macos-platform-agent/) | macOS dev patterns (stub) |
| Linux platform | [`linux-platform-agent/`](../linux-platform-agent/) | Linux patterns (stub) |

Skills/MCP convention: [`MCP_AND_SKILLS.md`](MCP_AND_SKILLS.md) · Platform table: [`PLATFORM_AGENTS.md`](PLATFORM_AGENTS.md).

## Not in this repo (by design)

| Need | Use instead |
|------|-------------|
| Your `~/Git` clone list, Pi cron, steward scripts | **[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** |
| DO inventory, droplet compose | **my-droplet-config** (private) |
| Pi server scripts | **my-pi-server-config** (private) |
| Mac Nix + satellites | **my-mac-config** (private) |
| Public dotfile examples | **dotfiles** (public) |

## Migrated standalone repos

| Former name | Today |
|-------------|--------|
| `cursor-music-streaming-agent` | `music-streaming-agent/` |
| `mastodon-cursor-agent` | **mastodon-agent** + submodule |
| `cursor-config` | **my-cursor-config** (private) |
