#!/usr/bin/env bash
# Load or append a stored MPD playlist by name.
# Usage:
#   MPD_HOST='pw@host' ./queue_playlist_by_name.sh <playlist-name>
#   MPD_HOST='pw@host' ./queue_playlist_by_name.sh <playlist-name> --append
set -euo pipefail

: "${MPD_HOST:?Set MPD_HOST (e.g. password@your-mpd-host)}"

name="${1:?playlist name}"
mode="${2:-}"

if [[ "$mode" == "--append" ]]; then
  while IFS= read -r track; do
    [[ -z "$track" ]] && continue
    mpc add "$track"
  done < <(mpc playlist "$name")
else
  mpc clear
  mpc load "$name"
fi

mpc play
mpc status
