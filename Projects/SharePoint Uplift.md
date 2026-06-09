---
note-type: project
status: active
phase: Phase 0 — Foundation
last-updated: 2026-06-08
---

# SharePoint Uplift — Denver Technology

**Organisation:** Denver Technology — Australian MSP/tech consultancy, Perth.
**Brad's role:** Operations Manager / Senior BA. Project lead for intranet uplift.
**Path:** `D:\Claude Repo\SharePoint Uplift`

## Session Start

Read these two files at the start of every session:
1. `CLAUDE.md` — full project instructions and context
2. `skills/denver-sharepoint-skill.md` — SharePoint knowledge base

## Current Phase: Phase 0 — Foundation

**Active (unblocked):**
- Hub homepage redesign — building in "Denver Hub Preview" (isolated from production)
- Quick wins — removing obsolete nav, adding Wiki3 migration notice

**Blocked on Mark P (ICT):**
- Hub site registration (requires SharePoint Admin)
- Term Store Group Manager rights — ICT request submitted

**Complete:**
- Navigation audit, HLD v0.2, Metadata Taxonomy, KB Architecture design
- Project Register partially built (all columns except Technical Lead)
- RAG pipeline proven: Autotask → SharePoint `ProjectsFromAutotask` (517 records), colour pill JSON working

## Key Stakeholders

- **Mark Pepall (Mark P)** — ICT. Owns infrastructure, Autotask sync, admin access
- **Robert Dixon** — Full Control on `ProjectsFromAutotask` list

## Build Order (post Phase 0)

1. People and Culture site
2. Project Register (extend)
3. Clients Hub
4. Knowledge Base (replacing Wiki3)
5. Phase 1 dept sites: Delivery, ICT, P&C, DSC (shared PnP template)
6. Tools and Systems
7. Cutover and retire legacy sites

## Key Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | Full project instructions |
| `Denver_Intranet_ToDo.md` | Master checklist — current task state |
| `skills/denver-sharepoint-skill.md` | SharePoint knowledge base |
| `skills/useful-links.md` | Documentation URLs |
| `deliverables/` | HTML mockups, HLD.docx, KB architecture docs |
| `brand/` | Denver brand assets |

## Constraints

- Claude cannot deploy to SharePoint or create sites directly
- All admin actions performed by Brad or Mark P
- Use "Denver Hub Preview" for experimental work
- PnP PowerShell scripts must include pre-flight checks
- Foundation first (Term Store, hub registration) before content sites
