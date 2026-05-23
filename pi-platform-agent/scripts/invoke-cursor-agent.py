#!/usr/bin/env python3
"""One-shot local Cursor agent (Python SDK). See invoke-cursor-agent.mjs for Node variant."""
from __future__ import annotations

import os
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: invoke-cursor-agent.py <prompt-file> [cwd]", file=sys.stderr)
        return 2

    prompt_path = Path(sys.argv[1])
    cwd = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path.cwd()

    api_key = os.environ.get("CURSOR_API_KEY")
    if not api_key:
        print("CURSOR_API_KEY is not set", file=sys.stderr)
        return 1

    from cursor_sdk import Agent, AgentOptions, LocalAgentOptions

    model = os.environ.get("CURSOR_AGENT_MODEL", "composer-2.5")
    prompt = prompt_path.read_text(encoding="utf-8")

    print(f"invoke-cursor-agent: model={model} cwd={cwd}")

    result = Agent.prompt(
        prompt,
        AgentOptions(
            api_key=api_key,
            model=model,
            local=LocalAgentOptions(cwd=str(cwd)),
        ),
    )

    print({"status": result.status, "id": result.id, "has_result": bool(result.result)})
    if result.result:
        print("--- agent result ---")
        print(result.result)

    return 2 if result.status == "error" else 0


if __name__ == "__main__":
    raise SystemExit(main())
