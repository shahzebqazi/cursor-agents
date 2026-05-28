# AI-facing documentation

Put **prompts, evaluation rubrics, tool-use recipes, and other model-oriented text** here (versioned with the repo).

**Editor-agnostic workflow habits** (Kanban, parallel sessions) and optional **Cursor rules** live in **my-cursor-config** under `patterns/` and `.cursor/rules/`. Link or vendor those files if you want the same guidance in this clone; they are not dependencies of the Python package.

**Private** experimental hooks, credentials, or unpublished-library workflows belong in **`my-cursor-config`** (private) or the music server’s private docs—not in this public tree.

Orchestration index for any AI working in this repo: **[`AGENTS.md`](../../AGENTS.md)** (package root).

**Operator prompt:** [`CURSOR_MUSIC_BOT.md`](CURSOR_MUSIC_BOT.md) — paste into Cursor rules or a custom agent when driving LAN `music-agent` / `mpc`.
