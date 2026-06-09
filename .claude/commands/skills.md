---
context: conversation
description: Load skill index context for skill selection and invocation
allowed-tools: Read, Glob
---

# /skills — Load Skill Index

Loads the vault's skill index into context so Claude can identify and invoke the right skill for a task — without reading the full dual-index manually.

## Instructions for Claude

### Step 1: Read the quick reference

Read the curated intent guide first:

```
D:\Claude Repo\Claude Skills Vault\Index\Skill Quick Reference.md
```

This covers the Top 20 most-used skills and key disambiguation cases (~2,300 tokens).

### Step 2: Read the lookup YAML if needed

If the task requires a skill not in the Top 20, read the full trigger lookup:

```
D:\Claude Repo\Claude Skills Vault\Index\skills-lookup.yaml
```

This maps 1,100+ intent phrases to skill IDs (~2,800 tokens).

### Step 3: Report what was loaded

Briefly confirm:

```
Skill index loaded.
[X] skills across [Y] plugins.
Ready — what do you need?
```

### Step 4: Proceed with task

Use the loaded context to identify the right skill and invoke it with the Skill tool.

---

## When to Use

Run `/skills` at the start of any session where you will be:
- Selecting a skill for a task
- Checking what skills are available
- Deciding between two similar skills
- Invoking a skill that requires reading its SKILL.md first

This replaces the manual "read both index files" step and ensures the right skill is selected efficiently.
