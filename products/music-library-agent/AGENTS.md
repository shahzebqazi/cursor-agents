# music-library-agent

Charter for **library ingest and metadata** on the Iconoclast Pi + dragon SSD. Playback bots live in **music-streaming-agent**; Pi nginx/Ampache deploy in **my-pi-server-config**.

## Read order

1. This file
2. [`README.md`](README.md)
3. Skills under [`.cursor/skills/`](.cursor/skills/)

## Canonical paths (Pi)

| Tier | Path |
|------|------|
| Library | `/mnt/dragon/iPod` |
| Quarantine | `/mnt/dragon/Applications/Downloads` |
| Picard profile | `/mnt/dragon/Applications/Picard` |
| dragon-agent git | `/mnt/dragon/Git/dragon-agent` |

## Safety

- **Dry-run default** for integrate and Picard batch previews.
- Never Soulseek → `iPod/` without quarantine + tag.
- No secrets in git.
