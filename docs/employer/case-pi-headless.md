# Case: Pi headless agent patterns

## Problem

Run Cursor-compatible agents on a headless host without embedding personal inventory in a public repo.

## Approach

[`platform/pi-platform-agent`](../../platform/pi-platform-agent/): invoke scripts and SSH/systemd skills (patterns only; no steward cron YAML in git).

## Outcome

Shows headless invocation and publish boundaries; operator cron stays private.
