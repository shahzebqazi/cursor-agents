# Platform and product agents (public)

No operator-specific inventory in this repo.

## Products

| Package | Status | Scope |
|---------|--------|--------|
| [music-streaming-agent](../products/music-streaming-agent/) | **Active** | LAN MPD control (`music_agent` CLI, optional HTTP) |
| [music-library-agent](../products/music-library-agent/) | **Active** | Picard CLI ingest, quarantine, metadata |
| [mastodon-agent](../products/mastodon-agent/) (submodule) | **Active** | Mastodon posting from drafts |
| [mastodon-agent-cursor](../products/mastodon-agent-cursor/) | **Active** | Cursor charter for Mastodon submodule |

## Platform

| Package | Status | Scope |
|---------|--------|--------|
| [digitalocean-agent](../platform/digitalocean-agent/) | **Stub** | `doctl`, droplet/DNS/App Platform skills + MCP notes |
| [pi-platform-agent](../platform/pi-platform-agent/) | **Stub** | Pi ops: SSH, systemd, Docker, headless invoke |
| [macos-platform-agent](../platform/macos-platform-agent/) | **Active** | macOS dev + [clear-archived-cursor-chats](../platform/macos-platform-agent/.cursor/skills/clear-archived-cursor-chats/SKILL.md) |
| [linux-platform-agent](../platform/linux-platform-agent/) | **Stub** | Linux desktop/server patterns |

## Private operator config

Machine names, `~/Git` clone lists, sync cron: **my-cursor-config**.

## Related infra (not Cursor agents)

| Repo | Role |
|------|------|
| `my-droplets` | DO compose + inventory (private) |
| `my-pi-server` | Pi scripts + sync anchor (private) |
