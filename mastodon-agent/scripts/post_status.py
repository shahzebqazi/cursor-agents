#!/usr/bin/env python3
"""Post UTF-8 text to Mastodon from a file.

Credentials load from a dotenv-style file (default: repo root ``.env``); see ``.env.example``.
No editor-specific tooling is required—run with ``python3`` from a shell or CI.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def instance_base(url: str) -> str:
    url = url.rstrip("/")
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}"
    return url


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Post a text file to Mastodon.")
    parser.add_argument(
        "file",
        type=Path,
        help="Path to post body (UTF-8), e.g. post.txt",
    )
    parser.add_argument(
        "--env",
        type=Path,
        default=root / ".env",
        help=f"Path to .env (default: {root / '.env'})",
    )
    parser.add_argument(
        "--visibility",
        default="public",
        choices=("public", "unlisted", "private", "direct"),
        help="Mastodon visibility (default: public)",
    )
    args = parser.parse_args()

    if not args.env.is_file():
        print(f"Missing {args.env} — copy .env.example and add credentials.", file=sys.stderr)
        return 1
    if not args.file.is_file():
        print(f"Not found: {args.file}", file=sys.stderr)
        return 1

    env = load_env(args.env)
    base = instance_base(env.get("MASTODON_INSTANCE_URL", ""))
    token = env.get("MASTODON_ACCESS_TOKEN", "")
    if not base or not token or token.startswith("your_"):
        print("Set MASTODON_INSTANCE_URL and MASTODON_ACCESS_TOKEN in .env", file=sys.stderr)
        return 1

    api_url = f"{base}/api/v1/statuses"
    status_text = args.file.read_text(encoding="utf-8")
    body = json.dumps(
        {"status": status_text, "visibility": args.visibility},
        ensure_ascii=False,
    ).encode("utf-8")

    req = urllib.request.Request(
        api_url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            out = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(e.read().decode()[:4000], file=sys.stderr)
        return 1

    print(out.get("url", out.get("id", "ok")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
