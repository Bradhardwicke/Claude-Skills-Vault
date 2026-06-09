---
context: conversation
description: Preserve session learnings to CLAUDE.md (Claude Skills Vault project)
model: opus
allowed-tools: Read, Edit, Write, Glob, Bash, AskUserQuestion
---

# /preserve - Preserve Session Knowledge to CLAUDE.md

Updates CLAUDE.md with key learnings from this session, optimised for context efficiency.

Vault path: `D:\Claude Repo\Claude Skills Vault`
Project repo: `D:\Claude Repo\Claude Skills Vault`

## Instructions for Claude

### Step 1: Check for CLAUDE.md

Look for CLAUDE.md in the current working directory:
- `CLAUDE.md`
- `.claude/CLAUDE.md`

If not found, ask:
"No CLAUDE.md found. Would you like me to create one, or output preservation notes to conversation instead?"

### Step 2: Ask What to Preserve

Use AskUserQuestion with multi-select:

**Question:** "What should be preserved from this session?"

**Options:**
1. **Phase/Status Changes:** What moved forward, what is now complete
2. **Key Decisions:** Choices made and why (for future reference)
3. **Files Modified:** Vault files created, edited, or standardised
4. **Patterns/Insights:** Reusable learnings, template decisions, Dataview query fixes
5. **Blockers/Warnings:** MCP timeouts, connectivity issues, frontmatter edge cases
6. **Next Steps:** Clear action items for the next vault session

### Step 3: Review Current CLAUDE.md

If CLAUDE.md exists, read it to understand:
- Current structure and format
- What sections exist
- What needs updating versus adding
- What workstreams are active or outstanding

### Step 4: Generate Updates

Based on selections, prepare updates following these rules:

**HIGH SIGNAL (include):**
- Vault workstream status changes (one line each)
- Decisions with rationale (table row format)
- Files standardised (brief list with tag changes)
- Outstanding workstreams (current count and scope)
- MCP connectivity notes or known failure patterns
- Dataview query patterns that work

**LOW SIGNAL (exclude):**
- Verbose explanations of Obsidian concepts
- Full file contents
- Timestamps or session logs (those go in /compress)
- Frontmatter block contents already saved to vault files

**FORMAT RULES:**
- Tables for structured data
- Single-line entries, not paragraphs
- Point to files: `See path/to/file.md`
- Target: CLAUDE.md under 280 lines
- Australian English throughout

**VAULT-SPECIFIC SECTIONS to maintain in CLAUDE.md:**

```
## Active Workstreams
| Workstream | Status | Remaining |
|---|---|---|

## Vault Conventions (PROTECTED)
- Date formats: Do MMMM YYYY (display) / YYYY-MM-DD (frontmatter)
- Tag casing: lowercase (person, company, meeting)
- Archive folder: .trash (not permanent deletion)
- No auto-move on template creation

## MCP Status
- Last confirmed: [date]
- Known issues: [any timeout patterns]
- Check command: Filesystem:list_allowed_directories
```

### Step 5: Apply Updates

Edit CLAUDE.md directly, then summarise:

```
CLAUDE.md Updated

Preserved:
- [What was added/changed]
- [What was added/changed]

CLAUDE.md is now [X] lines (target: <280)
```

### Step 6: Check Line Count and Archive Logic

After updating, count CLAUDE.md lines:
```bash
wc -l CLAUDE.md
```

**IF lines > 280:**

1. Identify auto-archivable content:
   - `## Session Notes (DATE)` sections older than 7 days
   - `## Completed Workstreams` section

2. Calculate impact and report to user:
   ```
   CLAUDE.md is [X] lines (target: <280).

   Auto-archivable content found:
   - Session Notes (YYYY-MM-DD) - 25 lines
   - Completed Workstreams - 15 lines

   Archiving would reduce to [Y] lines.

   Archive now? [Yes / No, all content is essential]
   ```

3. If still > 280 after auto-archivable content, identify other non-CORE, non-PROTECTED sections and ask user to confirm archiving.

4. If user approves: append archived content to `CLAUDE-Archive.md` in project root and remove from CLAUDE.md.

### Step 7: Archive File Handling

Walk up from pwd looking for CLAUDE.md or .git to find project root.
Archive to: `{project_root}/CLAUDE-Archive.md`

Archive file format:
```markdown
# CLAUDE.md Archive

Archived content from CLAUDE.md to maintain context efficiency.

---

## Archived: [DATE]

[Archived section content]

---
```

### Step 8: If No CLAUDE.md

Output a structured summary to conversation:

```markdown
# Session Preservation: [Brief Title]
**Project:** Claude Skills Vault
**Date:** [Today]

## [Selected sections with content]

---

## Quick Resume Context
[2-3 sentences for future sessions]
```

Then suggest: "Consider creating a CLAUDE.md to persist this across sessions."

---

## CORE Sections (Never Suggest Archiving)

- `## Vault Conventions`
- `## Active Workstreams`
- `## MCP Status`
- `## Key References`
- `## Vault Paths`
- `## Tag Taxonomy`
- Any section with `(PROTECTED)` in the heading

---

## Auto-Archivable Patterns

| Pattern | Rule |
|---------|------|
| `## Session Notes (DATE)` | Archive if DATE is > 7 days old |
| `## Completed Workstreams` | Always archivable |
| Sections with `(ARCHIVABLE)` | User-marked as archivable |

---

## Guidelines

- Context efficiency is paramount. Future sessions pay for every token.
- Signal over noise. The "why" matters more than the "what".
- Point, do not duplicate. Reference files instead of copying content.
- Respect existing format. Match the CLAUDE.md style already in use.
- Never archive PROTECTED or CORE sections.
- Ask before archiving non-auto content.
- Use Australian English and short sentences.
