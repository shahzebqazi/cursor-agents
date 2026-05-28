# Review, test, and merge gates (agents)

Mandatory workflow for **feature work** that ends in a **pull request** into `dev`. Read together with root [`AGENTS.md`](../../AGENTS.md) § Parallel Cursor agents.

## Roles

| Role | Responsibility |
|------|----------------|
| **Agent** | Implement, run tests, **self-review the PR** after gates below, re-test after self-review, drive merge hygiene, ask the user to close the chat after merge when back on `dev`. |
| **Human** | **Code review** (read diff, design, safety) **before** the agent’s formal PR self-review. **Do not** run hands-on / exploratory **testing** until the agent has **finished its own test pass** at least once on the branch. |

## Ordered gates (do not skip or reorder)

1. **Agent: first test pass**  
   Run the project’s automated checks and any scripted or documented manual verification the agent can perform without the human (tests, lint, smoke scripts, `curl` against a local server, etc.). Fix failures before asking the human for anything.

2. **Human: code review**  
   The human reviews **the code** (diff, approach, obvious risks). This is **not** a substitute for step 1.  
   **Block:** The agent **must not** perform its formal **PR self-review** (step 3) until the human has confirmed they have completed this code review (or explicitly waived it in chat).

3. **Agent: PR self-review**  
   After human code review, the agent reviews its **own PR**: description vs actual diff, risk notes, test coverage called out, merge checklist, and whether anything still violates [`AGENT_SPEC.md`](AGENT_SPEC.md) / [`CORE_FEATURES.md`](../CORE_FEATURES.md). Update the PR or branch as needed.

4. **Agent: second test pass**  
   Re-run the same (or stricter) test plan after any fixes from self-review. Treat regressions as merge blockers.

5. **Merge and delete branch**  
   When steps 1–4 are green, merge **`feature/*` → `dev`** (per [`docs/README.md`](../README.md) § Branches). Then **delete the feature branch** (remote and local) so stale names do not accumulate.

## Human testing timing

- **No** human-driven testing **before** the agent’s **first** test pass (step 1) completes successfully.  
- After merge, optional human smoke on `dev` is encouraged for high-risk changes; the agent should still have satisfied steps 1 and 4 on the feature branch before merge.

## After merge (agent on `dev`)

1. `git checkout dev && git pull` (or equivalent) so the session matches integrated `dev`.  
2. **Ask the user explicitly** to **close this chat** (session) now that the branch is merged and you are on `dev` again—avoids stale branch context in long threads.  
3. You **may** invite the user to: pick **backlog** items, dictate **new features**, or file **bugs** for the next `feature/…` branch.

## Tone

Keep prompts to the human short and precise; default stance matches [`SOUL.md`](SOUL.md).
