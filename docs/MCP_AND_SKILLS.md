# MCP servers and skills (public catalog)

**cursor-agents** owns **reusable** Cursor integration: skills, MCP server wiring, rules, and small CLIs that any operator can adopt without your private hosts or secrets.

**[my-cursor-config](https://github.com/shahzebqazi/my-cursor-config)** (private) owns **your** machine overlays, repo routing, sync policy, and infra-specific paths.

## What belongs here

| Layer | Examples | Notes |
|-------|----------|--------|
| **Skills** | `doctl` workflows, Pi SSH/systemd, Linux desktop, macOS tooling | No hostnames, no API tokens, no `~/Git` layout |
| **MCP** | Documented server configs (HTTP/SSE, stdio) with env var *names* only | Ship `.example` env files; never real secrets |
| **Rules** | `.cursor/rules/*.mdc` for product agents | Generic behavior, not personal prefs |
| **Packages** | `music-streaming-agent/`, `mastodon-agent/`, `digitalocean-agent/`, … | Runnable or charter-only subtrees |

## What belongs in my-cursor-config

| Layer | Examples |
|-------|----------|
| **Workspaces** | `workspaces/pi-server.yaml`, `macbook-dev.yaml` — machine IDs, clone roots |
| **PI_SERVER/** | systemd units, `sync-policy.yaml`, steward scripts tied to *your* Pi |
| **macbook/** | Merged personal Mac bundle branches |
| **patterns/** | Home-lab clone matrix, consolidation tracker |
| **tools/cursor-config-sync/** | Capture/restore *your* Cursor IDE settings |

## MCP templates (by platform)

Document and extend under each `*-agent/` package README. Suggested servers:

| Platform | Typical MCP / CLI | Env (examples only) |
|----------|-------------------|---------------------|
| **DigitalOcean** | `doctl` via shell MCP or documented manual flows | `DIGITALOCEAN_ACCESS_TOKEN` |
| **Pi / Linux server** | SSH, `systemctl`, `docker` | `PI_HOST`, `PI_SSH_USER` |
| **macOS** | Shell, Homebrew, optional browser MCP for local UI | — |
| **Linux desktop** | Shell, window manager / dotfiles helpers | — |

Add package-local `docs/mcp.md` when a server needs non-obvious setup (OAuth, LAN-only endpoints).

## Skills layout (convention)

```
<package>/
  .cursor/skills/<skill-name>/SKILL.md
  docs/mcp.md              # optional MCP install notes
  .cursor/rules/*.mdc      # optional agent rules
```

Skills here should be **copy-friendly**: assume the reader will fill hostnames and tokens from their private config repo or environment.

## Adding a new platform agent

1. Create `<platform>-agent/` under this repo (see `digitalocean-agent/` stub).
2. Add skills + MCP docs; keep secrets out of git.
3. Link from [`HUB_INDEX.md`](HUB_INDEX.md) and [`PLATFORM_AGENTS.md`](PLATFORM_AGENTS.md).
4. If you need *your* droplet IP, Pi hostname, or repo clone list → document the handoff in **my-cursor-config** only.
