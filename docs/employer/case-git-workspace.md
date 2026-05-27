# Case: Git workspace hygiene

## Problem

Multiple Cursor agents and humans sharing `~/Git` clones cause failed pulls, mixed branches, and accidental secret commits.

## Approach

- Public charter: [`tooling/git-workspace-agent`](../../tooling/git-workspace-agent/)
- Skill: `git-workspace-hygiene` — dirty-tree gate, ff-only pull, parallel branch naming
- Template layout YAML with placeholders (no operator inventory)

## Outcome

Operators and contributors get **deterministic sync rules** copyable into any homelab or team workspace without publishing private paths.

## Try it

```bash
# From cursor-agents clone
cat tooling/git-workspace-agent/.cursor/skills/git-workspace-hygiene/SKILL.md
```
