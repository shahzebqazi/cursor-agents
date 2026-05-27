# Contributing — cursor-agents

We ship the **monorepo v2** layout using **XP-style increments**: small PRs, working `main`, review before merge.

## Kanban

**[Project #16 — cursor-agents — monorepo v2](https://github.com/users/shahzebqazi/projects/16)**

Pick or create an issue before starting work. Move cards **Todo → In progress → Done** when you merge.

## Branch naming

| Prefix | Use |
|--------|-----|
| `feature/` | User-visible package or docs |
| `fix/` | Bug or broken links |
| `chore/` | CI, housekeeping |

One issue per PR when possible. Example: `feature/epic-01-scaffold-tooling-meta-employer`.

## Pull requests

- Target **`main`** only (no force-push to `main`).
- Link issue: `Fixes #N` or `Refs #N`.
- Keep PRs reviewable (**&lt; ~400 lines** diff when practical).
- CI must pass (Mastodon submodule compile, music-streaming smoke).
- Request review; address feedback in the same branch.

## What belongs here

| In this repo | Not here |
|--------------|----------|
| Skills, MCP notes, public charters | Tokens, hostnames, personal clone trees |
| Runnable agent packages | `my-cursor-config`, `my-droplets`, `my-pi-server` internals |

See [`docs/employer/ARCHITECTURE.md`](docs/employer/ARCHITECTURE.md) for the public/private boundary.

## Local check

```bash
git submodule update --init --recursive
pip install -e ./music-streaming-agent && music-agent plan --help
python3 -m compileall -q mastodon-agent/scripts
```
