---
context: conversation
description: Smart Conversation Compression with Session Logging (Brad Hardwicke Vault)
model: opus
allowed-tools: Read, Write, Bash, AskUserQuestion
---

# /compress - Smart Conversation Compression

Prepares preservation notes for conversation compaction AND saves the full session to searchable logs.

Run this BEFORE `/compact`.

**Workflow:** `/preserve` (optional) -> `/compress` -> answer questions -> session saved -> `/compact` (always last)

Vault path: `D:\Claude Repo\Claude Skills Vault`
Project repo: `D:\Claude Repo\Claude Skills Vault`

## Instructions for Claude

When the user runs `/compress`, follow these steps:

### Step 1: Ask What to Preserve

Use the AskUserQuestion tool with the following multi-select question:

**Question:** "What would you like to preserve from this conversation?"

**Options (multi-select enabled):**
1. **Key Learnings:** Vault insights, frontmatter patterns, Dataview fixes, tag taxonomy decisions
2. **Solutions and Fixes:** Edit approaches that worked, MCP reconnection steps, bulk edit patterns
3. **Decisions Made:** Choices about tag naming, template structure, PARA organisation
4. **Files Modified:** Vault files created, standardised, or edited with brief descriptions
5. **MCP and Config:** Connectivity status, allowed paths, timeout patterns encountered
6. **Pending Tasks:** Outstanding workstreams, files not yet processed, next actions
7. **Errors and Workarounds:** MCP timeouts, frontmatter edge cases, edit failures and fixes

### Step 2: Ask for Custom Preservation (Optional)

Call AskUserQuestion with:
- **question:** "Anything specific you want to highlight or remember from this session?"
- **header:** "Custom note"
- **multiSelect:** false
- **options:**
  1. `{ label: "Skip", description: "No custom notes, continue with session log" }`
  2. `{ label: "Add a custom note", description: "Provide a custom note to preserve" }`

If the user selects "Skip", set custom notes to "None". If the user provides input, treat it verbatim.

### Step 3: Confirm Topic Name

Analyse the conversation and derive a concise topic name (3-5 words, lowercase, hyphens).

Examples for vault sessions:
- `people-tag-rename`
- `operations-meeting-frontmatter`
- `project-files-standardisation`
- `moc-layer-build`
- `home-page-dataview`

Call AskUserQuestion with:
- **question:** `Topic name for this session log: "{suggested-name}". Confirm or provide a different one?`
- **header:** "Topic name"
- **multiSelect:** false
- **options:**
  1. `{ label: "Accept: {suggested-name}", description: "Use the suggested topic name" }`
  2. `{ label: "Provide a different name", description: "Use a custom topic name instead" }`

### Step 4: Generate Session Log

Create the session log content with this structure:

```markdown
# Session Log: DD-MM-YYYY HH:MM - {Topic Name}

## Quick Reference (for AI scanning)
**Confidence keywords:** {extracted keywords from conversation}
**Workstreams:** {vault workstreams referenced}
**Outcome:** {1-sentence outcome summary}

## Decisions Made
- {Decision 1 with brief rationale}
- {Decision 2 with brief rationale}

## Key Learnings
- {Learning 1}
- {Learning 2}

## Solutions and Fixes
- {Solution 1}
- {Solution 2}

## Files Modified
- `{vault path/to/file}`: {what changed - tag rename, frontmatter standardised, etc.}

## MCP and Config
- {MCP status, connectivity note, or path confirmed}

## Pending Tasks
- {Pending workstream or file count}

## Errors and Workarounds
- {Error and fix}

## Key Exchanges
- {Notable exchange 1, brief summary}

## Custom Notes
{User's custom notes from Step 2, or "None"}

---

## Quick Resume Context
{2-3 sentences that would help resume vault work in a future session. Include outstanding workstream counts and last confirmed MCP status.}

---

## Raw Session Log

{FULL CONVERSATION - Copy the entire conversation history here, preserving all user messages and assistant responses. This is the searchable archive.}
```

**IMPORTANT:** Only include sections the user selected in Step 1. Always include:
- Quick Reference (for AI scanning)
- Quick Resume Context
- Raw Session Log

### Step 5: Detect Project Root and Save

**Generate filename:**
```
DD-MM-YYYY-HH_MM-{topic-name}.md
```
Example: `07-06-2026-09_30-people-tag-rename.md`

**Detect project root:**
1. Get current working directory (pwd)
2. Walk up from pwd looking for CLAUDE.md or .git
3. If found: project_root = that directory
4. If not found: project_root = pwd
5. Session logs path: `{project_root}/CC-Session-Logs/`
6. Create folder if it does not exist: `mkdir -p "{project_root}/CC-Session-Logs/"`
7. Write session log there

**Save the session log:**
```bash
mkdir -p "{project_root}/CC-Session-Logs/"
# Then write session log to {project_root}/CC-Session-Logs/{filename}
```

### Step 6: Confirm and Instruct

Output confirmation:

```markdown
## Session Saved Successfully

### File Created

**Session Log:**
`{project_root}/CC-Session-Logs/{filename}`

### Session Summary
- **Vault project:** Claude Skills Vault
- **Topic:** {topic-name}
- **Sections preserved:** {list of selected sections}
- **Keywords:** {confidence keywords}
- **Outstanding workstreams:** {note any pending tasks captured}

---

**Next step:** Run `/compact` to compress the conversation context (always last).

The session log is saved locally. Use `/resume` to load context from recent sessions.
```

---

## Vault-Specific Confidence Keywords

When generating the "Confidence keywords" field, extract from these vault-relevant categories:
- Workstream names (people-tag, company-tag, project-frontmatter, operations-meeting)
- Client project names (genesis-minerals, tianqi, tlk, talison, paladin, atom, ora-banda)
- Vault structure terms (PARA, MOC, frontmatter, dataview, templater, template)
- Tag changes (People->person, Company->company, meeting, denver, activeproject)
- MCP status (filesystem-mcp, timeout, reconnect, list-allowed-directories)
- Action types (standardise, rename, audit, batch, bulk-edit, read-multiple-files)
- Colleagues (ben-mills, keren-jenns, adam-fry, matt-clayton, carrie-beattie)

---

## Guidelines

- Be concise. Each bullet should be actionable or informative.
- Use code blocks for file paths, tag values, and frontmatter snippets.
- Include file paths with folder context for vault files.
- Preserve exact tag values and frontmatter field names. Do not paraphrase these.
- Note MCP connectivity state at session end.
- Record outstanding file counts for each workstream.
- Extract keywords that will help future `/resume` searches.
- The Raw Session Log must contain the COMPLETE conversation for searchability.
- Use Australian English throughout.