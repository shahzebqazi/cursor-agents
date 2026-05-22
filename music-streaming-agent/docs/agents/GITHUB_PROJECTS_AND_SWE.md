# GitHub Projects + SWE (this repo)

**Repository:** `shahzebqazi/cursor-agents (music-streaming-agent/)`

Generic **Kanban + software-engineering** guidance (Issues, Projects, `gh` CLI, safety rules) lives in the public template repo:

- **[patterns/github-projects-and-swe.md](https://github.com/shahzebqazi/cursor-config/blob/main/patterns/github-projects-and-swe.md)** in **[shahzebqazi/cursor-config](https://github.com/shahzebqazi/cursor-config)**

## Music-agent–specific reminders

- **Branch flow:** `feature/*` → `dev` → `main` (see [`docs/README.md`](../README.md)).
- **Verify before merge:** run `ruff check src` when you use Ruff, and a manual `music-agent plan "status"` (or another harmless read) against a non-production MPD when behaviour changes.
- **Deploy coordination:** network, MPD layout, and colocated services are owned by your **music server** repository or private runbooks—keep secrets and deanonymizing details there (see [`docs/INTEGRATION.md`](../INTEGRATION.md)).
