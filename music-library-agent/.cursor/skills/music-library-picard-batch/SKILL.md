---
name: music-library-picard-batch
description: Install and run MusicBrainz Picard CLI batch tagging on the Iconoclast Pi for quarantine audio. Use when tagging Soulseek downloads, fixing metadata before integrate, or configuring Picard -e FROM_FILE workflows.
---

# Picard CLI batch tagging (Pi)

## Install (once, sudo)

```bash
cd ~/Git/my-pi-server-config && git checkout picard
sudo bash scripts/install-picard.sh
```

## Config on dragon

- Profile dir: `/mnt/dragon/Applications/Picard`
- Naming script must match **dragon-agent** `scripts/lib/path-builder.sh` / `file-naming-script.txt`

## Dry-run

```bash
bash scripts/picard/batch-tag-quarantine.sh --dry-run \
  --source /mnt/dragon/Applications/Downloads
```

## Apply (tags in place under quarantine)

```bash
bash scripts/picard/batch-tag-quarantine.sh --apply \
  --source "/mnt/dragon/Applications/Downloads/Downloads/<release-folder>"
```

Uses **standalone** Picard (`-s`) and [`quarantine.commands.txt`](https://github.com/shahzebqazi/my-pi-server-config/blob/picard/scripts/picard/quarantine.commands.txt): CLUSTER → LOOKUP_CLUSTERED → SAVE_MATCHED → SCAN → QUIT.

## Headless Pi

If Picard exits immediately without processing, the host may need a display or `xvfb-run` — check journal / Picard logs before retrying. Do not loop blindly.

## After tagging

Run **music-library-ingest-pipeline** integrate + `mpd-refresh.sh`.

## Reference

- [Picard executable commands](https://picard-docs.musicbrainz.org/en/usage/exec_commands.html)
- [Command and batch processing](https://picard-docs.musicbrainz.org/en/usage/command_processing.html)
