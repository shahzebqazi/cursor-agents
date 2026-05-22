<div align="center">

# mastodon-agent

**Compose and ship Mastodon posts from the terminal—without leaking secrets into chat or version control.**

*Fediverse · Plain UTF-8 files · `.env` for credentials*

![AI-generated hero: a robotic, mummified Mastodon rampaging — same art as the GitHub Pages site](docs/images/hero.png)

Part of **[cursor-agents](https://github.com/shahzebqazi/cursor-agents)** · [GitHub Pages mini-site](https://shahzebqazi.github.io/cursor-agents/docs/mastodon/)

</div>

---

## Why this exists

Drafts in a file, review in git, credentials in `.env`, and a small script you or automation can run—**not** copy-pasting tokens into prompts.

---

## What you get

| Piece | What it does |
|--------|----------------|
| **`scripts/post_status.py`** | Posts a UTF-8 text file via the Mastodon API (`/api/v1/statuses`). |
| **`.env.example`** | Safe template—copy to `.env` locally. **Never commit `.env`.** |
| **`docs/`** | GitHub Pages mini-site (hero art preserved under the monorepo). |

---

## Quick start

From this directory (`cursor-agents/mastodon-agent/`):

1. **Python 3.8+** on your PATH as `python3`.
2. On your Mastodon server: **Preferences → Development → New application** with **`write:statuses`**.
3. `cp .env.example .env` — set `MASTODON_INSTANCE_URL` (server base only, e.g. `https://example.social`) and `MASTODON_ACCESS_TOKEN`.
4. Write a UTF-8 post file.
5. `python3 scripts/post_status.py path/to/your_post.txt`

```text
python3 scripts/post_status.py post.txt --visibility unlisted
python3 scripts/post_status.py post.txt --env /path/to/.env
```

---

## Security

- **Never commit** `.env`, tokens, or unpublished sensitive drafts to public remotes.
- Optional personal Cursor rules live in private **[cursor-config](https://github.com/shahzebqazi/cursor-config)** — not required to post.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contributor notes.

---

## License

MIT — see [`LICENSE`](LICENSE).
