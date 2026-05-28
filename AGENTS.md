# AGENTS.md — cursor-agents monorepo

Public [cursor-agents](https://github.com/shahzebqazi/cursor-agents): skills, MCP notes, charters, and small scripts.

## Scope

| In scope | Out of scope |
|----------|----------------|
| Skills, MCP notes, charters, small scripts | Operator inventory, tokens, hostnames |
| Product agents (music, Mastodon) | Private `my-cursor-config`, `my-droplets`, `my-pi-server` |
| Platform patterns (DO, Pi, macOS, Linux) | LinkedIn / job-search automation |
| UX mockups, brand codegen, design guide | **[mystic-ai](https://github.com/shahzebqazi/mystic-ai)** (sibling showcase) |

## Layout

| Category | Path |
|----------|------|
| Tooling | [`tooling/`](tooling/) |
| Meta | [`meta/`](meta/) |
| Platform | [`platform/`](platform/) |
| Products | [`products/`](products/) |

Roadmap: [`docs/MONOREPO_V2_ROADMAP.md`](docs/MONOREPO_V2_ROADMAP.md) · Moved paths: [`docs/RETIRED_PATHS.md`](docs/RETIRED_PATHS.md)

## Submodule (Mastodon)

Product code: **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** (`products/mastodon-agent/` submodule). Commit upstream, then bump the pointer. Cursor glue: `products/mastodon-agent-cursor/` only.

## Before you edit

1. Read the package `AGENTS.md`.
2. Never commit `.env`, keys, IPs, or personal clone paths.
3. One issue + one PR per story ([`CONTRIBUTING.md`](CONTRIBUTING.md)).

## Related

| Repo | Role |
|------|------|
| [mystic-ai](https://github.com/shahzebqazi/mystic-ai) | Design + UX showcase (mockups, brand pipeline) |
| [cursor-config](https://github.com/shahzebqazi/cursor-config) | Public workspace docs mirror |
| my-cursor-config (private) | Operator workspaces, Pi sync |

Reviewers: [`docs/employer/README.md`](docs/employer/README.md)
