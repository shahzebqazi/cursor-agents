"""Minimal LAN HTTP chat (stdlib only): POST /chat JSON {message, device_id?, tone?}."""

from __future__ import annotations

import json
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from .calculus import legal
from .executor import execute
from .mpc_client import SubprocessMpc
from .personas import render
from .pipeline import parse_plan


class ChatHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    mpc_factory: type[SubprocessMpc] = SubprocessMpc

    def _json(self, code: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in {"/", "/health"}:
            self._json(200, {"ok": True, "service": "cursor-music-streaming-agent"})
            return
        if parsed.path == "/chat":
            html = """<!doctype html><meta charset=utf-8><title>music-agent</title>
<style>body{font-family:system-ui;max-width:42rem;margin:2rem auto}textarea,input{width:100%}</style>
<h1>LAN chat (v0)</h1>
<p>Formal tone default. Commands route locally (no LLM on device).</p>
<label>Message<br><textarea id=m rows=4>status</textarea></label>
<p><label>Device id (optional, for volume memory)<br><input id=d></label></p>
<p><button type=button id=b>Send</button> <span id=s></span></p>
<pre id=o></pre>
<script>
const $ = (id) => document.getElementById(id);
$('b').onclick = async () => {
  $('s').textContent = '…';
  const r = await fetch('/chat', {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({message: $('m').value, device_id: $('d').value || null, tone: 'formal'})});
  const j = await r.json();
  $('o').textContent = JSON.stringify(j, null, 2);
  $('s').textContent = r.ok ? 'ok' : ('err '+r.status);
};
</script>"""
            data = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(data)
            return
        self._json(404, {"error": "not_found"})

    def do_POST(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/chat":
            self._json(404, {"error": "not_found"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length > 0 else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self._json(400, {"error": "invalid_json"})
            return
        message = str(payload.get("message", ""))
        device_id = payload.get("device_id")
        tone = str(payload.get("tone") or "formal")

        mpc = self.mpc_factory()
        situation = mpc.snapshot()
        plan = parse_plan(message, situation, device_id if isinstance(device_id, str) else None)
        if not plan.effects:
            body = "\n".join(plan.notes) if plan.notes else "No operation."
            self._json(200, {"reply": render(tone, body), "effects": [], "results": []})
            return

        for e in plan.effects:
            ok, reason = legal(e, situation)
            if not ok:
                self._json(400, {"error": "illegal_effect", "reason": reason, "effect": e.op})
                return

        results: list[str] = []
        for e in plan.effects:
            results.append(execute(mpc, e))
            situation = mpc.snapshot()

        summary = "\n".join(f"- {e.op}: {r}" for e, r in zip(plan.effects, results, strict=True))
        self._json(
            200,
            {
                "reply": render(tone, summary),
                "effects": [{"op": e.op, "arg": e.arg, "arg2": e.arg2} for e in plan.effects],
                "results": results,
            },
        )

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        # minimal observability: stderr only, quiet by default
        return


def serve(host: str, port: int) -> None:
    httpd = ThreadingHTTPServer((host, port), ChatHandler)
    httpd.serve_forever()
