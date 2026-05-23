# Agents

This package lives under **[cursor-agents](https://github.com/shahzebqazi/cursor-agents)** at `music-streaming-agent/`.

## Read order (server-side agent)

1. This file
2. [`docs/agents/SERVER_SIDE_AGENT.md`](docs/agents/SERVER_SIDE_AGENT.md)
3. [`docs/agents/AGENT_SPEC.md`](docs/agents/AGENT_SPEC.md)
4. [`docs/agents/REVIEW_MERGE_GATES.md`](docs/agents/REVIEW_MERGE_GATES.md)

## Docs map

| Doc | Audience |
|-----|----------|
| [`docs/README.md`](docs/README.md), [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Humans — install, integration |
| [`docs/agents/`](docs/agents/) | Agents — policy, merge gates, persona |
| [`docs/ai/CURSOR_MUSIC_BOT.md`](docs/ai/CURSOR_MUSIC_BOT.md) | Paste-ready IDE prompt for `music-agent` |
| [`.cursor/rules/`](.cursor/rules/) | Thin Cursor pointers into `docs/agents/` |

Optional private workspace handoff: **[cursor-config](https://github.com/shahzebqazi/cursor-config)** (`docs/WORKSPACE_AGENTS.md`, `patterns/`). Not required to build or run.

When using GitHub Issues + Projects, one in-flight issue per agent session keeps parallel work legible.
