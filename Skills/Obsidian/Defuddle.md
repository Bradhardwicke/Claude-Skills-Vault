---
name: defuddle
skill-id: defuddle
plugin: Obsidian Skills
category: Obsidian
tags:
- skill
- obsidian
- web
- clipping
- markdown
aliases:
- Web Clipper
- Defuddle CLI
- Clean Web Content
triggers:
- fetch URL clean
- extract article
- clean web page
- scrape article
- web content to markdown
- URL to markdown
- defuddle
---


# Defuddle

**Invoke:** `skill: "defuddle"` *(from obsidian-skills-main)*

Extracts clean markdown from web pages using the Defuddle CLI. Removes navigation, ads, and clutter to save tokens. Prefer over WebFetch for standard web pages.

## Triggers

- User provides a URL to read or analyse
- Online documentation, articles, or blog posts
- "Clip this page to markdown"
- Do NOT use for URLs ending in `.md` — use WebFetch directly

## Usage

```bash
# Install
npm install -g defuddle

# Extract to markdown
defuddle parse <url> --md

# Save to file
defuddle parse <url> --md -o content.md
```

## Related Skills

- [[Obsidian Markdown]]
- [[Obsidian CLI]]
