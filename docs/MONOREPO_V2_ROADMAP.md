# Monorepo v2 roadmap

**Kanban:** [GitHub Project #16 — cursor-agents — monorepo v2](https://github.com/users/shahzebqazi/projects/16)

## Target layout

```text
cursor-agents/
├── tooling/          # git-workspace-agent, …
├── meta/             # cursor-guide-agent, …
├── platform/         # digitalocean, pi, macos, linux
├── products/         # music-*, mastodon-*
└── docs/employer/    # reviewer case cards
```

**Today:** new categories are **additive**. Legacy top-level package dirs remain until migration PRs land ([issue #8](https://github.com/shahzebqazi/cursor-agents/issues/8), [#9](https://github.com/shahzebqazi/cursor-agents/issues/9)).

## XP increments (issues)

| # | Story | Status |
|---|--------|--------|
| [#2](https://github.com/shahzebqazi/cursor-agents/issues/2) | Epic: categorized monorepo v2 | In progress |
| [#3](https://github.com/shahzebqazi/cursor-agents/issues/3) | XP workflow docs + PR template | Done in PR #1 |
| [#4](https://github.com/shahzebqazi/cursor-agents/issues/4) | `tooling/git-workspace-agent` | Done in PR #1 |
| [#5](https://github.com/shahzebqazi/cursor-agents/issues/5) | `meta/cursor-guide-agent` | Done in PR #1 |
| [#6](https://github.com/shahzebqazi/cursor-agents/issues/6) | `docs/employer/` | Done in PR #1 |
| [#7](https://github.com/shahzebqazi/cursor-agents/issues/7) | Migrate `platform/*` | Todo |
| [#8](https://github.com/shahzebqazi/cursor-agents/issues/8) | Migrate `products/*` | Todo |
| [#9](https://github.com/shahzebqazi/cursor-agents/issues/9) | Root README + `AGENTS.md` refresh | Partial |
| [#10](https://github.com/shahzebqazi/cursor-agents/issues/10) | Sync `my-cursor-config` routing | Todo (operator) |
| [#11](https://github.com/shahzebqazi/cursor-agents/issues/11) | GitHub Pages `/employer/` | Todo |

## Principles

1. **Cursor user first** — README and packages must work without private repos.
2. **Small PRs** — one story per merge when possible.
3. **Review before merge** — no direct commits that skip CI on `main`.
