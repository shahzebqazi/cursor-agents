---
name: doctl
description: Use when managing DigitalOcean droplets, DNS, App Platform, or firewalls via doctl. Public workflows only; load private inventory from the operator's my-droplet-config repo.
---

# doctl (DigitalOcean CLI)

## Scope

- **This skill:** generic `doctl` commands, safety checks, and API patterns.
- **Not here:** account-specific IPs, domains, or inventory JSON — read **`my-droplet-config`** on the operator machine if present.

## Safety

- Prefer **read** commands (`doctl compute droplet list`, `doctl compute domain records list`) before mutations.
- Never print or commit `DIGITALOCEAN_ACCESS_TOKEN`.
- Confirm droplet name/ID with the user before `delete`, `power-off`, or DNS record changes.

## Common flows

```bash
doctl auth init   # interactive once per machine
doctl account get
doctl compute droplet list --format ID,Name,PublicIPv4,Region
doctl compute domain list
doctl apps list
```

## MCP

See `digitalocean-agent/docs/mcp.md` when added. Until then, use shell MCP or terminal with `doctl` on PATH.

## Related repos

| Repo | Visibility | Contents |
|------|------------|----------|
| **my-droplet-config** | private | `home-stack/`, `digitalocean-networks/` inventory |
| **cursor-agents** | public | This skill + future MCP notes |
