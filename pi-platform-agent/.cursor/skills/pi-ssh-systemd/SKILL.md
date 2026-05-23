---
name: pi-ssh-systemd
description: Use when operating a Raspberry Pi or Linux SBC over SSH — systemd units, Docker, logs, and read-only health checks. Host-specific paths come from my-cursor-config or my-pi-server-config on the operator machine.
---

# Pi / SBC over SSH

## Scope

- Generic SSH + systemd + Docker workflows.
- **Not here:** hostname `iconoclast-audio-pi-server`, dragon paths, or your `sync-policy.yaml`.

## Safety

- Read-only first: `systemctl status`, `journalctl -u … --no-pager -n 50`, `docker ps`.
- Ask before `systemctl restart`, `docker compose down`, or package installs.

## Patterns

```bash
ssh "${PI_USER}@${PI_HOST}" 'systemctl --failed'
ssh "${PI_USER}@${PI_HOST}" 'docker ps --format "table {{.Names}}\t{{.Status}}"'
```

Set `PI_HOST` / `PI_USER` from private config — never hardcode in this public repo.

## Related

- **music-streaming-agent** — MPD product agent
- **my-pi-server-config** — your Pi repo
