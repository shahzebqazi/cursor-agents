# Cursor layer — mastodon-agent

This directory is **Cursor-only**. The product (scripts, spec, Pages art) lives in the **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** submodule at [`../mastodon-agent/`](../mastodon-agent/).

## Open in Cursor

Clone **cursor-agents** and open the **repository root**. Rules under [`.cursor/rules/mastodon-agent.mdc`](../.cursor/rules/mastodon-agent.mdc) apply when you work on Mastodon tasks.

## Read first

1. **[`mastodon-agent/docs/SPEC.md`](../mastodon-agent/docs/SPEC.md)** — tool-agnostic product authority
2. **[`mastodon-agent/README.md`](../mastodon-agent/README.md)** — runtime quick start
3. **[`AGENTS.md`](AGENTS.md)** — Cursor session charter (this folder)

## Submodule updates

After merging changes in **shahzebqazi/mastodon-agent**, bump the submodule pointer in this monorepo:

```bash
cd mastodon-agent && git fetch && git checkout main && git pull
cd .. && git add mastodon-agent && git commit -m "Bump mastodon-agent submodule"
```

Do **not** edit product files only in the monorepo copy—commit upstream in **mastodon-agent**, then bump the pointer.
