#!/usr/bin/env python3
"""Export and remove archived Cursor chats older than N days.

macOS default DB: ~/Library/Application Support/Cursor/User/globalStorage/state.vscdb
Linux: ~/.config/Cursor/User/globalStorage/state.vscdb
"""

from __future__ import annotations

import argparse
import json
import platform
import re
import shutil
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

USER_QUERY_RE = re.compile(r"<user_query>\s*(.*?)\s*</user_query>", re.DOTALL)
ACTION_PATTERNS = [
    re.compile(r"(?i)\b(?:TODO|FIXME|operator|pending|follow[- ]?up|next step)\b"),
    re.compile(r"(?i)\b(?:you should|need to|must|merge PR|run `)\b"),
]


def default_cursor_db() -> Path:
    home = Path.home()
    if platform.system() == "Darwin":
        return home / "Library/Application Support/Cursor/User/globalStorage/state.vscdb"
    return home / ".config/Cursor/User/globalStorage/state.vscdb"


def default_projects() -> Path:
    return Path.home() / ".cursor/projects"


def default_export_dir() -> Path:
    return Path.home() / "AiChats/CURSOR_TODO/archived"


def ms_timestamp(raw: int | None) -> int:
    if not raw:
        return 0
    return raw // 1000 if raw > 1_000_000_000_000 else raw


def load_headers(db_path: Path) -> list[dict]:
    conn = sqlite3.connect(db_path)
    row = conn.execute(
        "SELECT value FROM ItemTable WHERE key='composer.composerHeaders'"
    ).fetchone()
    conn.close()
    if not row:
        return []
    return json.loads(row[0]).get("allComposers", [])


def workspace_path(composer: dict) -> str:
    wi = composer.get("workspaceIdentifier") or {}
    uri = wi.get("uri") or {}
    return str(uri.get("fsPath") or uri.get("path") or wi.get("id") or "unknown")


def workspace_id(composer: dict) -> str:
    return str((composer.get("workspaceIdentifier") or {}).get("id") or "")


def is_stale(composer: dict, days: int, now_s: int) -> bool:
    if not composer.get("isArchived"):
        return False
    ts = ms_timestamp(composer.get("lastUpdatedAt") or composer.get("createdAt"))
    if not ts:
        return False
    age_days = (now_s - ts) / 86400
    return age_days >= days


def slugify(name: str, cid: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (name or "untitled").strip()).strip("-").lower()[:60]
    return f"{s}-{cid[:8]}" if s else cid[:8]


def project_slug(workspace: str) -> str:
    home = str(Path.home())
    if workspace == home:
        return "Users-" + Path.home().name
    rel = workspace.replace(home + "/", "").replace("/", "-")
    return f"Users-{Path.home().name}-" + rel.replace(" ", "-")


def find_transcript(projects: Path, cid: str, workspace: str) -> Path | None:
    for slug in (project_slug(workspace), f"Users-{Path.home().name}"):
        p = projects / slug / "agent-transcripts" / cid / f"{cid}.jsonl"
        if p.is_file():
            return p
    return None


def parse_transcript(path: Path) -> tuple[list[str], str]:
    queries: list[str] = []
    last_a = ""
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        role = row.get("role")
        texts = [
            b.get("text", "")
            for b in row.get("message", {}).get("content", [])
            if isinstance(b, dict) and b.get("type") == "text"
        ]
        blob = "\n".join(texts)
        if role == "user":
            for m in USER_QUERY_RE.finditer(blob):
                q = m.group(1).strip()
                if q:
                    queries.append(q)
            if not queries and blob.strip():
                queries.append(blob.strip()[:2000])
        elif role == "assistant" and blob.strip():
            last_a = blob
    return queries, re.sub(r"\s+", " ", last_a)[:2000]


def action_items(name: str, subtitle: str, queries: list[str], excerpt: str) -> list[str]:
    items: list[str] = []
    for line in "\n".join([name, subtitle] + queries + [excerpt]).splitlines():
        line = line.strip(" -*•\t")
        if len(line) < 12:
            continue
        if any(p.search(line) for p in ACTION_PATTERNS) and line not in items:
            items.append(line[:400])
    return items[:12]


def export_chat(
    composer: dict,
    projects: Path,
    export_dir: Path,
    days: int,
) -> Path:
    cid = composer["composerId"]
    name = (composer.get("name") or "untitled").strip()
    subtitle = (composer.get("subtitle") or "").strip()
    workspace = workspace_path(composer)
    ts = ms_timestamp(composer.get("lastUpdatedAt") or composer.get("createdAt"))
    when = (
        datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        if ts
        else "unknown"
    )
    tpath = find_transcript(projects, cid, workspace)
    if tpath:
        queries, excerpt = parse_transcript(tpath)
        source = str(tpath)
    else:
        queries, excerpt = [], subtitle
        source = "metadata-only"
    actions = action_items(name, subtitle, queries, excerpt)
    fname = slugify(name, cid) + ".md"
    lines = [
        f"# {name}",
        "",
        f"- **Chat ID:** `{cid}`",
        f"- **Archived:** yes",
        f"- **Retention:** >= {days} days since last activity",
        f"- **Workspace:** `{workspace}`",
        f"- **When:** {when}",
        f"- **Source:** {source}",
        "",
    ]
    if subtitle:
        lines += ["## Subtitle", "", subtitle, ""]
    if queries:
        lines += ["## User asks", ""]
        for i, q in enumerate(queries[:8], 1):
            lines.append(f"### Ask {i}\n\n{q}\n")
    if excerpt:
        lines += ["## Summary", "", excerpt, ""]
    lines += ["## Review / TODO", ""]
    if actions:
        for a in actions:
            lines.append(f"- [ ] {a}")
    else:
        lines.append("- [ ] _(skim summary — nothing auto-flagged)_")
    lines.append("")
    out = export_dir / fname
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def backup_db(db_path: Path, backup_dir: Path) -> Path:
    backup_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = backup_dir / f"state.vscdb.{stamp}"
    shutil.copy2(db_path, dest)
    return dest


