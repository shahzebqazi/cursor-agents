# Platform agents (public)

Product-style agents integrate Cursor with a **class** of host or service. No operator-specific inventory.

| Agent / package | Status | Scope |
|-----------------|--------|--------|
| [music-streaming-agent](../music-streaming-agent/) | **Active** | LAN MPD control (`music_agent` CLI, optional HTTP) |
| [music-library-agent](../music-library-agent/) | **Active** | Picard CLI ingest, quarantine, metadata |
| [mastodon-agent](../mastodon-agent/) (submodule) | **Active** | Mastodon posting from drafts |
| [mastodon-agent-cursor](../mastodon-agent-cursor/) | **Active** | Cursor charter for Mastodon submodule |
| [digitalocean-agent](../platform/digitalocean-agent/) | **Stub** | `doctl`, droplet/DNS/App Platform skills + MCP notes |
| [pi-platform-agent](../platform/pi-platform-agent/) | **Stub** | Pi ops: SSH, systemd, Docker patterns |
| [macos-platform-agent](../platform/macos-platform-agent/) | **Active** | macOS dev + [clear-archived-cursor-chats](../platform/macos-platform-agent/.cursor/skills/clear-archived-cursor-chats/SKILL.md) |
| [linux-platform-agent](../platform/linux-platform-agent/) | **Stub** | Linux desktop/server patterns |

## Private operator config

Machine names, `~/Git` clone lists, sync cron live in **my-cursor-config** — not here.

## Related infra repos (not Cursor agents)

| Repo | Role |
|------|------|
| `my-droplets` | DO droplet compose + inventory (private) |
| `my-pi-server` | Pi scripts + sync anchor (private) |
| `my-linux-server-config` | Charon / homelab Linux (private) |
| `my-mac-config` | Mac bootstrap + satellites (private) |
