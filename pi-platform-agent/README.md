# pi-platform-agent (Cursor)

Public **Raspberry Pi / SBC** patterns: SSH, systemd, and headless **Cursor SDK** invocation. No hostnames, music paths, or operator secrets.

## Scripts

| Script | Purpose |
|--------|---------|
| [`scripts/invoke-cursor-agent.mjs`](scripts/invoke-cursor-agent.mjs) | One-shot `Agent.prompt` for scheduled home-agent runs |

**Install (on the Pi, no sudo):**

```bash
bash ~/Git/cursor-agents/pi-platform-agent/scripts/setup-runtime.sh
```

Installs **nvm + Node 20**, `npm install` for `@cursor/sdk`, and a **Python venv** with `cursor-sdk` (systemd uses the venv when `node` is not on PATH).

**Secrets:** `CURSOR_API_KEY` in operator `~/.env` (never commit). `home-agent-run.sh` sources it before calling this script.

**Environment (optional):**

| Variable | Default |
|----------|---------|
| `CURSOR_AGENT_MODEL` | `composer-2.5` |
| `HOME_AGENT_INVOKE_SCRIPT` | this repo's `scripts/invoke-cursor-agent.mjs` |
| `HOME_AGENT_PI_PLATFORM_ROOT` | `~/Git/cursor-agents/pi-platform-agent` |

## Private handoff

| Need | Repo |
|------|------|
| Pi timers, `home-agent-run.sh`, publish policy | **my-cursor-config** (`PI_SERVER/home-steward/`) |
| Ampache/MPD deploy, OS slices | **my-pi-server-config** |
| MPD control plane product | **music-streaming-agent** (this monorepo) |

## Skills

- [`.cursor/skills/pi-ssh-systemd/SKILL.md`](.cursor/skills/pi-ssh-systemd/SKILL.md)
