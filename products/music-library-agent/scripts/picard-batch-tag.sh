#!/usr/bin/env bash
# Wrapper: Picard quarantine batch on Pi (my-pi-server-config picard branch).
set -euo pipefail

REMOTE="${PI_SERVER_REPO:-${HOME}/Git/my-pi-server-config}"
WRAPPER="${REMOTE}/scripts/picard/batch-tag-quarantine.sh"

if [[ -x "${WRAPPER}" ]]; then
  exec "${WRAPPER}" "$@"
fi

DRAGON_AGENT="/mnt/dragon/Git/dragon-agent/scripts/ingest/tag-batch.sh"
if [[ -x "${DRAGON_AGENT}" ]]; then
  exec "${DRAGON_AGENT}" "$@"
fi

echo "Missing Pi wrapper: ${WRAPPER}" >&2
echo "Checkout my-pi-server-config branch picard on the Pi." >&2
exit 1
