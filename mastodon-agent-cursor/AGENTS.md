# Agents — Mastodon (Cursor)

Cursor session index for **mastodon-agent**. Product behavior is defined in the submodule at **`mastodon-agent/docs/SPEC.md`** — not in this file.

## Hard rules

- **Never** commit `.env`, tokens, or secrets in either repo.
- **Product edits** go to **shahzebqazi/mastodon-agent**; this monorepo only gets submodule pointer bumps + Cursor glue.
- Preserve **`mastodon-agent/docs/images/hero.png`** unless the user requests new art.

## Default stance

When the user is vague (“continue”, “what’s next”):

1. Read **`mastodon-agent/docs/SPEC.md`** and pick the next phase-appropriate task.
2. Run `python3 -m compileall -q mastodon-agent/scripts` after Python changes.
3. State a one-paragraph plan before editing.

## Workstreams (from SPEC)

- Posting hardening (errors, dry-run, validation)
- Draft workflow (`drafts/` conventions)
- Docs/Pages alignment with SPEC
- Phase 3 features **only** with documented consent

## Paths

| Path | Role |
|------|------|
| `mastodon-agent/` | Git submodule — canonical product |
| `mastodon-agent-cursor/` | This Cursor charter |
| `.cursor/rules/mastodon-agent.mdc` | Repo-root rule for Cursor |
