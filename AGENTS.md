# AGENTS.md — cursor-agents monorepo

You are working in the **public** [cursor-agents](https://github.com/shahzebqazi/cursor-agents) repository.

## Scope

| In scope | Out of scope |
|----------|----------------|
| Skills, MCP notes, charters, small scripts in this repo | Operator inventory, tokens, hostnames |
| Product agents (music, Mastodon) | Private `my-cursor-config`, `my-droplets`, `my-pi-server` |
| Platform patterns (DO, Pi, macOS, Linux) | LinkedIn / job-search automation |

## Layout (v2 in progress)

| Category | Path | Role |
|----------|------|------|
| Tooling | [`tooling/`](tooling/) | Git workspace hygiene, shared dev patterns |
| Meta | [`meta/`](meta/) | Ask-mode guides and routing |
| Platform | [`platform/`](platform/) *(migration pending)* | Cloud/OS agent patterns — see also legacy top-level dirs |
| Products | [`products/`](products/) *(migration pending)* | End-user workflows — see also legacy top-level dirs |

Roadmap: [`docs/MONOREPO_V2_ROADMAP.md`](docs/MONOREPO_V2_ROADMAP.md) · Kanban: [Project #16](https://github.com/users/shahzebqazi/projects/16)

## Submodule policy (Mastodon)

- **Product code** lives in **[shahzebqazi/mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** (`mastodon-agent/` submodule).
- Commit product changes **upstream**, then bump the submodule pointer here.
- Cursor glue only in `mastodon-agent-cursor/` — do not duplicate scripts in the monorepo tree.

## Before you edit

1. Read the **package** `AGENTS.md` for the directory you are changing.
2. Never commit `.env`, keys, IPs, or personal clone paths.
3. Prefer one issue + one PR per story ([`CONTRIBUTING.md`](CONTRIBUTING.md)).

## Related repos

| Repo | Role |
|------|------|
| [cursor-config](https://github.com/shahzebqazi/cursor-config) | Public workspace docs mirror |
| my-cursor-config (private) | Operator workspaces, Pi sync, publish policy |

Reviewer narrative: [`docs/employer/README.md`](docs/employer/README.md)
