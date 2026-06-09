---
name: obsidian-bases
skill-id: obsidian-bases
plugin: Obsidian Skills
category: Obsidian
tags:
- skill
- obsidian
- bases
- database
- views
aliases:
- Obsidian Bases
- .base file
- Database View
- Obsidian Database
triggers:
- Obsidian Base
- .base file
- database view
- table view Obsidian
- card view
- Bases filter
---


# Obsidian Bases

**Invoke:** `skill: "obsidian-bases"` *(from obsidian-skills-main)*

Creates and edits Obsidian Bases (`.base` files) with views, filters, formulas, and summaries. Provides database-like views (table, cards, list, map) of vault notes.

## Triggers

- Creating a `.base` file
- Database-style views of notes
- "Table view of all my [tag] notes"
- Filtering notes by property, tag, or folder
- Computed properties (formulas) across notes

## Key Concepts

- Views: `table`, `cards`, `list`, `map`
- Filters using `and`, `or`, `not`
- File properties: `file.name`, `file.tags`, `file.mtime`, etc.
- Formulas: `if()`, `date()`, `now()`, `today()`

## Related Skills

- [[Obsidian Markdown]]
- [[Obsidian CLI]]
- [[JSON Canvas]]
