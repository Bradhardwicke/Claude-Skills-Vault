---
note-type: evaluation
status: trial-recommended
last-updated: 2026-06-08
---

# QMD — Semantic Search Evaluation

## What It Is

[tobi/qmd](https://github.com/tobi/qmd) — mini CLI search engine for markdown vaults. Built by Tobi Luetke (Shopify CEO). Combines BM25 full-text search, vector semantic search, and LLM re-ranking. Runs fully local via node-llama-cpp + GGUF models.

## Why It Matters for This Vault

Current session startup reads two index files (~5,000 tokens). QMD replaces that with a single semantic query returning only the relevant skill. For a 144-skill vault this is a significant token saving per session.

Community reports 60%+ token reduction for context retrieval (Kevin Lee, @ArtemXTech).

## Windows Compatibility

Confirmed compatible. Pre-compiled `sqlite-vec` binaries for `windows-x64` are included as optional dependencies.

## Installation

```bash
npm install -g @tobilu/qmd
```

Requires ~2GB disk space for GGUF models (auto-downloaded on first use).

## Obsidian Integration

There is a community plugin: [obsidian-qmd](https://github.com/achekulaev/obsidian-qmd) — local semantic search inside Obsidian using QMD.

There is also a Claude Code plugin: listed on claudepluginhub.com — would integrate directly into the skill invocation flow.

## How to Trial

1. Install: `npm install -g @tobilu/qmd`
2. Index the vault: `qmd index "D:\Claude Repo\Claude Skills Vault\Skills"`
3. Test a query: `qmd search "create a word document"` — should return `docx` skill
4. Compare token cost vs reading both index files

## Decision Criteria

Replace dual-index approach if:
- Query returns correct skill in top 3 results with ≥80% accuracy on 20 test queries
- Total token cost (query + result) is lower than ~5,000 tokens
- Latency is acceptable in a Cowork session context

## Related

- [[Skill Quick Reference]] — current primary lookup (~2,300 tokens)
- [[skills-lookup.yaml]] — current secondary lookup (~2,800 tokens)
- [[Project Context]] — vault design decisions
