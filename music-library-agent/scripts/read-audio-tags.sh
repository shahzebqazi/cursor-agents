#!/usr/bin/env bash
# Print Picard-relevant tags for one audio file (ffprobe + python3).
set -euo pipefail

f="${1:?usage: read-audio-tags.sh FILE.flac}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
READ_TAGS="${DRAGON_READ_TAGS:-}"

for candidate in \
  "/mnt/dragon/Git/dragon-agent/scripts/lib/read-tags.sh" \
  "${HOME}/Git/dragon-agent/scripts/lib/read-tags.sh" \
  "${SCRIPT_DIR}/../../dragon-agent/scripts/lib/read-tags.sh"; do
  if [[ -f "${candidate}" ]]; then
    READ_TAGS="${candidate}"
    break
  fi
done

[[ -n "${READ_TAGS}" ]] || { echo "read-tags.sh not found" >&2; exit 1; }
# shellcheck source=/dev/null
source "${READ_TAGS}"

if dragon_read_tags "${f}"; then
  printf 'albumartist=%s\nartist=%s\ndate=%s\nalbum=%s\ntrack=%s\ntitle=%s\n' \
    "${DRAGON_TAG_ALBUMARTIST}" "${DRAGON_TAG_ARTIST}" "${DRAGON_TAG_DATE}" \
    "${DRAGON_TAG_ALBUM}" "${DRAGON_TAG_TRACK}" "${DRAGON_TAG_TITLE}"
else
  echo "No tags read from: ${f}" >&2
  exit 1
fi
