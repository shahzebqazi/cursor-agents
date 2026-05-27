# git-workspace-agent

**Problem:** Multiple Cursor sessions and automation jobs fight over the same `~/Git` clones unless branch and sync rules are explicit.

**Use this package when:** You want deterministic git hygiene for a multi-repo workspace (grouped layout, dirty-tree handling, parallel agent sessions).

## Quick start

1. Copy [`.cursor/skills/git-workspace-hygiene/SKILL.md`](.cursor/skills/git-workspace-hygiene/SKILL.md) into your project or enable from this path.
2. Read [`AGENTS.md`](AGENTS.md) for charter boundaries.
3. Adapt [`docs/layout-template.yaml`](docs/layout-template.yaml) with **your** repo names (placeholders only).

## Contents

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Agent charter (public, sanitized) |
| `docs/dirty-tree-strategies.md` | Stash / WIP branch / skip pull |
| `docs/parallel-sessions.md` | Branch discipline for parallel agents |
| `docs/layout-template.yaml` | Example grouped `~/Git` manifest |

## Private operator layer

Machine-specific sync cron, publish policy, and host profiles belong in **your** private config repo — not here.
