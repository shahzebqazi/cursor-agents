"""CLI entry: `music-agent serve` or `music-agent plan \"...\"` (dry plan, still snapshots MPD)."""

from __future__ import annotations

import argparse
import json
import sys

from .calculus import legal
from .executor import execute
from .mpc_client import SubprocessMpc
from .personas import render
from .pipeline import parse_plan


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="music-agent")
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("serve", help="LAN HTTP chat (stdlib)")
    ps.add_argument("--host", default="127.0.0.1")
    ps.add_argument("--port", type=int, default=8765)

    pp = sub.add_parser("plan", help="Print JSON plan + legality for a message (contacts MPD for fluents)")
    pp.add_argument("message")
    pp.add_argument("--device-id", default=None)
    pp.add_argument("--tone", default="formal")
    pp.add_argument("--execute", action="store_true", help="Also run effects after planning")

    args = p.parse_args(argv)

    if args.cmd == "serve":
        from .server import ChatHandler, ThreadingHTTPServer

        httpd = ThreadingHTTPServer((args.host, args.port), ChatHandler)
        print(f"music-agent listening on http://{args.host}:{args.port}/chat", file=sys.stderr)
        httpd.serve_forever()
        return 0

    mpc = SubprocessMpc()
    situation = mpc.snapshot()
    plan = parse_plan(args.message, situation, args.device_id)
    out: dict[str, object] = {
        "notes": plan.notes,
        "effects": [{"op": e.op, "arg": e.arg, "arg2": e.arg2} for e in plan.effects],
        "legal": [{e.op: legal(e, situation)[0]} for e in plan.effects],
    }
    if args.execute and plan.effects:
        results = []
        for e in plan.effects:
            ok, reason = legal(e, situation)
            if not ok:
                print(json.dumps({"error": reason, "effect": e.op}, indent=2))
                return 2
            results.append(execute(mpc, e))
            situation = mpc.snapshot()
        out["results"] = results
        out["reply"] = render(args.tone, "\n".join(f"- {e.op}: {r}" for e, r in zip(plan.effects, results, strict=True)))
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
