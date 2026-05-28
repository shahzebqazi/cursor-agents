#!/usr/bin/env bash
# Example: rsync a portable library tree into MPD's music_directory, chown for mpd, run mpc update.
# Copy to a private path or music-server repo and set variables for your layout — do not commit secrets.
#
# Required env:
#   SYNC_SOURCE   — absolute path to source tree (e.g. mounted portable player)
#   SYNC_DEST     — absolute path under MPD music_directory (e.g. /var/lib/mpd/music/imported)
# Optional:
#   SYNC_QUICK_SUBDIR — if set, only rsync "$SYNC_SOURCE/$SYNC_QUICK_SUBDIR/" (partial sync)
#   MPD_UPDATE_PATH   — path segment passed to `mpc update` (default: basename of SYNC_DEST)
#
# Usage (as root, typical on the MPD host):
#   sudo SYNC_SOURCE=/media/PLAYER SYNC_DEST=/var/lib/mpd/music/player ./sync-external-library-into-mpd.example.sh
set -euo pipefail

: "${SYNC_SOURCE:?}"
: "${SYNC_DEST:?}"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Run as root so files can be placed under MPD music_directory: sudo $0" >&2
  exit 1
fi

if [[ ! -d "$SYNC_SOURCE" ]]; then
  echo "Missing SYNC_SOURCE directory: $SYNC_SOURCE" >&2
  exit 1
fi

mkdir -p "$SYNC_DEST"

if [[ -n "${SYNC_QUICK_SUBDIR:-}" ]]; then
  echo "Partial sync: $SYNC_SOURCE/$SYNC_QUICK_SUBDIR/ -> $SYNC_DEST/$SYNC_QUICK_SUBDIR/"
  rsync -aH --delete --info=progress2 "$SYNC_SOURCE/$SYNC_QUICK_SUBDIR/" "$SYNC_DEST/$SYNC_QUICK_SUBDIR/"
else
  echo "Full sync: $SYNC_SOURCE/ -> $SYNC_DEST/"
  rsync -aH --info=progress2 "$SYNC_SOURCE/" "$SYNC_DEST/"
fi

chown -R mpd:audio "$SYNC_DEST"

RUNUSER="$(getent passwd 1000 | cut -d: -f1)"
[[ -n "$RUNUSER" ]] || RUNUSER="root"

rel="${MPD_UPDATE_PATH:-$(basename "$SYNC_DEST")}"
echo "Updating MPD database for path: $rel"
runuser -u "$RUNUSER" -- mpc update "$rel"
runuser -u "$RUNUSER" -- mpc status
