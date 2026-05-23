---
name: music-library-ingest-pipeline
description: Run the Iconoclast music ingest pipeline on the Pi — mount check, quarantine scan, Picard tag batch, integrate dry-run/apply, MPD refresh. Use for Soulseek downloads, library sorting, or dragon SSD ingest tasks.
---

# Music library ingest pipeline

## Preconditions

```bash
findmnt /mnt/dragon
ls /mnt/dragon/iPod /mnt/dragon/Applications/Downloads 2>/dev/null | head
```

If dragon is not mounted, stop and escalate to **home-meta-agent** / operator (fstab `LABEL=dragon`).

## Repos on Pi

| Path | Repo |
|------|------|
| `/mnt/dragon/Git/dragon-agent` | dragon-agent (canonical) |
| `~/Git/my-pi-server-config` | pi-server — branch **`picard`** for Picard + MPD cutover |

## Steps (in order)

1. **Quarantine scan** (read-only inventory):

   ```bash
   bash /mnt/dragon/Git/dragon-agent/scripts/ingest/quarantine-scan.sh
   ```

2. **Tag** (Picard CLI — dry-run first):

   ```bash
   bash ~/Git/my-pi-server-config/scripts/picard/batch-tag-quarantine.sh --dry-run \
     --source /mnt/dragon/Applications/Downloads
   ```

   Apply per album or batch when confident:

   ```bash
   bash ~/Git/my-pi-server-config/scripts/picard/batch-tag-quarantine.sh --apply \
     --source "/mnt/dragon/Applications/Downloads/Downloads/<Album>"
   ```

3. **Integrate** (copy into `iPod/` layout — dry-run default):

   ```bash
   bash /mnt/dragon/Git/dragon-agent/scripts/ingest/integrate.sh --dry-run \
     --source /mnt/dragon/Applications/Downloads
   ```

   Only with operator approval:

   ```bash
   bash /mnt/dragon/Git/dragon-agent/scripts/ingest/integrate.sh --apply \
     --source /mnt/dragon/Applications/Downloads
   ```

4. **MPD refresh**:

   ```bash
   bash /mnt/dragon/Git/dragon-agent/scripts/ingest/mpd-refresh.sh
   ```

## MPD library cutover (once)

If `mpc stats` shows zero songs but `/mnt/dragon/iPod` is populated:

```bash
sudo bash ~/Git/my-pi-server-config/scripts/mpd-cutover-to-dragon.sh
```

See **my-pi-server-config** `docs/MPD_DRAGON_LIBRARY.md`.

## Do not

- Copy quarantine → `iPod/` without tagging (except explicit test env vars).
- Delete or retag immutable trees (`My CDs/`, `My Digital Purchases/`).
- Commit `.env` or Soulseek credentials.
