---
name: git-workspace-hygiene
description: >
  Git hygiene for multi-repo ~/Git workspaces: dirty-tree checks, ff-only pulls,
  parallel session branch discipline. Use before pull/push or when multiple agents
  share a clone.
---

# Git workspace hygiene

## When to use

Before `git pull`/`git push` on any clone under your git root, or when multiple Cursor sessions may touch the same repo.

## Rules

1. `git status -sb` — if not clean, do not pull or push ([`docs/dirty-tree-strategies.md`](../../docs/dirty-tree-strategies.md)).
2. At session start, note `git branch --show-current`; stay on that branch unless scope changes.
3. No `git push --force` to shared branches unless the operator asks.
4. Never commit `.env`, keys, tokens, or credential files.
5. After a clean tree: `git pull --ff-only`.

Parallel sessions: [`docs/parallel-sessions.md`](../../docs/parallel-sessions.md).

## Out of scope

Service features, DNS, infra apply, autonomous merges — use the owning repo charter.
