# Architecture (short)

## Music server (your deployment repo or appliance)

- **MPD** (or equivalent) owns playback, the music library path, outputs, and long-lived **systemd** units for `mpd`.
- **Network and security**: LAN bind addresses, VPN, reverse proxies, and TLS are decided here—not in `cursor-music-streaming-agent`.
- **How this package appears**: a directory on disk (often `/opt/cursor-music-streaming-agent` or a path you choose), populated by `rsync`, `git pull`, submodule checkout, or monorepo layout (see [INTEGRATION.md](INTEGRATION.md)).

## Agent runtime (this repository)

- **Python package** `music_agent` (`src/music_agent/`): parses user text into an ordered list of **`Effect`** values, checks them against a **situation** snapshot from MPD, and executes through **`mpc`** (subprocess). No cloud LLM is called from this package.
- **Optional LAN HTTP** (`music-agent serve`): stdlib `ThreadingHTTPServer`, `POST /chat` for JSON control from phones or scripts on the same LAN/VPN.
- **Ansible role** `music_agent`: installs the package into a venv, writes `/etc/default/music-agent` with `MPD_HOST`, installs `music-agent.service`. It **does not** replace or install MPD itself.
- **Shell scripts** under `scripts/`: operator helpers (playlists, systemd drop-in examples). Treat paths in **`scripts/examples/*.example.sh`** as templates you copy and specialize privately if needed.

## Local development (engineer laptop)

- Editable install (`pip install -e .`), `MPD_HOST` pointing at a reachable MPD (local or over VPN), and tests/smoke via `music-agent plan "…"`.
- **Cursor / other editors**: optional `.cursor/` rules can be vendored from **my-cursor-config**; they are not required to build or run the package.

## Documentation split

| Location | Audience |
|----------|----------|
| `docs/` here | Anyone integrating MPD + this agent |
| **my-cursor-config** `patterns/` | Generic agent + GitHub workflow habits |
| Private operator repo | Secrets, real hosts, one-off library sync jobs |
