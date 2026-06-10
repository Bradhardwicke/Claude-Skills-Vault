# Claude Skills Vault

> **Agents Read, Humans Write.**
> A token-efficient skill reference system so Claude can identify and invoke the right skill for any task.

---

## What This Is

Claude has access to hundreds of skills — specialised tools for writing documents, analysing data, running SQL, managing projects, building agents, and more. The problem is discovery: how does Claude know which skill to reach for, without pre-loading every skill definition into every conversation?

This vault solves that problem. It is Claude's reference brain — authored by humans, optimised for Claude to read quickly at conversation start. It is not a general-purpose personal knowledge base. Every note in this vault exists to help Claude do its job better.

---

## The Problem It Addresses

Pre-loading all 128+ skills into every Claude conversation costs thousands of tokens before the first useful word is written. It also creates ambiguity — when everything is loaded, nothing is prioritised.

Most community patterns for AI-assisted PKM follow the rule: **human thinking goes in the vault, Claude outputs go in `~/.claude/`**. This vault consciously inverts that pattern. Skill definitions are the primary content here. Claude's session memory, working plans, and task outputs live elsewhere.

---

## How It Works

The vault uses a three-tier lookup system to minimise token cost whilst keeping all skills discoverable.

| Tier | What Claude reads | Token cost |
|------|-------------------|------------|
| 1 | Top 25 skills hardcoded in `CLAUDE.md` | Free (already in context) |
| 2 | `Index/skills-lookup.yaml` — compact intent-to-skill-id map | ~2,800 tokens |
| 3 | Individual skill notes in `Skills/` | On demand only |

At session start, Claude checks Tier 1 first. If the required skill is in the Top 25, it invokes it immediately. If not, it reads the compact YAML index. Only when a skill is actually invoked does Claude read the full skill note. Total lookup cost across all three tiers: approximately 5,000 tokens.

### Skill Notes

Each skill note has two frontmatter blocks — Obsidian metadata followed by the verbatim `SKILL.md` content from the plugin:

```yaml
---
# Obsidian frontmatter
name: data-analyze
skill-id: "data:analyze"
plugin: Data
category: Data
tags: [skill, data, analysis]
aliases: [Data Analysis, Analyze Data]
triggers:
  - data question
  - metric lookup
  - what drove
  - analytics report
---

---
# SKILL.md frontmatter (copied verbatim from plugin)
name: analyze
description: Answer data questions...
---

# Full SKILL.md content follows...
```

The `triggers` field is the single source of truth. The build script reads every trigger across every skill note and generates both index files automatically.

---

## Vault Structure

```
Claude Skills Vault/
├── Skills/                     # 128 skill notes across 12 categories
│   ├── Documents/              # docx, xlsx, pptx, pdf, view-pdf
│   ├── Data/                   # 10 data:* skills
│   ├── Design/                 # 7 design:* skills
│   ├── Operations/             # 9 operations:* skills
│   ├── Sales/                  # 9 sales:* skills
│   ├── Productivity/           # 4 productivity:* skills
│   ├── Obsidian/               # 5 obsidian:* skills
│   ├── Superpowers/            # 14 advanced dev workflow skills
│   ├── PM Skills/              # 8 project management skills
│   ├── Executive Mentor/       # 6 executive decision skills
│   ├── Finance/                # 3 finance skills
│   ├── Markdown HTML/          # 11 markdown-to-HTML skills
│   └── Engineering/            # 15 engineering and tooling skills
├── Index/
│   ├── skills-lookup.yaml      # AUTO-GENERATED — compact intent index
│   ├── Skill Quick Reference.md# AUTO-GENERATED — curated intent guide
│   ├── Skills Index.md         # Human-readable map of categories
│   └── Skills Database.base    # Obsidian Base view (for human use)
├── _scripts/
│   └── build_skill_brain.py    # Regenerates both index files from skill notes
├── .claude/commands/           # /preserve, /compress, /resume commands
├── CLAUDE.md                   # Session memory and Top 25 skill list
├── Project Context.md          # Design decisions and project history
└── Welcome.md                  # Vault overview
```

---

## Skill Categories

