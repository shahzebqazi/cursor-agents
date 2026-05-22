# Migration checklist (repos and clones)

Use this when splitting or renaming remotes after moving generic docs into **[cursor-config](https://github.com/shahzebqazi/cursor-config)** or personal material into **`my-cursor-config`** (private).

## Local clones

- [ ] **`cursor-music-streaming-agent`**: `git remote -v` → expect `git@github.com:shahzebqazi/cursor-agents (music-streaming-agent/).git` (or HTTPS equivalent). Do **not** rename this GitHub repository without an explicit decision; local folder names may differ (`~/Code/cursor-music-streaming-agent`, worktrees, etc.).
- [ ] **`cursor-config`**: add or refresh `origin` → `shahzebqazi/cursor-config`. Pull `main` to pick up `patterns/` used by this repo’s docs.
- [ ] **Music server repo**: ensure it documents how it pins this package (submodule SHA, subtree, or copy path) per [INTEGRATION.md](INTEGRATION.md).
- [ ] **`my-cursor-config` (private)**: if you removed operator-specific scripts from the public tree, restore them here (or in the music server repo) from git history before the cleanup commit.

## Docs and bookmarks

- [ ] Replace any old links to `docs/agents/GITHUB_PROJECTS_AND_SWE.md` **full prose** bookmarks: the file still exists but defers generic sections to [cursor-config patterns](https://github.com/shahzebqazi/cursor-config/tree/main/patterns).
- [ ] If you used `scripts/sync-ipod-to-mpd.sh`, it was **removed** as operator-specific; recover from git history if needed, or adapt [`scripts/examples/sync-external-library-into-mpd.example.sh`](../scripts/examples/sync-external-library-into-mpd.example.sh) in a private repo.

## Ansible / inventory

- [ ] Copy `ansible/inventory.example.yml` → a private `inventory.yml` (or `host_vars/`) with real `ansible_host` and `ansible_user`.
- [ ] Set `music_agent_mpd_host` via `-e` or vault to match working `mpc` on the box.

## Verification

- [ ] From a clean machine: clone only **public** repos listed in the music server README + this repo; follow [docs/README.md](README.md) and confirm you can run `music-agent plan "status"` against a test MPD using **placeholder-style** examples (no private URLs required).
