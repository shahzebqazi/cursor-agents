# Integrating with the music server

This repository is designed to **ship alongside** a **music server** project: the server repo (or private runbooks) owns MPD, OS tuning, and deployment; this repo supplies the **agent layer** (Python + optional HTTP + Ansible for the agent only).

Nothing here requires access to a private repository to build or run.

## Install location (convention)

The Ansible defaults use:

- **`music_agent_install_root`**: `/opt/cursor-music-streaming-agent` (override with `-e` / inventory).
- **venv**: `{{ music_agent_install_root }}/.venv`
- **systemd**: `music-agent.service` reads `MPD_HOST` from `/etc/default/music-agent` (mode `0640`, root-owned).

You may install under `$HOME` on a dev host instead; adjust paths and skip systemd.

## Environment variables

| Variable | Where | Meaning |
|----------|--------|---------|
| `MPD_HOST` | Shell, `/etc/default/music-agent`, dev laptop | Standard `mpc` form: optional `password@host`, port via `MPD_PORT` if needed. On the same host as MPD, often `password@127.0.0.1`. |
| `XDG_DATA_HOME` | Optional | Used for per-device volume memory (`volume_profiles.json`) when set; otherwise platform defaults. |

Never commit real passwords or hostnames into this public tree.

## Version pinning

- **PyPI:** not required; today the package is installed **from a git checkout** (`pip install -e .` in the synced directory).
- **Pin by git:** record the **commit SHA** or **tag** in your music server repo (submodule, lockfile note, or release checklist). Example: `git -C /opt/cursor-music-streaming-agent rev-parse HEAD`.
- **`pyproject.toml` `version`:** marketing-style API version (`0.1.0` today); bump when you tag releases. Align tags with whatever your server repo documents.

## How updates roll out

Typical flow (same as [docs/README.md](README.md) Ansible section):

1. **Sync tree** to the server directory (example):  
   `rsync -a --delete --exclude .git --exclude .venv ./ music-server:/opt/cursor-music-streaming-agent/`
2. **Reinstall** into the venv: `pip install -e .` inside that tree (Ansible does this).
3. **Restart** `music-agent.service` if the agent code changed.

MPD itself is restarted only when *its* config or library layout changes—handled in the music server repo, not assumed here.

## Submodule vs vendor copy vs monorepo

| Approach | Pros | Cons |
|----------|------|------|
| **Git submodule** | Pin exact upstream SHA; upstream stays a separate clone/fetch. | Contributors must run `git submodule update`; two PR flows unless automated. |
| **Vendor copy** (rsync / subtree) | Simple mental model; music server repo is self-contained snapshot. | Drift until someone manually refreshes; merge conflicts on refresh. |
| **Monorepo** | Single CI pipeline and atomic changes across MPD config + agent. | Larger clone; blurs “public agent” vs “private infra” unless paths are disciplined. |

Pick one, document it in the **music server** repository, and link to this file for the agent half.

## Public vs private content

- **Public here:** code, generic docs, `ansible/inventory.example.yml`, and templates under [`scripts/examples/`](../scripts/examples/).
- **Private elsewhere:** real `inventory.yml`, VPN or internal DNS names, `rsync` targets, paid API keys, unpublished-library ingestion scripts derived from those templates.

See [MIGRATION_CHECKLIST.md](MIGRATION_CHECKLIST.md) when moving material between repos.
