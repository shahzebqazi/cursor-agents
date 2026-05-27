# cursor-guide-agent

**Problem:** New Cursor users need a read-only guide that explains which package in this monorepo owns their task—without touching private operator repos.

## Quick start

1. Add [`.cursor/agents/cursor-guide.md`](.cursor/agents/cursor-guide.md) to your workspace (Ask / readonly).
2. Ask: “Which agent package should I use for …?”
3. For implementation, switch to **Agent mode** and open the package listed in [`AGENTS.md`](AGENTS.md).

## Not included

LinkedIn automation, homelab hostnames, publish cron, or secrets — those stay in private operator config.