| Category | Skills | Purpose |
|----------|--------|---------|
| Documents | 5 | Word, Excel, PowerPoint, PDF creation and manipulation |
| Data | 10 | SQL, analysis, visualisation, dashboards, statistical testing |
| Design | 7 | UX copy, critique, accessibility, user research |
| Operations | 9 | Process docs, status reports, runbooks, risk assessment |
| Sales | 9 | Research, outreach, call prep, competitive intel, forecasting |
| Productivity | 4 | Task management, memory systems, working context |
| Obsidian | 5 | Vault interaction, markdown, bases, CLI, JSON canvas |
| Superpowers | 14 | Advanced dev workflows: brainstorming, TDD, debugging, code review |
| PM Skills | 8 | Project management, Jira, Confluence, scrum, communications |
| Executive Mentor | 6 | Board prep, stress testing, decisions, postmortems |
| Finance | 3 | Financial analysis, valuation, SaaS metrics |
| Engineering | 15 | Workflows, skill creation, MCP building, debugging tooling |

---

## Current Status

**128 skills documented.** All have full `SKILL.md` content and `triggers` frontmatter. The Index contains 1,105 intent triggers across all skills.

### Recently Added Categories

The following six categories were added in the most recent build session, bringing the vault from 71 to 128 documented skills:

| Category | Skills Added |
|----------|-------------|
| Superpowers | 14 — brainstorming, writing-plans, executing-plans, TDD, debugging, code review, subagent-dev, git-worktrees, and more |
| PM Skills | 8 — senior-pm, scrum-master, meeting-analyzer, jira-expert, confluence-expert, atlassian-admin, atlassian-templates, team-comms |
| Executive Mentor | 6 — executive-mentor, board-prep, challenge, hard-call, postmortem, stress-test |
| Finance | 3 — financial-analyst, saas-metrics-coach, finance-skills |
| Markdown HTML | 11 — markdown-html-orchestrator, md-document, md-review, md-slides, design-system, and command variants |
| Engineering | 15 — workflow-builder, write-a-skill, caveman, slopmop and sub-commands, mcp-builder, ai-agents-architect, and more |

### Skills Still to Add (Optional)

| Skill | Notes |
|-------|-------|
| `helm-chart-builder` | Engineering category |
| `frontend-design` | Claude API plugin variant |
| `webapp-testing` | Claude API plugin variant |
| `slack-gif-creator` | Claude API plugin variant |
| `2slides-ppt-generator` | Claude API plugin variant |

### Known Issue: Index Regeneration

The `build_skill_brain.py` script was updated with all new TRIGGERS and INTENT_GROUPS entries covering all 128 skills, but the Write tool silently truncates large files on the Windows filesystem mount. The script currently contains only its file header (18 lines).

**Fix:** Write the full script via bash heredoc in chunks, then run it to regenerate both index files. The full script content is documented in the session transcript.

Both `skills-lookup.yaml` and `Skill Quick Reference.md` currently reflect only the original 71 skills until the script is rebuilt and run.

---

## Adding a New Skill

1. Create a note in the appropriate `Skills/` subfolder.
2. Add Obsidian frontmatter with `skill-id`, `plugin`, `category`, `tags`, `aliases`, and `triggers`.
3. Paste the full `SKILL.md` content below (including its own frontmatter block from the plugin).
4. Run the build script from the vault root:

```bash
python "_scripts/build_skill_brain.py"
```

The script is idempotent — it skips notes already processed and regenerates both index files from scratch on every run.

---

## Design Principles

**Agents Read, Humans Write.** The dominant community pattern is: human thinking goes in the vault, Claude outputs go in `~/.claude/`. This vault inverts that pattern. It is Claude's reference brain. Skill definitions are the primary content, not personal notes or session memory.

**Single source of truth.** Triggers live in frontmatter only. The build script reads them to generate all lookup files. Adding a skill means editing one note, then running one script.

**Lazy loading.** Claude reads the minimum it needs. Top 25 are free. The YAML index is compact. Full skill notes load only on invocation.

**Boundary rule.** Session memory, working plans, task outputs, and Claude-generated content belong in `~/.claude/` or Cowork's memory system — not in this vault.

---

## Future Direction

### QMD Semantic Search

The current dual-index approach costs approximately 5,000 tokens per session. QMD (`npm install -g @tobilu/qmd`) could replace this with a single semantic query returning only the relevant skill. Windows-compatible. Trial recommended before committing.

### Custom Slash Command

A `/skills` command (`D:\Claude Repo\Claude Skills Vault\.claude\commands\skills.md`) provides a structured alternative in the meantime — loading the right index file on demand instead of pre-loading both.

---

## Repository

**Local vault path:** `D:\Claude Repo\Claude Skills Vault`

**MCP integrations:**
- Obsidian CLI — enabled
- Desktop Commander — active, used for file read/write on this vault

---

*Last updated: 7 June 2026 | 128 skills | 12 categories | 1,105 triggers*
