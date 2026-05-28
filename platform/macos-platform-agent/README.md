# macos-platform-agent (Cursor)

Public **macOS** dev patterns for Cursor: shell, Homebrew, window managers, editor integration, and **chat hygiene**.

## Public vs private

| Public (here) | Private |
|---------------|---------|
| AeroSpace / Leader Key *patterns* | **dotfiles** / **my-dotfiles** |
| Homebrew workflow skills | **my-mac-config** bootstrap + satellites |
| **clear-archived-cursor-chats** skill | **my-cursor-config** `macbook/cursor-meta-agent/` git journal |
| MCP notes for local shell | **my-cursor-config** `macbook/` |

## Skills

| Skill | Purpose |
|-------|---------|
| [`clear-archived-cursor-chats`](.cursor/skills/clear-archived-cursor-chats/SKILL.md) | Export + prune archived chats **≥ 7 or 30 days** old |

## Scripts

| Script | Purpose |
|--------|---------|
| [`scripts/clear-archived-cursor-chats.py`](scripts/clear-archived-cursor-chats.py) | Implements the skill (dry-run, export-only, prune) |

```bash
python3 scripts/clear-archived-cursor-chats.py --days 30 --dry-run
```
