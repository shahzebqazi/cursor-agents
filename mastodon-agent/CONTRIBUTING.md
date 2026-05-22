# Contributing

Thanks for helping improve **mastodon-agent** inside **[cursor-agents](https://github.com/shahzebqazi/cursor-agents)**.

## Prerequisites

- **Python 3.8+** (stdlib only for `scripts/post_status.py`).
- **UTF-8** drafts; the script reads files as UTF-8 and sends JSON with `ensure_ascii=False`.

## Environment variables

Copy `.env.example` to `.env` (never commit `.env`):

| Variable | Meaning |
|----------|---------|
| `MASTODON_INSTANCE_URL` | Server base URL only, e.g. `https://example.social` |
| `MASTODON_ACCESS_TOKEN` | OAuth access token (treat like a password) |

Optional: `--env /path/to/.env`

## Verify locally

```bash
python3 -m compileall -q scripts
python3 scripts/post_status.py path/to/draft.txt --visibility unlisted  # needs real .env
```

## Optional Cursor configuration

Personal automation belongs in private **[cursor-config](https://github.com/shahzebqazi/cursor-config)**. Public builds must not depend on it.

## Pull requests

Open PRs against **[shahzebqazi/cursor-agents](https://github.com/shahzebqazi/cursor-agents)** with changes under `mastodon-agent/`. Keep PRs focused; never commit secrets.
