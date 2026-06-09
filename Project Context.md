---
note-type: project-context
status: active
last-updated: 2026-06-07
---

# Claude Skills Vault — Project Context

## Purpose

This Obsidian vault is Claude's "skill brain" — a fast, token-efficient reference system so Claude can identify and invoke the right skill for any task. It is not for human navigation; it is optimised for Claude to read quickly at conversation start.

## What Has Been Built

### Vault structure

```
Claude Skills Vault/
├── Skills/              ← 71 skill notes (one per available skill)
│   ├── Documents/       ← docx, xlsx, pptx, pdf, view-pdf
│   ├── Data/            ← 10 data:* skills
│   ├── Design/          ← 7 design:* skills
│   ├── Operations/      ← 9 operations:* skills
│   ├── Sales/           ← 9 sales:* skills
│   ├── Productivity/    ← 4 productivity:* skills
│   ├── Obsidian/        ← defuddle, json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown
│   ├── Plugin Management/
│   ├── Engineering/
│   └── ... (other categories)
├── Index/
│   ├── Skills Index.md          ← human-readable MOC by plugin category
│   ├── Skills Database.base     ← Obsidian Base view (for human use in Obsidian UI)
│   ├── skills-lookup.yaml       ← AUTO-GENERATED — compact intent→skill-id lookup (~2,800 tokens)
│   └── Skill Quick Reference.md ← CURATED — intent-grouped guide with Top 20 + disambiguation (~2,300 tokens)
├── _scripts/
│   └── build_skill_brain.py     ← regenerates skills-lookup.yaml and Skill Quick Reference.md
├── Skill Brain Demo.html        ← animated neural network presentation (open in browser)
└── Project Context.md           ← this file
```

### Each skill note structure

Every note has two frontmatter blocks:

```yaml
---
# Obsidian frontmatter (Claude reads this for lookup)
name: data-analyze
skill-id: "data:analyze"
plugin: Data
category: Data
tags: [skill, data, analysis]
aliases: [Data Analysis, Analyze Data]
triggers:
  - data question
  - data analysis
  - metric lookup
  - what drove
  - analytics report
---

---
# SKILL.md frontmatter (copied verbatim from plugin)
name: analyze
description: Answer data questions...
argument-hint: "<question>"
---

# Full SKILL.md content follows...
```

The `triggers` field is the key addition — intent-focused phrases Claude matches against user language to identify the right skill.

### Key design decisions

- **Triggers in frontmatter** — single source of truth; script reads them to generate the YAML
- **Two lookup files** — `skills-lookup.yaml` is the compact machine-readable index; `Skill Quick Reference.md` is the curated intent guide with disambiguation notes
- **Short IDs for Obsidian skills** — `defuddle`, `json-canvas`, `obsidian-bases`, `obsidian-cli`, `obsidian-markdown` (no `obsidian:` prefix)
- **Auto-generation** — adding a new skill note with `triggers` in frontmatter + running the script is all that is needed to update both index files

## Current State

**128 skills documented.** All have full SKILL.md content and `triggers` frontmatter. The pending list from before is now complete.

### New folders added this session

| Folder | Skills |
|---|---|
| `Skills/Superpowers/` | 14 skills — brainstorming, writing-plans, executing-plans, test-driven-development, systematic-debugging, requesting-code-review, receiving-code-review, subagent-driven-development, finishing-a-development-branch, using-git-worktrees, verification-before-completion, writing-skills, dispatching-parallel-agents, using-superpowers |
| `Skills/PM Skills/` | 8 skills — senior-pm, scrum-master, meeting-analyzer, jira-expert, confluence-expert, atlassian-admin, atlassian-templates, team-communications |
| `Skills/Executive Mentor/` | 6 skills — executive-mentor, board-prep, challenge, hard-call, postmortem, stress-test |
| `Skills/Finance/` | 3 skills — financial-analyst, saas-metrics-coach, finance-skills |
| `Skills/Markdown HTML/` | 11 skills — markdown-html-orchestrator, md-document, md-review, md-slides, design-system (mkdH), cs-markdown-html, cs-md-document, cs-md-review, cs-md-slides, cs-design-system, cs-grill-markdown-html |
| `Skills/Engineering/` | 15 skills — workflow-builder, cs-workflow-build, write-a-skill, cs-write-a-skill, caveman, cs-caveman, slopmop + 6 sm-* sub-commands, developing-claude-code-plugins, working-with-claude-code |

### Still to add (optional)

| Category | Skills |
|---|---|
| Helm | helm-chart-builder |
| Claude API plugin unique | frontend-design, webapp-testing, slack-gif-creator, 2slides-ppt-generator |

### Outstanding issue — index regeneration

`build_skill_brain.py` was updated with all new TRIGGERS and INTENT_GROUPS entries covering all 128 skills, but the Write tool silently truncates large files on the Windows filesystem mount. The script currently has only the file header (18 lines).

**Fix required (next session):** Write the full script via bash heredoc in chunks, then run it to regenerate `skills-lookup.yaml` and `Skill Quick Reference.md`. Both index files currently reflect only the original 71 skills and are also truncated.

The full updated script content (TRIGGERS dict + INTENT_GROUPS + functions) is documented in the session transcript.

## How to Add New Skills

1. Create a note in the appropriate `Skills/` subfolder
2. Add Obsidian frontmatter with `skill-id`, `plugin`, `category`, `tags`, `aliases`, and `triggers`
3. Paste the full SKILL.md content below (with its own `---` frontmatter block)
4. Run the generation script to update both index files:

```bash
python "_scripts/build_skill_brain.py"
```

The script is idempotent — it skips notes that already have `triggers` and regenerates both index files from scratch each run.

## How Claude Uses This Vault

At conversation start (when the vault is connected as a project folder), Claude reads:
- `Index/Skill Quick Reference.md` — first pass, intent matching
- `Index/skills-lookup.yaml` — if more trigger detail is needed
- Individual skill notes — when invoking a specific skill

Total token cost for full lookup: ~5,000 tokens across both files.

## Presentation

`Skill Brain Demo.html` — open in any browser. Animated neural network showing the skill hierarchy (Claude → categories → skills) with particle flows and live query demonstration. Built for presenting this architecture to stakeholders.

---

## Design Principle: Agents Read, Humans Write

The dominant community pattern (Greg Isenberg, InternetVin, et al.) is: **human thinking goes in the vault, Claude outputs go in `~/.claude/`**. Keep agents from polluting personal knowledge.

**This vault consciously inverts that pattern.** It is Claude's reference brain — authored by humans, optimised for Claude to read. Human thinking is not the primary content here; skill definitions are.

The rule still applies at the boundary: session memory, project files, and plans stay in `~/.claude/` or Cowork's memory system. The vault contains durable, curated skill knowledge only — not ephemeral Claude outputs.

**Practical implication:** do not store Claude-generated session content (plans, memory exports, task outputs) in this vault. If the vault ever expands into genuine PKM (personal notes, research, daily notes), the principle applies fully in that domain.

---

## Future Direction: QMD Semantic Search

See `Index/QMD Evaluation.md` for the full assessment.

Summary: QMD (`npm install -g @tobilu/qmd`) could replace the dual-index approach (~5,000 tokens per session) with a single semantic query returning only the relevant skill. Windows-compatible. Trial recommended before committing.

Custom `/skills` slash command (`D:\Claude Repo\Claude Skills Vault\.claude\commands\skills.md`) provides a structured alternative in the meantime — loads the right index file(s) on demand.
