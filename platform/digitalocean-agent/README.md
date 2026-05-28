# digitalocean-agent (Cursor)

Public **DigitalOcean** agent package: skills and MCP guidance for `doctl`, droplets, DNS, App Platform, and firewalls.

## Out of scope (use my-cursor-config)

- Account email, team IDs, droplet IPs, invoice snapshots
- Clone paths under `~/Git` for your stacks
- Live inventory JSON

Those live in private **[my-droplets](https://github.com/shahzebqazi/my-droplets)** (`digitalocean-networks/`, `home-stack/`).

## Planned contents

| Path | Purpose |
|------|---------|
| `.cursor/skills/doctl/SKILL.md` | Safe `doctl` workflows (read-only defaults) |
| `docs/mcp.md` | MCP / shell integration for DO API |
| `.cursor/rules/digitalocean-agent.mdc` | Cursor rules when working in DO context |

## Prerequisites

- [`doctl`](https://docs.digitalocean.com/reference/doctl/) installed
- `DIGITALOCEAN_ACCESS_TOKEN` in environment (never commit)

## Status

Stub — skills and MCP docs to be added incrementally.
