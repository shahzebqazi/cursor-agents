#!/usr/bin/env node
/**
 * One-shot local Cursor agent for scheduled home-agent runs.
 * Usage: invoke-cursor-agent.mjs <prompt-file> [cwd]
 *
 * Requires CURSOR_API_KEY (typically from ~/.env, sourced by home-agent-run.sh).
 * Install deps: npm install --prefix <pi-platform-agent-dir>
 */
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { Agent, CursorAgentError } from "@cursor/sdk";

const promptPath = process.argv[2];
const cwd = resolve(process.argv[3] || process.cwd());

if (!promptPath) {
  console.error("Usage: invoke-cursor-agent.mjs <prompt-file> [cwd]");
  process.exit(2);
}

const apiKey = process.env.CURSOR_API_KEY;
if (!apiKey) {
  console.error("CURSOR_API_KEY is not set");
  process.exit(1);
}

const modelId = process.env.CURSOR_AGENT_MODEL || "composer-2.5";
const prompt = readFileSync(promptPath, "utf8");

console.log(`invoke-cursor-agent: model=${modelId} cwd=${cwd}`);

try {
  const result = await Agent.prompt(prompt, {
    apiKey,
    model: { id: modelId },
    local: { cwd },
  });

  console.log(
    JSON.stringify(
      { status: result.status, id: result.id, hasResult: Boolean(result.result) },
      null,
      2,
    ),
  );
  if (result.result) {
    console.log("--- agent result ---");
    console.log(result.result);
  }
  process.exit(result.status === "error" ? 2 : 0);
} catch (err) {
  if (err instanceof CursorAgentError) {
    console.error(`CursorAgentError: ${err.message} retryable=${err.isRetryable}`);
    process.exit(1);
  }
  throw err;
}
