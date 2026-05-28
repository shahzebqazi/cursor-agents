# Cursor layer — mastodon-agent

**Cursor-only.** Product code: **[mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** submodule at [`../mastodon-agent/`](../mastodon-agent/).

## Open in Cursor

Clone **cursor-agents** and open the repo root. Rules: [`.cursor/rules/mastodon-agent.mdc`](../../.cursor/rules/mastodon-agent.mdc).

## Read first

1. [`../mastodon-agent/docs/SPEC.md`](../mastodon-agent/docs/SPEC.md)
2. [`../mastodon-agent/README.md`](../mastodon-agent/README.md)
3. [`AGENTS.md`](AGENTS.md)

## Submodule bump

```bash
cd products/mastodon-agent && git fetch && git checkout main && git pull
cd ../.. && git add products/mastodon-agent && git commit -m "Bump mastodon-agent submodule"
```

Commit product changes upstream first — do not fork scripts only in this monorepo copy.
