---
name: json-canvas
skill-id: json-canvas
plugin: Obsidian Skills
category: Obsidian
tags:
- skill
- obsidian
- canvas
- visual
- mindmap
aliases:
- Canvas File
- .canvas
- Obsidian Canvas
triggers:
- canvas file
- Obsidian canvas
- mind map
- visual canvas
- .canvas file
- JSON canvas
---


# JSON Canvas

**Invoke:** `skill: "json-canvas"` *(from obsidian-skills-main)*

Creates and edits JSON Canvas files (`.canvas`) with nodes, edges, groups, and connections. Supports text, file, link, and group node types.

## Triggers

- Working with `.canvas` files
- Creating visual canvases, mind maps, or flowcharts in Obsidian
- Connecting notes visually
- "Create a canvas for..."

## Key Concepts

- Nodes: `text`, `file`, `link`, `group`
- Edges connect nodes via `fromNode` / `toNode`
- IDs are 16-char hex strings
- Coordinates: `x` right, `y` down

## Related Skills

- [[Obsidian Markdown]]
- [[Obsidian CLI]]
