---
name: music-library-metadata-read
description: Read audio file tags with ffprobe for ingest planning without running Picard. Use when previewing integrate paths, validating quarantine files, or debugging tag fields before batch tagging.
---

# Read audio metadata (ffprobe)

## On Pi or Mac

```bash
bash /mnt/dragon/Git/dragon-agent/scripts/lib/read-tags.sh   # sourced by integrate.sh
# Or use the cursor-agents helper:
bash music-library-agent/scripts/read-audio-tags.sh /path/to/track.flac
```

Requires **ffprobe** and **python3**.

## Fields used for Picard layout

| Variable | Tags (first match) |
|----------|-------------------|
| album artist | `album_artist`, `albumartist` |
| artist | `artist` |
| date / year | `date`, `year`, `originaldate` |
| album | `album` |
| track | `track`, `tracknumber` |
| title | `title` |

## Integrate dry-run

`integrate.sh` calls `dragon_read_tags` automatically. Override for tests only:

```bash
DRAGON_TEST_ALBUMARTIST="..." DRAGON_TEST_ALBUM="..." \
  bash scripts/ingest/integrate.sh --dry-run --source /path
```

## When to use Picard instead

- Wrong or missing MusicBrainz IDs
- Soulseek mislabeled filenames
- VA / soundtrack routing

Use **music-library-picard-batch** skill.
