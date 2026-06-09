---
description: Start session by loading context from CLAUDE.md + recent vault session logs
model: opus
allowed-tools: Read, Glob, Bash
---

# /resume - Resume Vault Work with Full Context

Quickly get up to speed by reading CLAUDE.md AND recent session logs.
Supports topic-based search for relevant past sessions.

Vault path: `D:\Claude Repo\Claude Skills Vault`
Project repo: `D:\Claude Repo\Claude Skills Vault`

**Usage:**
- `/resume`: Load CLAUDE.md + last 3 session summaries
- `/resume 5`: Load CLAUDE.md + last 5 session summaries
- `/resume people-tag`: Load CLAUDE.md + last 3 + search for "people-tag" related sessions
- `/resume 10 frontmatter`: Load CLAUDE.md + last 10 + search for "frontmatter"
- `/resume genesis`: Load CLAUDE.md + last 3 + search for genesis minerals sessions

## Instructions for Claude

### Step 1: Parse Arguments

Check if user provided arguments:
- **Number (N):** How many recent sessions to read (default: 3, max: 50)
- **Topic keyword:** Search for related sessions beyond the last N

Examples:
- `/resume` -> N=3, no topic search
- `/resume 5` -> N=5, no topic search
- `/resume people-tag` -> N=3, topic="people-tag"
- `/resume 10 paladin` -> N=10, topic="paladin"

### Step 2: Find and Read CLAUDE.md

Search for project memory file:
- `CLAUDE.md`
- `.claude/CLAUDE.md`

Read and extract:
- Current vault workstream status and outstanding counts
- Active client projects
- MCP connectivity last confirmed state
- Vault conventions and tag taxonomy
- Last known blockers
- Next steps

### Step 3: Find Session Logs

**Detect project root:**
1. Get current working directory (pwd)
2. Walk up from pwd looking for CLAUDE.md or .git
3. If found: project_root = that directory
4. If not found: project_root = pwd
5. Session logs path: `{project_root}/CC-Session-Logs/`

**List and count session logs:**
```bash
ls -1 "{project_root}/CC-Session-Logs/"*.md 2>/dev/null | wc -l
```

### Step 4: Read Session Summaries (Scaling Logic)

**IF session logs < 100:**
1. List all session log files, sorted by filename (newest first)
2. Read the SUMMARY ONLY (everything BEFORE "## Raw Session Log") for the last N files
3. If topic keyword provided, also scan all summaries for keyword matches

**IF session logs >= 100:**
1. Read last N session summaries directly
2. For topic matching, use grep to search through session logs:
   ```bash
   grep -rl "{topic keyword}" "{project_root}/CC-Session-Logs/"*.md
   ```
3. Read summaries of top 5 topic-matched results (if not already in last N)

**IMPORTANT: Only read up to "## Raw Session Log".** Do NOT read the full raw conversation. The summary contains the Quick Reference keywords needed for context.

### Step 5: Extract Key Information

From each session summary, extract:
- Date and topic (from filename and title)
- Confidence keywords (from Quick Reference section)
- Workstreams referenced
- Outcome (from Quick Reference section)
- Outstanding file counts for each workstream
- MCP status at end of session

### Step 6: Topic Search (If Keyword Provided)

If user provided a topic keyword:

1. For <100 logs: scan summaries for keyword matches
2. For >=100 logs: use grep to search session logs

Find sessions where:
- Topic name contains keyword
- Confidence keywords contain keyword
- Workstreams mentioned contain keyword
- Client project names match keyword

Add matched sessions to output (mark them as "RELATED SESSIONS").

### Step 7: Output Combined Report

