# Agent hub index

**cursor-agents** = public **skills, MCP notes, rules, and agent packages** (doctl, Pi, macOS, Linux, Mastodon, MPD, …).

**my-cursor-config** (private) = personalizations, machine workspaces, and infra/repo routing.

## Monorepo v2 categories

| Category | Packages | Kanban |
|----------|----------|--------|
| **tooling/** | [`git-workspace-agent`](../tooling/git-workspace-agent/) | [Project #16](https://github.com/users/shahzebqazi/projects/16) |
| **meta/** | [`cursor-guide-agent`](../meta/cursor-guide-agent/) | same |
| **platform/** | [`digitalocean-agent`](../platform/digitalocean-agent/), [`pi-platform-agent`](../platform/pi-platform-agent/), [`macos-platform-agent`](../platform/macos-platform-agent/), [`linux-platform-agent`](../platform/linux-platform-agent/) | [#7](https://github.com/shahzebqazi/cursor-agents/issues/7) done |
| **products/** | *(migration pending)* | [#8](https://github.com/shahzebqazi/cursor-agents/issues/8) |
| **employer/** | [`docs/employer/`](employer/README.md) | merged (PR #12) |

Roadmap: [`MONOREPO_V2_ROADMAP.md`](MONOREPO_V2_ROADMAP.md)

## Packages (products — legacy top-level paths)

| Package | Directory | Role |
|---------|-----------|------|
| Music / MPD | [`music-streaming-agent/`](../music-streaming-agent/) | LAN MPD product agent |
| Music library ingest | [`music-library-agent/`](../music-library-agent/) | Picard CLI, quarantine, metadata |
| Mastodon | [`mastodon-agent/`](../mastodon-agent/) submodule | **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** |
| Mastodon (Cursor) | [`mastodon-agent-cursor/`](../mastodon-agent-cursor/) | Cursor charter for submodule |

Moved paths: [`RETIRED_PATHS.md`](RETIRED_PATHS.md)

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
