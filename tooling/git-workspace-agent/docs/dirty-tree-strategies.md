# Dirty tree strategies

When `git status` is not clean (including **untracked** files that block your sync policy), automated agents must **not** pull or push blindly.

| Strategy | Command pattern | When |
|----------|-----------------|------|
| **Stash** | `git stash push -u -m "git-workspace: …"` then `git pull --ff-only` | Keep WIP, resume after pull |
| **WIP branch** | `git checkout -b wip/agent-YYYYMMDD-topic` | Publish in-progress work safely |
| **Skip** | Log repo + branch + status; exit 0 | Operator must resolve manually |
| **Reset** | `git fetch origin && git reset --hard origin/<branch>` | **Operator approval only** |
| **Commit** | Doc-only, allowlisted extensions | Operator explicitly asked |

## Agent behavior

1. Always run `git status -sb` first.
2. If dirty, pick a strategy from the table or ask the operator — do not guess `reset`.
3. Never combine stash and reset in one automated run without confirmation.
