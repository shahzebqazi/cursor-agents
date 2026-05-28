<div align="center">

<p align="center">
  <img src="docs/assets/hero.svg" alt="cursor-agents" width="100%" />
</p>

# cursor-agents

### Public Cursor agent toolkit — skills, MCP notes, charters, runnable packages

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Monorepo](https://img.shields.io/badge/layout-monorepo-89b4fa.svg)](#layout)

**Shipped agent workflows** for git multi-repo hygiene, DigitalOcean read-first ops, Pi/headless patterns, LAN music control, and Mastodon drafting — organized for Cursor and other coding agents.

> **Not in this repo:** machine hostnames, API tokens, or personal infra paths. Employer-safe overview: [`docs/employer/ARCHITECTURE.md`](docs/employer/ARCHITECTURE.md).

[Start here](#start-here-by-problem) · [Layout](#layout) · [Clone](#clone) · [Related](#related-repos)

</div>

---

## How it works

```
┌─────────────────────────────────────────────────────────────┐
│  meta/          cursor-guide-agent — route tasks to package │
├─────────────────────────────────────────────────────────────┤
│  tooling/       git-workspace-agent — sync, dirty trees     │
├─────────────────────────────────────────────────────────────┤
│  platform/      doctl, Pi, macOS Cursor maintenance         │
├─────────────────────────────────────────────────────────────┤
│  products/      MPD, Picard, Mastodon-from-git              │
└─────────────────────────────────────────────────────────────┘
         Each package: AGENTS.md + skills + optional scripts
```

Packages are **problem-first**: open the row that matches your task, not a deep directory tree.

---

## Start here (by problem)

| I want to… | Package |
|------------|---------|
| Fix git sync / dirty trees / multi-repo layout | [`tooling/git-workspace-agent/`](tooling/git-workspace-agent/) |
| Find which package owns my task | [`meta/cursor-guide-agent/`](meta/cursor-guide-agent/) |
| Use `doctl` read-first on DigitalOcean | [`platform/digitalocean-agent/`](platform/digitalocean-agent/) |
| Run headless agent patterns on a Pi | [`platform/pi-platform-agent/`](platform/pi-platform-agent/) |
| Prune archived Cursor chats on macOS | [`platform/macos-platform-agent/`](platform/macos-platform-agent/) |
| Control LAN MPD / music streaming | [`products/music-streaming-agent/`](products/music-streaming-agent/) |
| Batch-tag a music library (Picard) | [`products/music-library-agent/`](products/music-library-agent/) |
| Post Mastodon drafts from git | [`products/mastodon-agent/`](products/mastodon-agent/) |

Full index: [`docs/HUB_INDEX.md`](docs/HUB_INDEX.md) · Platform matrix: [`docs/PLATFORM_AGENTS.md`](docs/PLATFORM_AGENTS.md)

---

## Layout

| Category | Path |
|----------|------|
| Tooling | [`tooling/`](tooling/) |
| Meta | [`meta/`](meta/) |
| Platform | [`platform/`](platform/) |
| Products | [`products/`](products/) |

Roadmap: [`docs/MONOREPO_V2_ROADMAP.md`](docs/MONOREPO_V2_ROADMAP.md) · Contribute: [`CONTRIBUTING.md`](CONTRIBUTING.md) · Charter: [`AGENTS.md`](AGENTS.md)

---

## Clone

```bash
git clone --recurse-submodules https://github.com/shahzebqazi/cursor-agents.git
cd cursor-agents
```

Docs site: [shahzebqazi.github.io/cursor-agents/](https://shahzebqazi.github.io/cursor-agents/)

---

## For reviewers

Hiring-manager summary: [`docs/employer/README.md`](docs/employer/README.md)

---

## Related repos

| Repo | Role |
|------|------|
| [mystic-ai](https://github.com/shahzebqazi/mystic-ai) | Design showcase — brand pipeline, UX mockups |
| [mhn-ai-agent-memory](https://github.com/shahzebqazi/mhn-ai-agent-memory) | Hopfield research memory + MCP |
| [sqazi.sh](https://sqazi.sh) | Portfolio CV |

---

## License

MIT — see [LICENSE](LICENSE).
