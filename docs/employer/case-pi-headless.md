# Case: Pi headless agent patterns

## Problem

Run Cursor-compatible agents on a headless host (SSH, systemd) without embedding personal inventory in a public repo.

## Approach

- Package: [`pi-platform-agent`](../../pi-platform-agent/) *(migrating to `platform/pi-platform-agent/`)*
- Scripts: `invoke-cursor-agent.mjs` / `.py`, `setup-runtime.sh` (patterns only)
- Skills: SSH/systemd/Docker **patterns** — no Pi hostname, no steward job YAML

## Outcome

Demonstrates **headless agent invocation** and publish boundaries; private cron and `home-steward` stay in operator config.

## Try it

Read `pi-platform-agent/README.md` and skills under `.cursor/skills/` — adapt paths locally; do not expect live Pi credentials in git.
