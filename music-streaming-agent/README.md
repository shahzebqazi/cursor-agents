# music-streaming-agent

Public **music-server–oriented** tooling inside **[cursor-agents](https://github.com/shahzebqazi/cursor-agents)**: a Python package (`music_agent`) that turns short messages into **validated MPD effects** (`mpc` at the edges), plus optional **LAN HTTP** chat, helper shell scripts, and an Ansible role.

**Canonical deployment surface:** your **music server** repository (or private operator docs)—MPD, audio paths, firewall, TLS, and how this package is vendored—lives there. This tree stays agent-facing, redacted, and safe to publish.

| Doc | Purpose |
|-----|---------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | What runs on the server vs laptop vs editor |
| [docs/INTEGRATION.md](docs/INTEGRATION.md) | Bundle with the music server: paths, env vars, version pinning |
| [docs/README.md](docs/README.md) | Install, run, Ansible, branches |

## Personal Cursor configuration

Optional private rules live in **[cursor-config](https://github.com/shahzebqazi/cursor-config)**. Generic workflow patterns are also described there under `patterns/` if you maintain a private clone.

## Quick install (developer)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
export MPD_HOST='YOUR_MPD_PASSWORD@YOUR_MPD_HOST'
music-agent plan "status"
```

See [docs/README.md](docs/README.md) for the full picture.