def prune(db_path: Path, composer_ids: set[str], projects: Path, dry_run: bool) -> tuple[int, int]:
    conn = sqlite3.connect(db_path)
    raw = json.loads(
        conn.execute(
            "SELECT value FROM ItemTable WHERE key='composer.composerHeaders'"
        ).fetchone()[0]
    )
    composers = raw.get("allComposers", [])
    before = len(composers)
    kept = [c for c in composers if c.get("composerId") not in composer_ids]
    removed = before - len(kept)
    if not dry_run:
        raw["allComposers"] = kept
        conn.execute(
            "UPDATE ItemTable SET value=? WHERE key='composer.composerHeaders'",
            (json.dumps(raw),),
        )
        for cid in composer_ids:
            conn.execute("DELETE FROM cursorDiskKV WHERE key=?", (f"composerData:{cid}",))
        conn.commit()
    conn.close()

    transcripts = 0
    for cid in composer_ids:
        for base in projects.glob("*/agent-transcripts"):
            tdir = base / cid
            if tdir.is_dir():
                if not dry_run:
                    shutil.rmtree(tdir)
                transcripts += 1
    return removed, transcripts


def update_index(export_dir: Path, exported: list[tuple[str, str]]) -> None:
    parent = export_dir.parent
    index = parent / "ARCHIVED_INDEX.md"
    rows = "\n".join(
        f"| [{f}](archived/{f}) | {title} |"
        for f, title in sorted(exported, key=lambda x: x[1].lower())
    )
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = (
        f"\n## Cleared {stamp}\n\n"
        f"**{len(exported)}** chat(s) exported to `archived/` and removed from Cursor.\n\n"
        f"| File | Title |\n|------|-------|\n{rows}\n"
    )
    if index.is_file():
        index.write_text(index.read_text(encoding="utf-8") + block, encoding="utf-8")
    else:
        index.write_text(
            f"# Archived chats (exported)\n{block}",
            encoding="utf-8",
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export and delete archived Cursor chats older than N days.",
    )
    parser.add_argument(
        "--days",
        type=int,
        choices=[7, 30],
        default=30,
        help="Only chats archived with last activity at least this many days ago (default: 30)",
    )
    parser.add_argument("--db", type=Path, default=None)
    parser.add_argument("--projects", type=Path, default=None)
    parser.add_argument("--export-dir", type=Path, default=None)
    parser.add_argument("--workspace-path", help="Limit to one workspace fsPath (e.g. /Users/you)")
    parser.add_argument("--workspace-id", help="Limit to workspace storage id")
    parser.add_argument("--limit", type=int, default=0, help="Max chats per run (0 = no limit)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--export-only", action="store_true", help="Export markdown only; do not prune")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--backup-dir", type=Path, default=None)
    args = parser.parse_args()

    db_path = args.db or default_cursor_db()
    projects = args.projects or default_projects()
    export_dir = args.export_dir or default_export_dir()

    if not db_path.is_file():
        print(f"Cursor DB not found: {db_path}", file=sys.stderr)
        return 1

    now_s = int(time.time())
    headers = load_headers(db_path)
    selected = [c for c in headers if is_stale(c, args.days, now_s)]
    if args.workspace_path:
        selected = [c for c in selected if workspace_path(c) == args.workspace_path]
    if args.workspace_id:
        selected = [c for c in selected if workspace_id(c) == args.workspace_id]
    selected.sort(key=lambda c: c.get("lastUpdatedAt") or c.get("createdAt") or 0)
    if args.limit:
        selected = selected[: args.limit]

    if not selected:
        print(f"No archived chats older than {args.days} day(s) matched.")
        return 0

    print(f"Matched {len(selected)} chat(s) (>= {args.days} days old, archived).")
    if args.dry_run:
        for c in selected:
            print(f"  {c['composerId'][:8]}  {workspace_path(c)}  {(c.get('name') or '')[:50]}")
        print(f"Would export to {export_dir}")
        if not args.export_only:
            print("Would prune from Cursor DB + agent-transcripts")
        return 0

    export_dir.mkdir(parents=True, exist_ok=True)
    exported: list[tuple[str, str]] = []
    ids: set[str] = set()
    for c in selected:
        out = export_chat(c, projects, export_dir, args.days)
        exported.append((out.name, (c.get("name") or "untitled").strip()))
        ids.add(c["composerId"])

    update_index(export_dir, exported)
    print(f"Exported {len(exported)} -> {export_dir}")

    if args.export_only:
        return 0

    backup_dir = args.backup_dir or (Path(__file__).resolve().parent / ".backups")
    if not args.no_backup:
        dest = backup_db(db_path, backup_dir)
        print(f"DB backup -> {dest}")

    for attempt in range(8):
        try:
            removed, transcripts = prune(db_path, ids, projects, dry_run=False)
            print(f"Pruned {removed} composer(s), {transcripts} transcript dir(s)")
            break
        except sqlite3.OperationalError as e:
            if "locked" not in str(e).lower() or attempt == 7:
                raise
            print(f"DB locked, retry {attempt + 1}/8...", file=sys.stderr)
            time.sleep(8)
    else:
        return 1

    print("Reload Cursor window if the Archived list looks stale.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
