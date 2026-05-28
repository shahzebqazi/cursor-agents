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
| DigitalOcean / doctl (read-first) | [`platform/digitalocean-agent`](../../platform/digitalocean-agent/) |
| Raspberry Pi SSH, systemd, headless agent | [`platform/pi-platform-agent`](../../platform/pi-platform-agent/) |
| macOS dev / prune Cursor chats | [`platform/macos-platform-agent`](../../platform/macos-platform-agent/) |
| Linux desktop / server patterns | [`platform/linux-platform-agent`](../../platform/linux-platform-agent/) |
| LAN MPD music control | [`music-streaming-agent`](../../music-streaming-agent/) |
| Music library ingest / Picard | [`music-library-agent`](../../music-library-agent/) |
| Mastodon posting from drafts | [`mastodon-agent`](../../mastodon-agent/) submodule + [`mastodon-agent-cursor`](../../mastodon-agent-cursor/) |
| Hiring / portfolio narrative | [`docs/employer/README.md`](../../docs/employer/README.md) |
| Monorepo contribution | [`CONTRIBUTING.md`](../../CONTRIBUTING.md) |

## Agent definition

See [`.cursor/agents/cursor-guide.md`](.cursor/agents/cursor-guide.md).
