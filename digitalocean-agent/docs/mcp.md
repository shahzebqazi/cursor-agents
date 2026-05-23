# MCP — DigitalOcean

## Recommended approach

1. **Shell / terminal MCP** with `doctl` on PATH — simplest for agents that run approved commands.
2. **Custom MCP** — only if you need structured resources; keep token in env, not repo.

## Environment

```bash
export DIGITALOCEAN_ACCESS_TOKEN="..."   # never commit
doctl auth init
```

## Example MCP server snippet (local)

Add to the operator's **private** Cursor config (`my-cursor-config` or user settings), not this public repo:

```json
{
  "mcpServers": {
    "shell": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-shell"]
    }
  }
}
```

Pair shell MCP with the **doctl** skill in this package. Restrict write commands via rules in `.cursor/rules/`.

## Private handoff

| Need | Repo |
|------|------|
| Droplet IP, DNS zones, compose paths | `my-droplet-config` |
| Workspace clone list on Pi/Mac | `my-cursor-config` |
