---
context: conversation
description: Save key session context to the relevant Projects/ note in the Skills Vault
allowed-tools: Read, Edit, Write, AskUserQuestion
---

# /capture — Save Session Context

Saves key decisions, status changes, and discoveries from this session to the appropriate `Projects/` note in the Skills Vault.

## Instructions for Claude

### Step 1: Identify the project

Ask which project this session was for (if not obvious from context):

**Options:** SharePoint Uplift / Claude Skills Vault / Antigravity Skills / Other (specify)

### Step 2: Determine what to capture

Ask what is worth saving (multi-select):

1. **Phase / status changes** — what moved forward or is now complete
2. **Blockers** — new blockers or blockers resolved
3. **Key decisions** — choices made and why
4. **Files created or modified** — new deliverables, key edits
5. **Next steps** — clear action items for next session

### Step 3: Read the existing Projects/ note

Read `D:\Claude Repo\Claude Skills Vault\Projects\[Project Name].md` to understand current state.

### Step 4: Apply updates

Edit the note directly. Follow these rules:

- Update `last-updated` frontmatter date
- Move completed items to **Complete** section
- Add new blockers or remove resolved ones
- Add new key files if created
- Update **Next Steps** to reflect current state
- Keep entries brief — one line each
- Do not add session timestamps or verbose summaries

### Step 5: Confirm

Report what changed:
```
Projects/[Name].md updated.
Changed: [brief list]
```

---

## Notes

- Only save what is non-obvious and durable — not what can be re-derived from the files
- If the project doesn't have a Projects/ note yet, create one using `_scripts/project-claude-template.md` as a base
- Run `/preserve` instead if updating the vault's own CLAUDE.md
