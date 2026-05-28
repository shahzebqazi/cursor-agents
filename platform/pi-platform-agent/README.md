# pi-platform-agent (Cursor)

Public **Raspberry Pi / SBC** patterns: SSH, systemd, and headless **Cursor SDK** invocation. No hostnames, music paths, or operator secrets.

## Scripts

| Script | Purpose |
|--------|---------|
| [`scripts/invoke-cursor-agent.mjs`](scripts/invoke-cursor-agent.mjs) | SDK fallback when `agent` CLI is absent |
| `agent -p` (Cursor CLI) | Preferred one-shot for scheduled `home-agent-run.sh` |
| `agent worker start` | Long-lived **My Machines** bridge (see below) |

### My Machines (`agent worker start`)

Keeps an outbound connection so **cloud** agents can run tools on this host ([docs](https://cursor.com/docs/cloud-agent/my-machines)). Install CLI: `curl https://cursor.com/install -fsS | bash`. Auth via `CURSOR_API_KEY` in operator `~/.env`.

```bash
cd ~/Git/my-cursor-config
agent worker start --name your-pi-host
```

On the Pi, `my-cursor-config` ships `cursor-agent-worker.service` (user systemd) — enable via `install-home-agent-timers.sh`.

**Install (on the Pi, no sudo):**

```bash
# from cursor-agents repo root
bash platform/pi-platform-agent/scripts/setup-runtime.sh
```

Installs **nvm + Node 20**, `npm install` for `@cursor/sdk`, and a **Python venv** with `cursor-sdk` (systemd uses the venv when `node` is not on PATH).

**Secrets:** `CURSOR_API_KEY` in operator `~/.env` (never commit). `home-agent-run.sh` sources it before calling this script.

**Environment (optional):**

| Variable | Default |
|----------|---------|
| `CURSOR_AGENT_MODEL` | `composer-2.5` |
| `HOME_AGENT_INVOKE_SCRIPT` | this repo's `scripts/invoke-cursor-agent.mjs` |
| `HOME_AGENT_PI_PLATFORM_ROOT` | this package directory (`platform/pi-platform-agent`) |

## Private handoff

| Need | Repo |
|------|------|
| Pi timers, `home-agent-run.sh`, publish policy | **my-cursor-config** (`PI_SERVER/home-steward/`) |
| Ampache/MPD deploy, OS slices | **my-pi-server-config** |
| MPD control plane product | **products/music-streaming-agent** (this monorepo) |

## Skills

- [`.cursor/skills/pi-ssh-systemd/SKILL.md`](.cursor/skills/pi-ssh-systemd/SKILL.md)
