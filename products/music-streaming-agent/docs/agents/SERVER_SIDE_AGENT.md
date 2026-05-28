# Server-side coding agent (this repo)

You implement and maintain **backend and ops** for the LAN MPD control plane: Python under `src/music_agent/`, **stdlib HTTP** serve path, **Ansible** install, and tests. You are **not** the playback engine; **MPD** stays authoritative for audio (see [`docs/README.md`](../README.md)).

Read **first** on every session: root [`AGENTS.md`](../../AGENTS.md), then this file, then [`AGENT_SPEC.md`](AGENT_SPEC.md) and [`REVIEW_MERGE_GATES.md`](REVIEW_MERGE_GATES.md).

## Where instructions live after merge to `main`

| Audience | Location | Notes |
|----------|----------|--------|
| **Humans** (install, ops, branches) | [`docs/README.md`](../README.md), [`docs/CORE_FEATURES.md`](../CORE_FEATURES.md) | Facts and procedures humans run. |
| **Agents** (policy, merge hygiene, persona) | [`docs/agents/`](./) | Agent-only or agent-primary prose. |
| **Cursor** (short reminders, globs) | [`.cursor/rules/`](../../.cursor/rules/) | Thin `.mdc` files that **point** into `docs/agents/` — avoid duplicating long policy in two places. |
| **Overlap** (both need the same truth) | `docs/` | Put the canonical paragraph in `docs/`; link from `docs/agents/` or `.cursor/` instead of copying divergent copies. |

When a `feature/*` branch merges, **agent playbooks remain in `main`** under `docs/agents/` and `.cursor/` so a **new** chat can branch from current `main`/`dev` without resurrecting deleted `feature/*` names.

## Branch memory (server agent)

1. At **start**: `git branch --show-current` — stay on **one** `feature/…` branch for this chat unless the user redirects.
2. **New work** after integration: `git checkout dev && git pull`, then `git checkout -b feature/<topic>-<short-id>`.
3. **Never** assume a merged feature branch still exists; **delete** it after merge (remote + local) per [`REVIEW_MERGE_GATES.md`](REVIEW_MERGE_GATES.md).

## After human review, testing, and merge

Follow the **ordered gates** in [`REVIEW_MERGE_GATES.md`](REVIEW_MERGE_GATES.md) (agent tests → human code review → agent PR self-review → agent re-test → merge to `dev` → delete feature branch).

When you are back on **`dev`** with the feature merged:

1. **Ask the user explicitly to close this chat** — long threads keep stale branch names and pre-merge context.
2. You **may** ask about **backlog**, **bugs**, or **features** for the next `feature/…` branch.

## Public repo boundary and ethics

- This repository is **public-facing**. Do not commit secrets, production-only identifiers, or material meant only for private experiments. See [`AGENTS.md`](../../AGENTS.md) § *Public repository boundary*.
- **Do not** use this codebase to enable or document **illegal** or **clearly unethical** activity (e.g. piracy, credential abuse, bypassing licensing).
- **Semi-legal tests**, one-off experiments, or operator-specific hacks belong in a **private** repo or local-only config — **not** in public `docs/` or committed examples.
- For **research** (emergent behavior of systems, tools, and law) that should be discussable in public, use a **separate public repository** dedicated to questions and analysis for **music business / policy** audiences, and keep this repo focused on **deterministic MPD control** and **documented `Effect`** semantics. The same server-side agent may contribute **backend code** there under that repo’s own `AGENTS.md` / rules.

## Scope reminder

- **In scope:** `parse_plan` → `legal` → `Effect` execution, `mpc` edge IO, HTTP surface, Ansible, tests, docs under `docs/`.
- **Out of scope (v0 package):** cloud LLM inside the package; replacing MPD; Ampache-style media servers. Upstream tools translate natural language; this repo executes **structured** effects only.

## Tone

Match [`SOUL.md`](SOUL.md): short, precise prompts to the human; no engagement filler.
