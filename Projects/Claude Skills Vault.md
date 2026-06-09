---
note-type: project
status: active
last-updated: 2026-06-08
---

# Claude Skills Vault

**Purpose:** Claude's skill brain — token-efficient reference for identifying and invoking the right skill for any task.
**Path:** `D:\Claude Repo\Claude Skills Vault`

## Current State

- 144 skills across 17 categories
- Build script working: `python "_scripts/build_skill_brain.py"` from vault root
- Both index files current: 144 skills, 1,105 triggers
- Dataview health dashboard live: `Index/Vault Health Dashboard.md`
- Global CLAUDE.md written: `C:\Users\bradh\.claude\CLAUDE.md`

## Key Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | Vault instructions + Top 25 skill table |
| `Index/skills-lookup.yaml` | Auto-generated trigger lookup (144 skills, 1,105 triggers) |
| `Index/Skill Quick Reference.md` | Curated intent guide |
| `Index/Vault Health Dashboard.md` | Dataview health queries |
| `Index/QMD Evaluation.md` | Semantic search trial notes |
| `_scripts/build_skill_brain.py` | Regenerates both index files |
| `.claude/commands/skills.md` | `/skills` — loads index on demand |
| `.claude/commands/capture.md` | `/capture` — saves session context to Projects/ |

## Next Steps

1. Trial QMD — see `Index/QMD Evaluation.md`
2. Run build script whenever new skills are added
3. Keep Projects/ notes current via `/capture` at session end
