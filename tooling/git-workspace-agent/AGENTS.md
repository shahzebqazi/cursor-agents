# AGENTS.md — git-workspace-agent

## Role

Maintain **deterministic git hygiene** for clones under a configurable git root (convention: `~/Git/`). Each clone’s **leaf directory name** should match its remote repo name. Paths may be **grouped** (`<group>/<repo>/`) per your layout manifest.

## In scope

- Detect dirty trees before pull/push; log and skip when unsafe
- Branch discipline for parallel Cursor sessions ([`docs/parallel-sessions.md`](docs/parallel-sessions.md))
- Align remotes and branch tracking when operator asks
- Doc-only commits on allowlisted extensions when explicitly requested

## Out of scope

- Service feature work (use `<repo>/AGENTS.md`)
- Home-disk / steward policy on appliances
- `git push --force` to shared branches
- Autonomous merge to `main` without human or PR review
- Executing LLM output as shell without confirmation

## Must not

- Pull or push with a **dirty** working tree (including untracked files that block sync)
- Delete clones or bulk data without operator approval
- Commit secrets (`.env`, keys, `credentials.json`, tokens)

## Dirty trees

See [`docs/dirty-tree-strategies.md`](docs/dirty-tree-strategies.md).

## Workspace handoff

| File | Purpose |
|------|---------|
| Workspace index (e.g. `~/Git/AGENTS.md`) | Short routing to repos |
| `<repo>/AGENTS.md` | Product/service work |
| This charter | Sync and branch hygiene only |

## Skill

Enable [`.cursor/skills/git-workspace-hygiene/SKILL.md`](.cursor/skills/git-workspace-hygiene/SKILL.md) in Cursor.
