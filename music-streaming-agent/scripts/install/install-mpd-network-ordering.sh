#!/usr/bin/env bash
# Install systemd drop-in so mpd starts after network-online (avoids bind-to-LAN-IP races).
set -euo pipefail
if [[ "$(id -u)" -ne 0 ]]; then
  echo "Run: sudo $0" >&2
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(git -C "$script_dir" rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "${repo_root}" ]]; then
  repo_root="$(cd "$script_dir/../.." && pwd)"
fi
conf_src="${repo_root}/scripts/install/systemd/mpd.service.d/wait-for-network.conf"
if [[ ! -f "$conf_src" ]]; then
  echo "Missing drop-in template: $conf_src" >&2
  exit 1
fi

echo "==> Installing drop-in under /etc/systemd/system/mpd.service.d/"
install -d /etc/systemd/system/mpd.service.d
install -m 0644 "$conf_src" \
  /etc/systemd/system/mpd.service.d/wait-for-network.conf

echo "==> systemctl daemon-reload"
systemctl daemon-reload

# mpd.service uses Type=notify: plain "systemctl restart mpd" blocks until MPD sends READY.
# With a huge music_directory on slow media, that can take many minutes and looks hung.
echo "==> Restarting mpd (non-blocking; then we poll for active or failed)…"
systemctl restart --no-block mpd.service

deadline=$((SECONDS + 720))
last_echo="$SECONDS"
while (( SECONDS < deadline )); do
  if systemctl is-active --quiet mpd.service 2>/dev/null; then
    echo "==> mpd is active."
    systemctl status mpd.service --no-pager -l || true
    exit 0
  fi
  if systemctl is-failed --quiet mpd.service 2>/dev/null; then
    echo "==> mpd failed to start. Recent logs:" >&2
    journalctl -u mpd.service -n 40 --no-pager >&2
    exit 1
  fi
  if (( SECONDS - last_echo >= 15 )); then
    echo "… still waiting for mpd (large library scan can take a long time) …"
    last_echo=$SECONDS
  fi
  sleep 1
done

echo "==> Timed out after 12m waiting for mpd to become active." >&2
journalctl -u mpd.service -n 40 --no-pager >&2
exit 1
