# Agent hub index

**cursor-agents** = public **skills, MCP notes, rules, and agent packages**.

**my-cursor-config** (private) = personalizations, machine workspaces, and infra/repo routing.

## Categories

| Category | Packages |
|----------|----------|
| **tooling/** | [`git-workspace-agent`](../tooling/git-workspace-agent/) |
| **meta/** | [`cursor-guide-agent`](../meta/cursor-guide-agent/) |
| **platform/** | [`digitalocean-agent`](../platform/digitalocean-agent/), [`pi-platform-agent`](../platform/pi-platform-agent/), [`macos-platform-agent`](../platform/macos-platform-agent/), [`linux-platform-agent`](../platform/linux-platform-agent/) |
| **products/** | [`music-streaming-agent`](../products/music-streaming-agent/), [`music-library-agent`](../products/music-library-agent/), [`mastodon-agent`](../products/mastodon-agent/) submodule, [`mastodon-agent-cursor`](../products/mastodon-agent-cursor/) |
| **employer/** | [`docs/employer/`](employer/README.md) |

Kanban: [Project #16](https://github.com/users/shahzebqazi/projects/16) · Roadmap: [`MONOREPO_V2_ROADMAP.md`](MONOREPO_V2_ROADMAP.md) · Moved paths: [`RETIRED_PATHS.md`](RETIRED_PATHS.md)

Skills/MCP: [`MCP_AND_SKILLS.md`](MCP_AND_SKILLS.md) · Platform/product status: [`PLATFORM_AGENTS.md`](PLATFORM_AGENTS.md)

## Sibling showcase

| Need | Use |
|------|-----|
| Brand asset codegen, desktop UX mockups, design guide | **[mystic-ai](https://github.com/shahzebqazi/mystic-ai)** — [`docs/HUB_INDEX.md`](https://github.com/shahzebqazi/mystic-ai/blob/main/docs/HUB_INDEX.md) |

## Not in this repo (by design)

| Need | Use instead |
|------|-------------|
| `~/Git` clone list, Pi cron, steward scripts | **[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** |
| Pi production scripts, Nextcloud, nginx | **[my-pi-server-config](https://github.com/shahzebqazi/my-pi-server-config)** (private) |
| Mac Nix + satellites | **[my-mac-config](https://github.com/shahzebqazi/my-mac-config)** (private) |

## Migrated standalone repos

| Former name | Today |
|-------------|--------|
| `cursor-music-streaming-agent` | `products/music-streaming-agent/` |
| `mastodon-cursor-agent` | `products/mastodon-agent/` + submodule + `products/mastodon-agent-cursor/` |
| `cursor-agent-config`, `cursor-config` (GitHub rename) | **my-cursor-config** (private) |
| `iconoclast-server`, `pi-server` (GitHub rename) | **my-pi-server-config** (private) |
