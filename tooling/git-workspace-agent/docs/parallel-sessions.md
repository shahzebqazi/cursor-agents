# Parallel agent sessions and branches

When multiple **automated agents** or **humans** work in separate sessions against the same clone (or different [git worktrees](https://git-scm.com/docs/git-worktree)), branch discipline reduces cross-talk.

## Rules

1. **At session start**, run `git branch --show-current` and treat that branch as this session’s branch until scope changes.
2. **Do not switch branches** mid-task unless explicitly asked.
3. **Prefer naming** so intent is obvious: `feature/<topic>-<short-id>` — one topic per branch per session when practical.
4. **Before commit or merge**, confirm `git branch --show-current` matches the intended branch.

Editor-agnostic: applies to Cursor, other IDEs, and headless automation equally.
