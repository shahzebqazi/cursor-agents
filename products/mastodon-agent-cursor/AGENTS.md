# Agents — Mastodon (Cursor)

Cursor index for **mastodon-agent**. Product authority: **`products/mastodon-agent/docs/SPEC.md`**.

## Hard rules

- Never commit `.env`, tokens, or secrets.
- Product edits → **shahzebqazi/mastodon-agent**; this repo gets submodule bumps + Cursor glue only.
- Preserve **`products/mastodon-agent/docs/images/hero.png`** unless asked to replace.

## Default stance

1. Read SPEC; pick the next phase-appropriate task.
2. `python3 -m compileall -q products/mastodon-agent/scripts` after Python changes.
3. One-paragraph plan before editing.

## Paths

| Path | Role |
|------|------|
| `products/mastodon-agent/` | Submodule (canonical product) |
| `products/mastodon-agent-cursor/` | This charter |
| `.cursor/rules/mastodon-agent.mdc` | Repo-root Cursor rule |
