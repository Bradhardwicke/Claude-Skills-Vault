# CLAUDE.md - Claude Skills Vault

Project memory for the Claude Skills Vault — Claude's skill reference brain.
Updated by /preserve at end of each session.

---

## Vault Paths (PROTECTED)

| Name | Path |
|------|------|
| Vault | `D:\Claude Repo\Claude Skills Vault` |
| Repo root | `D:\Claude Repo` |
| Scripts | `D:\Claude Repo\Claude Skills Vault\_scripts` |
| Session logs | `D:\Claude Repo\Claude Skills Vault\CC-Session-Logs` |

---

## Purpose (PROTECTED)

This vault is Claude's "skill brain" — a token-efficient reference system for identifying and invoking the right skill for any task. It is optimised for Claude to read, not for human navigation.

**How Claude uses it at session start:**
1. Check Top 25 below — free (already in CLAUDE.md)
2. Read `Index/skills-lookup.yaml` only if skill not in Top 25 (~2,800 tokens)
3. Read individual skill notes in `Skills/` when invoking a specific skill

---

## Top 25 Skills (PROTECTED)

| skill-id | triggers |
|---|---|
| `docx` | word doc, .docx, report, letter, memo |
| `xlsx` | spreadsheet, .xlsx, Excel, budget, table |
| `pptx` | slides, deck, .pptx, presentation |
| `pdf` | PDF, .pdf, extract PDF, merge PDF, OCR |
| `pdf-viewer:view-pdf` | view PDF, annotate PDF, sign PDF |
| `data:analyze` | data analysis, what drove, metric lookup, investigate data |
| `data:write-query` | write SQL, SQL query, natural language to SQL |
| `data:create-viz` | chart, plot, graph, visualise data |
| `data:build-dashboard` | HTML dashboard, KPI cards, shareable report |
| `data:explore-data` | profile data, null check, new dataset, first look |
| `data:statistical-analysis` | statistics, hypothesis test, A/B test, p-value |
| `design:ux-copy` | microcopy, error message, button text, CTA |
| `design:design-critique` | design feedback, review mockup, UX review |
| `design:accessibility-review` | a11y audit, WCAG, colour contrast, screen reader |
| `operations:status-report` | status report, project health, RAG status |
| `operations:process-doc` | SOP, RACI, document process, flowchart |
| `operations:runbook` | runbook, on-call steps, deployment steps |
| `pm-skills:jira-expert` | Jira, JQL, sprint planning, board setup |
| `pm-skills:scrum-master` | scrum, velocity, retrospective, burndown |
| `sales:account-research` | research company, company intel, look up prospect |
| `sales:draft-outreach` | cold email, outreach email, reach out to |
| `productivity:task-management` | tasks, to do, what's on my plate |
| `mcp-builder` | build MCP, MCP server, FastMCP |
| `ai-agents-architect` | build agent, AI agent, autonomous agent |
| `stop-slop` | remove AI writing, AI slop, writing audit |

**Disambiguation:** `pdf` = file ops; `pdf-viewer:view-pdf` = interactive annotate/sign. `data:analyze` = answer a question; `data:explore-data` = first-look profiling. `pptx` = local python-pptx; `2slides-ppt-generator` = API-powered AI deck.

For skills not listed above, read `Index/skills-lookup.yaml`.

---

## Vault Structure (PROTECTED)

```
Claude Skills Vault/
├── Skills/              ← 144 skill notes (one per available skill)
│   ├── Documents/       ← docx, xlsx, pptx, pdf, view-pdf
│   ├── Data/            ← 10 data:* skills
│   ├── Design/          ← 7 design:* skills
│   ├── Operations/      ← 9 operations:* skills
│   ├── Sales/           ← 9 sales:* skills
│   ├── Productivity/    ← 4 productivity:* skills
│   ├── Obsidian/        ← defuddle, json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown
│   ├── Superpowers/     ← 14 skills (brainstorming, plans, TDD, debugging, code review, etc.)
│   ├── PM Skills/       ← 8 skills (senior-pm, scrum-master, jira, confluence, etc.)
│   ├── Executive Mentor/← 6 skills
│   ├── Finance/         ← 3 skills
│   ├── Markdown HTML/   ← 11 skills
│   ├── Engineering/     ← 15 skills
│   └── Plugin Management/
├── Index/
│   ├── Skill Quick Reference.md   ← CURATED intent guide (Top 20 + disambiguation)
│   ├── skills-lookup.yaml         ← AUTO-GENERATED compact intent→skill-id lookup
│   ├── Skills Index.md            ← human-readable MOC by plugin category
│   └── Skills Database.base       ← Obsidian Base view (human use)
├── _scripts/
│   └── build_skill_brain.py       ← regenerates both index files from skill notes
├── .claude/commands/              ← CPR commands (preserve, compress, resume)
├── CLAUDE.md                      ← this file
├── Project Context.md             ← full design decisions and history
└── Welcome.md                     ← vault overview
```

---

## Skill Note Structure (PROTECTED)

Each skill note has two frontmatter blocks — Obsidian frontmatter (for lookup) followed by the verbatim SKILL.md content:

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
# SKILL.md frontmatter (verbatim from plugin)
name: analyze
description: Answer data questions...
---

# Full SKILL.md content follows...
```

The `triggers` field is the key addition — intent-focused phrases the build script reads to generate the YAML lookup.

---

## MCP Status (PROTECTED)

- **Obsidian CLI:** Enabled. Invocation pattern (Windows): `Start-Process "C:\Program Files\Obsidian\Obsidian.exe" -ArgumentList "vault" -Wait -NoNewWindow -RedirectStandardOutput $tmpFile`
- **Desktop Commander:** Active — use for file read/write operations on this vault.

---

## Active Workstreams

| Workstream | Status | Detail |
|---|---|---|
| Build script | Complete | `_scripts/build_skill_brain.py` working (238 lines). Run from vault root to regenerate. |
| Index files | Complete | Both index files current — 144 skills, 1,105 triggers (as of 2026-06-07) |
| All skills added | Complete | helm-chart-builder, frontend-design, webapp-testing, slack-gif-creator, 2slides-ppt-generator all added |
| Obsidian CLI | Complete | Enabled and working. See MCP Status for invocation pattern. |
| Vault health | Complete | 34 unresolved links remaining — all plugin-internal refs, acceptable |

---

## How to Add a New Skill

1. Create a note in the appropriate `Skills/` subfolder
2. Add Obsidian frontmatter with `skill-id`, `plugin`, `category`, `tags`, `aliases`, and `triggers`
3. Paste the full SKILL.md content below (with its own `---` frontmatter block)
4. Run the generation script to update both index files:

```bash
cd "D:\Claude Repo\Claude Skills Vault"
python "_scripts/build_skill_brain.py"
```

The script is idempotent — skips notes already processed, regenerates both index files from scratch.

---

## Session Log Pattern

Session logs saved to: `D:\Claude Repo\Claude Skills Vault\CC-Session-Logs\`
Filename format: `DD-MM-YYYY-HH_MM-topic-name.md`

Use `/resume` to load recent session context.
Use `/preserve` to update this file.
Use `/compress` then `/compact` to end a session.

---

## Next Steps

_(Updated by /preserve — keep this section current)_

1. Keep index current by running `python "_scripts/build_skill_brain.py"` whenever skills are added
