# pi-platform-agent (Cursor)

Public **Raspberry Pi / SBC** patterns: SSH, systemd, Docker, and workspace hygiene skills. Does not contain your Pi hostname, music stack paths, or sync cron.

## Private handoff

| Need | Repo |
|------|------|
| Pi scripts, `GIT_WORKSPACE_SYNC`, Ampache/MPD deploy | **my-pi-server-config** |
| `~/Git` clone policy, daily workspace agent | **my-cursor-config** (`PI_SERVER/`) |
| MPD control plane product | **music-streaming-agent** (this monorepo) |

## Planned contents

- `.cursor/skills/pi-ssh-systemd/SKILL.md`
- `docs/mcp.md` — SSH/shell MCP notes
- `.cursor/rules/pi-platform-agent.mdc`

## Status

Stub.
