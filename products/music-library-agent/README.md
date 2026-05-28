# music-library-agent

Cursor skills and scripts for **music library ingest**: quarantine, Picard CLI tagging, Picard path layout, metadata read, and MPD refresh.

**Product repos (not in this package):**

| Repo | Role |
|------|------|
| [dragon-agent](https://github.com/shahzebqazi/dragon-agent) | Ingest scripts on dragon SSD (`/mnt/dragon/Git/dragon-agent`) |
| [my-pi-server-config](https://github.com/shahzebqazi/my-pi-server-config) | Pi branch `picard`: MPD cutover, Picard install, batch wrapper |
| [music-streaming-agent](../music-streaming-agent/) | Optional HTTP MPD bot |

## Skills

| Skill | Use when |
|-------|----------|
| [`music-library-ingest-pipeline`](.cursor/skills/music-library-ingest-pipeline/SKILL.md) | End-to-end Soulseek → quarantine → tag → integrate → MPD |
| [`music-library-picard-batch`](.cursor/skills/music-library-picard-batch/SKILL.md) | Picard CLI batch tagging on Pi |
| [`music-library-metadata-read`](.cursor/skills/music-library-metadata-read/SKILL.md) | ffprobe tag read without Picard |

## Scripts

| Script | Purpose |
|--------|---------|
| [`scripts/picard-batch-tag.sh`](scripts/picard-batch-tag.sh) | Thin wrapper → pi-server `batch-tag-quarantine.sh` |
| [`scripts/read-audio-tags.sh`](scripts/read-audio-tags.sh) | ffprobe → shell vars (for integrate dry-runs) |

Paths are **examples**; fill host alias (`pi-server`) from **my-cursor-config**.
