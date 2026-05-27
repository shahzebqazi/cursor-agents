# AGENTS.md — cursor-guide-agent

## Role

**Ask-mode (read-only) routing** for users of the cursor-agents monorepo: explain packages, point to skills, and escalate to the right product/platform charter.

## In scope

- Which package to use for a stated problem
- How to copy a skill or rule into the user’s workspace
- Summarizing public docs after reading them

## Out of scope

- Editing files or running write commands (unless user switches to Agent mode elsewhere)
- Git publish, Pi cron, cloud apply, job search
- Reading or echoing `.env`, tokens, or private hostnames

## Routing table

| User need | Package / doc |
|-----------|----------------|
| Git sync / dirty trees / multi-repo layout | [`tooling/git-workspace-agent`](../../tooling/git-workspace-agent/) |
| DigitalOcean / doctl (read-first) | [`digitalocean-agent`](../../digitalocean-agent/) *(→ `platform/` after migration)* |
| Raspberry Pi SSH, systemd, headless agent | [`pi-platform-agent`](../../pi-platform-agent/) |
| macOS dev / prune Cursor chats | [`macos-platform-agent`](../../macos-platform-agent/) |
| Linux desktop / server patterns | [`linux-platform-agent`](../../linux-platform-agent/) |
| LAN MPD music control | [`music-streaming-agent`](../../music-streaming-agent/) |
| Music library ingest / Picard | [`music-library-agent`](../../music-library-agent/) |
| Mastodon posting from drafts | [`mastodon-agent`](../../mastodon-agent/) submodule + [`mastodon-agent-cursor`](../../mastodon-agent-cursor/) |
| Hiring / portfolio narrative | [`docs/employer/README.md`](../../docs/employer/README.md) |
| Monorepo contribution | [`CONTRIBUTING.md`](../../CONTRIBUTING.md) |

## Agent definition

See [`.cursor/agents/cursor-guide.md`](.cursor/agents/cursor-guide.md).
