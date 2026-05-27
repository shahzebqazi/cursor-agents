# Architecture — public boundary

```text
┌─────────────────────────────────────────────────────────────┐
│  cursor-agents (this repo)                                   │
│  Skills · MCP notes · charters · small scripts               │
│  No tokens · no hostnames · no personal clone matrices       │
└───────────────────────────┬─────────────────────────────────┘
                            │ fork / copy skills
┌───────────────────────────▼─────────────────────────────────┐
│  cursor-config (public mirror)                               │
│  Generic ~/Git docs · examples · patterns                    │
└───────────────────────────┬─────────────────────────────────┘
                            │ operator-only
┌───────────────────────────▼─────────────────────────────────┐
│  my-cursor-config (private)                                  │
│  Workspaces · Pi systemd · publish policy · machine YAML     │
└───────────────────────────┬─────────────────────────────────┘
                            │ deploy / inventory
┌───────────────────────────▼─────────────────────────────────┐
│  Infra repos (private): my-droplets, my-pi-server, …         │
└─────────────────────────────────────────────────────────────┘
```

## Package categories (v2)

| Category | Examples | Reviewer signal |
|----------|----------|-----------------|
| **tooling/** | git-workspace-agent | Agent SDLC, safe automation |
| **meta/** | cursor-guide-agent | UX for agent routing |
| **platform/** | digitalocean, pi, macos, linux | Integration boundaries |
| **products/** | music-*, mastodon | Shipped workflows |

Legacy top-level dirs remain during migration; see [`MONOREPO_V2_ROADMAP.md`](../MONOREPO_V2_ROADMAP.md).

## Submodule

**mastodon-agent** product code is canonical in [shahzebqazi/mastodon-agent](https://github.com/shahzebqazi/mastodon-agent). This monorepo holds a pointer + Cursor glue only.
