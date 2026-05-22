# cursor-music-streaming-agent

This file lives under `docs/`. Shell examples assume your shell’s current working directory is the **repository root** (the parent of `docs/`).

LAN-facing control plane for MPD: a small **pure core** (situation → effects) with **IO at the edges** (`mpc`). Optional **stdlib HTTP** chat for phones over VPN.

**Repository entry points:** root [`README.md`](../README.md) (GitHub landing), [`docs/ARCHITECTURE.md`](ARCHITECTURE.md) (what runs where), [`docs/INTEGRATION.md`](INTEGRATION.md) (bundle with your music server), [`docs/MIGRATION_CHECKLIST.md`](MIGRATION_CHECKLIST.md) (clone/remote hygiene).

## Shared agent conventions (public)

Generic **GitHub Projects / Kanban habits**, **parallel-agent branch discipline**, and optional **Cursor** scaffolding patterns live in **[shahzebqazi/cursor-config](https://github.com/shahzebqazi/cursor-config)** (`patterns/` and `.cursor/rules/`). This repo links there so third parties can reproduce workflow guidance without private config.

**Private** Cursor production rules, hooks, and legally sensitive or unpublished-library workflows stay in **`my-cursor-config`** (private) or out of git entirely—this public tree must never depend on them to build or run.

## Install (editable, any machine with Python ≥ 3.11)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Mac or Linux client (control remote MPD)

Use **`mpc`** pointed at the host where MPD listens. Example (placeholders):

```bash
export MPD_HOST='YOUR_MPD_PASSWORD@YOUR_MPD_LAN_HOSTNAME_OR_IP'
mpc status
```

For an interactive TUI, **`ncmpcpp`** is the usual companion to `mpc` (configure the same host/port in `~/.config/ncmpcpp/config`).

## Run the LAN agent (server or dev machine)

```bash
export MPD_HOST='YOUR_MPD_PASSWORD@YOUR_MPD_HOST'
music-agent serve --host 0.0.0.0 --port 8765
```

Then `POST http://YOUR_AGENT_HOST:8765/chat` with JSON `{"message":"volume 40","device_id":"phone-1"}`.

## Ansible

See [`ansible/playbook.yml`](../ansible/playbook.yml) and [`ansible/inventory.example.yml`](../ansible/inventory.example.yml).

Ansible **does not install or replace MPD**; it installs this agent under `music_agent_install_root` (default `/opt/cursor-music-streaming-agent`), creates a venv, writes `/etc/default/music-agent` with `MPD_HOST=…`, and enables `music-agent.service`.

**Operator workflow:** sync this repository to the target directory on the server, then run Ansible from a machine that can SSH with privilege escalation:

```bash
rsync -a --delete --exclude .git --exclude .venv ./ YOUR_SERVER:/opt/cursor-music-streaming-agent/
ansible-playbook -i ansible/inventory.example.yml ansible/playbook.yml \
  -e music_agent_mpd_host='YOUR_MPD_PASSWORD@127.0.0.1'
```

Use `127.0.0.1` on the same host as MPD when `mpc` is configured that way today; otherwise use the host/IP MPD exposes to the agent user.

### Example MPD layout (illustrative only)

A typical server might use:

- **`music_directory`** under a path you choose (for example `/var/lib/mpd/music`)
- **Bind address** and password from your own `mpd.conf` fragments (not committed here)
- **systemd drop-ins** for `mpd.service` if you need `network-online` ordering before binding to a LAN IP—see [`scripts/install/`](../scripts/install/)

## Public vs private operator material

| Public (`cursor-music-streaming-agent`) | Private (music server repo, `my-cursor-config`, or local only) |
|----------------------------------------|------------------------------------------------------------------|
| Redacted examples and `*.example.yml` | Real inventory, `host_vars`, Tailscale/WireGuard names |
| Generic Ansible role | Production `music_agent_mpd_host`, TLS material, SSH keys |
| Agent code + capability matrix | One-off library sync scripts with real mount points and artist folders |

## Branches

- `main` — production-aligned snapshots  
- `dev` — integration  
- `feature/*` — agent or feature work; merge to `dev` after you test  

## Scripts

- [`scripts/queue_playlist_by_name.sh`](../scripts/queue_playlist_by_name.sh) — load or append a stored playlist via `mpc` (`MPD_HOST` required).
- [`scripts/install/`](../scripts/install/) — optional MPD systemd drop-in helper for `network-online` ordering.
- [`scripts/examples/`](../scripts/examples/) — redacted templates (copy into a private repo before specializing paths).