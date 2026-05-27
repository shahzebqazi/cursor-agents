# Case: Music library ingest pipeline

## Problem

Batch-tag audio libraries with Picard/MusicBrainz while keeping quarantine and metadata rules explicit for agents.

## Approach

- Package: [`music-library-agent`](../../music-library-agent/)
- Skills: ingest pipeline, Picard batch, metadata read
- Shell helpers with clear inputs/outputs (no personal SSD paths in docs)

## Outcome

Shows **product-style agent work**: real media workflow, skills as the interface, scripts agents can invoke safely.

## Try it

```bash
cd music-library-agent
./scripts/read-audio-tags.sh --help 2>/dev/null || head -20 README.md
```
