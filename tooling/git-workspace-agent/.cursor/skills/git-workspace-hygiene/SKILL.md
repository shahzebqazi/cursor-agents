---
name: git-workspace-hygiene
description: >
  Git hygiene for multi-repo ~/Git workspaces: dirty-tree checks, ff-only pulls,
  parallel session branch discipline, and safe sync skips. Use before pull/push
  or when multiple agents touch the same clone.
---

# Git workspace hygiene

## When to use

- Before `git pull`, `git push`, or automated sync on any clone under your git root
- When multiple Cursor sessions or agents may touch the same repository
- When aligning grouped paths (`<group>/<repo>/`) with remote repo names

## Rules

1. Run `git status -sb` — if not clean, **do not pull or push** until resolved (see package `docs/dirty-tree-strategies.md`).
2. At session start, note `git branch --show-current`; stay on that branch unless the user changes scope.
3. Never `git push --force` to shared branches (`main`, `dev`) unless the operator explicitly requests it.
4. Never commit `.env`, keys, tokens, or credential files.
5. Prefer `git pull --ff-only` after a clean tree.

## Dirty tree strategies

| Strategy | When |
|----------|------|
| **Stash** | Keep WIP — `git stash push -u -m "git-agent: …"` then ff-only pull |
| **WIP branch** | Publish WIP — `wip/agent-YYYYMMDD-topic` |
| **Skip** | Log and leave tree dirty for operator |
| **Reset** | Operator approval only — `git fetch && git reset --hard origin/<branch>` |

## Parallel sessions

One topic per branch when practical: `feature/<topic>-<short-id>`. Confirm branch again before commit.

## Out of scope

Service features, DNS, infrastructure apply, and autonomous merges — use the owning repo’s charter.

## Reference

Package docs: `tooling/git-workspace-agent/` in [cursor-agents](https://github.com/shahzebqazi/cursor-agents).
