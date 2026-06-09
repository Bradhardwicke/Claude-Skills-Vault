---
name: inkscape-mcp
skill-id: "inkscape:inkscape-mcp"
plugin: Inkscape
category: Engineering
tags: [skill, design, mcp, inkscape, svg]
aliases: [Inkscape MCP Server, SVG Export MCP]
triggers:
  - inkscape
  - export svg
  - svg to png
  - svg to pdf
  - convert svg
  - optimise svg
  - batch export svg
  - inkscape actions
  - query svg objects
  - svg bounding box
  - design export
  - vector export
---

---
name: inkscape-mcp
description: "Python FastMCP server wrapping the Inkscape CLI. Provides SVG export, object info queries, action sequences, SVG optimisation, and batch export."
---

# Inkscape MCP Server

**Location:** `D:\Claude Repo\inkscape-mcp\`
**Entry point:** `server.py`
**Transport:** stdio

## Setup

```bash
cd "D:\Claude Repo\inkscape-mcp"
pip install -r requirements.txt
```

Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "inkscape": {
      "command": "python",
      "args": ["D:\\Claude Repo\\inkscape-mcp\\server.py"]
    }
  }
}
```

Optional: set `INKSCAPE_PATH` env var if Inkscape is not at the default location (`C:\Program Files\Inkscape\bin\inkscape.exe`).

## Tools

| Tool | Purpose |
|------|---------|
| `inkscape_check` | Verify install, return version |
| `inkscape_export` | Export SVG to png/pdf/eps/ps/emf/wmf/xaml with DPI, area, size |
| `inkscape_get_info` | Query all objects or a specific object ID for bounding boxes (JSON) |
| `inkscape_run_actions` | Execute an `--actions` sequence; optionally save result or return inline SVG |
| `inkscape_svg_to_optimised` | Pipe SVG through Inkscape to clean/normalise; reports byte reduction |
| `inkscape_batch_export` | Concurrently export multiple files; returns JSON success/failure summary |

## Key design notes

- All subprocess calls go through `_run()` helper using `run_in_executor` — non-blocking
- `INKSCAPE_PATH` env var with Windows default fallback; also tries `shutil.which("inkscape")`
- Error messages include install URL when binary not found
- Pydantic models with `extra="forbid"` on all tool inputs

## When to use

Reach for this MCP when the user needs to:
- Export SVGs to raster or print formats
- Query object dimensions or positions in an SVG
- Automate Inkscape transformations via action sequences
- Batch-process multiple SVG files
- Optimise/normalise SVG output

For design creation (not export), prefer the Figma MCP or canvas-design skill.