```
======================================================
 RESUMING: Claude Skills Vault
======================================================

PHASE: Vault audit and standardisation

ACTIVE WORKSTREAMS:
- People tag rename: ~60 files remaining (People -> person)
- Company tag rename: 29 files remaining (Company -> company)
- Project frontmatter: 5 projects pending (Ora Banda, Genesis, Paladin, Tianqi, TLK)

MCP STATUS:
- Last confirmed: {date from CLAUDE.md}
- Check before bulk edits: Filesystem:list_allowed_directories

VAULT PATHS:
- Vault: D:\Claude Repo\Claude Skills Vault
- Assets: C:\Users\bradh\OneDrive\Project Management Assets
- Repo: D:\Claude Repo\Claude Skills Vault

BLOCKERS:
- {Any blockers, or "None"}

======================================================
 MOST RECENT SESSION: {DD-MM-YYYY HH:MM}
 Topic: {Topic Name}
======================================================

**Keywords:** {confidence keywords}
**Workstreams:** {workstreams referenced}
**Outcome:** {outcome summary}

**Key Points:**
- {Decision or learning 1}
- {Decision or learning 2}
- {Outstanding task if any}

======================================================
 PREVIOUS SESSIONS ({N-1} more)
======================================================

- {DD-MM-YYYY}: {Topic}, {Outcome snippet}
- {DD-MM-YYYY}: {Topic}, {Outcome snippet}

{If topic search was performed:}
======================================================
 RELATED SESSIONS (Topic: "{keyword}")
======================================================

- {DD-MM-YYYY}: {Topic}, {Why it matched}

======================================================
 READY TO:
======================================================

- Confirm MCP connectivity (run Filesystem:list_allowed_directories)
- {Next workstream from CLAUDE.md}
- {Pending task from recent session}
- {Additional next steps}

======================================================
```

### Step 8: Handle Edge Cases

**If no CLAUDE.md found:**
```
No CLAUDE.md found in this project.

Options:
1. Tell me about the current vault state and I will help create one
2. Just start working and run /preserve later

What would you like to do?
```

**If no session logs exist:**
- Skip the session logs sections entirely
- Show CLAUDE.md context only
- Note: "No session logs yet. Run /preserve and/or /compress before /compact to start building session history."

**If fewer than N session logs exist:**
- Read all available logs
- Note: "Found {X} session logs (requested {N})"

---

## Session Summary Reading Pattern

When reading a session log, STOP at "## Raw Session Log":

```python
# Pseudocode for reading summary only
content = read_file(session_log_path)
summary_end = content.find("## Raw Session Log")
if summary_end > 0:
    summary = content[:summary_end]
else:
    summary = content  # No raw log section, read all
```

This ensures context is restored without consuming tokens on the full conversation archive.

---

## Filename Parsing

Session log filenames follow: `DD-MM-YYYY-HH_MM-topic-name.md`

Parse to extract:
- **Date:** `DD-MM-YYYY`
- **Time:** `HH:MM` (replace _ with :)
- **Topic:** Everything after the time, with hyphens replaced by spaces

Example: `07-06-2026-09_30-people-tag-rename.md`
- Date: 07-06-2026
- Time: 09:30
- Topic: people tag rename

---

## Vault-Specific Topic Keywords

These keywords are most useful for topic-based resume searches:

| Keyword | What it finds |
|---------|---------------|
| `people-tag` | Sessions working on People -> person rename |
| `company-tag` | Sessions working on Company -> company rename |
| `frontmatter` | Any frontmatter standardisation session |
| `operations-meeting` | Operations Meeting file sessions |
| `genesis` | Genesis Minerals project sessions |
| `paladin` | Paladin project sessions |
| `tianqi` | Tianqi/TLK project sessions |
| `ora-banda` | Ora Banda project sessions |
| `moc` | Map of Content build sessions |
| `template` | Template creation or editing sessions |
| `dataview` | Dataview query sessions |
| `mcp` | MCP connectivity troubleshooting sessions |
| `home-page` | Home page or dashboard sessions |

---

## Performance Notes

- Default N=3: Keeps token usage low while providing recent context.
- Max N=50: Reasonable upper limit for summary scanning.
- Summary-only reading: Critical for token efficiency. Never read raw logs in /resume.
- Grep search: Lightweight and available everywhere.
- Always confirm MCP connectivity before starting bulk vault edits.