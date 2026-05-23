# Platform agents (public)

Product-style agents in **cursor-agents** integrate Cursor with a **class** of host or service. They do not store operator-specific inventory.

| Agent / package | Status | Scope |
|-----------------|--------|--------|
| [music-streaming-agent](../music-streaming-agent/) | **Active** | LAN MPD control (`music_agent` CLI, optional HTTP) |
| [music-library-agent](../music-library-agent/) | **Active** | Picard CLI ingest, quarantine, metadata (dragon SSD) |
| [mastodon-agent](../mastodon-agent/) (submodule) | **Active** | Mastodon posting from drafts |
| [mastodon-agent-cursor](../mastodon-agent-cursor/) | **Active** | Cursor charter for Mastodon submodule |
| [digitalocean-agent](../digitalocean-agent/) | **Stub** | `doctl`, droplet/DNS/App Platform skills + MCP notes |
| [pi-platform-agent](../pi-platform-agent/) | **Stub** | Pi ops: SSH, systemd, Docker, workspace pull policy *patterns* |
| [macos-platform-agent](../macos-platform-agent/) | **Stub** | macOS dev: shell, Homebrew, AeroSpace/Leader Key *patterns* (not personal dotfiles) |
| [linux-platform-agent](../linux-platform-agent/) | **Stub** | Linux desktop/server: xmonad, dotfiles *patterns*, LAN services |

## Private operator config

Machine names, `~/Git` clone lists, sync cron, and consolidation state live in **[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** — not here.

## Related infra repos (not Cursor agents)

| Repo | Role |
|------|------|
| `my-droplet-config` | DO droplet compose + inventory (private) |
| `my-pi-server-config` | Pi scripts + sync anchor (private) |
| `my-linux-server-config` | Charon / homelab Linux (private) |
| `my-mac-config` | Mac bootstrap + satellites (private) |
