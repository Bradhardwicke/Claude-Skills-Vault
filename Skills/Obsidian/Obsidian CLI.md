---
name: obsidian-cli
skill-id: obsidian-cli
plugin: Obsidian Skills
category: Obsidian
tags:
- skill
- obsidian
- cli
- terminal
- automation
aliases:
- obsidian CLI
- Vault CLI
- Obsidian Command Line
triggers:
- Obsidian vault
- manage notes
- vault search
- Obsidian command
- vault operations
- Obsidian CLI
---


# Obsidian CLI

**Invoke:** `skill: "obsidian-cli"` *(from obsidian-skills-main)*

Interacts with Obsidian vaults via the `obsidian` CLI. Requires Obsidian to be running. Supports reading, creating, searching notes, managing properties, and plugin development.

## Triggers

- Running `obsidian` CLI commands against a live vault
- Searching vault content from the command line
- Managing note properties programmatically
- Plugin development (reload, test, screenshot, DOM inspection)

## Key Commands

```bash
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" silent
obsidian search query="term" limit=10
obsidian property:set name="status" value="done"
obsidian plugin:reload id=my-plugin
```

## Related Skills

- [[Obsidian Markdown]]
- [[Obsidian Bases]]
- [[Desktop Commander Overview]]
