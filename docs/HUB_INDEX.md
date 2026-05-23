# Agent hub index

**cursor-agents** holds **Cursor-specific integration** for public agent products. Product code and tool-agnostic specs may live in **standalone repos** linked by submodule.

## Packages in this monorepo

| Package | Directory | Canonical product | Deploy target |
|---------|-----------|-------------------|---------------|
| Music / MPD | [`music-streaming-agent/`](../music-streaming-agent/) | (in-tree) | Pi LAN (`music-agent`, optional Ansible) |
| Mastodon | [`mastodon-agent/`](../mastodon-agent/) submodule | **[shahzebqazi/mastodon-agent](https://github.com/shahzebqazi/mastodon-agent)** | Any host with `.env` |
| Mastodon (Cursor) | [`mastodon-agent-cursor/`](../mastodon-agent-cursor/) | — | Cursor session charter only |

## Not in this repo (by design)

| Need | Use instead |
|------|-------------|
| Private workspace handoff (`~/Git` on Pi) | **[cursor-config](https://github.com/shahzebqazi/cursor-config)** — `docs/WORKSPACE_AGENTS.md` |
| Mac satellites (AeroSpace, Leader Key, dotfiles, …) | **[my-mac-config](https://github.com/shahzebqazi/my-mac-config)** |
| Mastodon product spec (editor-neutral) | **`mastodon-agent/docs/SPEC.md`** in submodule |

## Migrated standalone repos

| Former GitHub name | New location |
|--------------------|--------------|
| `cursor-music-streaming-agent` | `music-streaming-agent/` |
| `mastodon-cursor-agent` | **mastodon-agent** repo + submodule here |

Local archives (if any): `~/archive/*-2026-05-23.tar.gz` on the Mac.
