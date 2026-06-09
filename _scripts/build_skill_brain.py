#!/usr/bin/env python3
"""
Claude Skills Vault - Skill Brain Builder
Generates:
  1. Index/skills-lookup.yaml
  2. Index/Skill Quick Reference.md
"""

import yaml
import re
import sys
from pathlib import Path
from datetime import date
from collections import defaultdict

VAULT = Path(__file__).parent.parent
SKILLS_DIR = VAULT / "Skills"
INDEX_DIR = VAULT / "Index"


def extract_frontmatters(text):
    pattern = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL | re.MULTILINE)
    return pattern.findall(text)


def to_list(val):
    if val is None:
        return []
    if isinstance(val, list):
        return [str(x) for x in val]
    return [str(val)]


def parse_skill(path: Path):
    try:
        text = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Warning: cannot read {path.name}: {e}", file=sys.stderr)
        return None

    blocks = extract_frontmatters(text)
    if not blocks:
        return None

    try:
        obs = yaml.safe_load(blocks[0])
    except Exception as e:
        print(f"  Warning: YAML error in {path.name}: {e}", file=sys.stderr)
        return None

    if not obs or 'skill-id' not in obs:
        return None

    skill = {
        'skill-id':    str(obs['skill-id']),
        'name':        str(obs.get('name', obs['skill-id'])),
        'plugin':      str(obs.get('plugin', '')),
        'category':    str(obs.get('category', '')),
        'aliases':     to_list(obs.get('aliases')),
        'triggers':    to_list(obs.get('triggers')),
        'description': '',
    }

    if len(blocks) >= 2:
        try:
            skill_fm = yaml.safe_load(blocks[1])
            if skill_fm and 'description' in skill_fm:
                skill['description'] = str(skill_fm['description']).strip()
        except Exception:
            pass

    return skill


def write_lookup_yaml(skills):
    out_path = INDEX_DIR / "skills-lookup.yaml"
    today = date.today().isoformat()
    total_triggers = sum(len(s['triggers']) for s in skills)

    lines = [
        f"# Skills lookup | {len(skills)} skills | {total_triggers} triggers | {today} | run build_skill_brain.py to refresh",
        "",
    ]

    for skill in sorted(skills, key=lambda s: s['skill-id'].lower()):
        triggers = [t.strip() for t in skill['triggers'] if t.strip()]
        if not triggers:
            continue
        trigger_list = ", ".join(f'"{t}"' for t in triggers)
        lines.append(f"{skill['skill-id']}: [{trigger_list}]")

    content = '\n'.join(lines) + '\n'
    out_path.write_text(content, encoding='utf-8')
    print(f"Wrote {out_path.name} -- {len(skills)} skills, {total_triggers} triggers, {len(content.splitlines())} lines")


TOP_25 = [
    ("docx",                        ["word doc", ".docx", "report"],                     None),
    ("xlsx",                        ["spreadsheet", ".xlsx", "Excel"],                   None),
    ("pptx",                        ["slides", "deck", ".pptx"],                         None),
    ("pdf",                         ["PDF", ".pdf", "extract PDF"],                      "create/extract/merge -- not interactive viewing"),
    ("pdf-viewer:view-pdf",         ["view PDF", "annotate PDF", "sign PDF"],            "interactive viewer -- not text extraction"),
    ("data:analyze",                ["data analysis", "what drove", "metric lookup"],    None),
    ("data:write-query",            ["write SQL", "SQL query", "natural language to SQL"], None),
    ("data:create-viz",             ["chart", "plot", "graph"],                          None),
    ("data:build-dashboard",        ["HTML dashboard", "KPI cards", "shareable report"], None),
    ("data:explore-data",           ["profile data", "null check", "new dataset"],       "first-look profiling; use data:analyze for questions"),
    ("data:statistical-analysis",   ["statistics", "hypothesis test", "A/B test"],      None),
    ("design:ux-copy",              ["microcopy", "error message", "button text"],       None),
    ("design:design-critique",      ["design feedback", "review mockup", "UX review"],  None),
    ("design:accessibility-review", ["a11y audit", "WCAG", "color contrast"],           None),
    ("operations:status-report",    ["status report", "project health", "RAG status"],  None),
    ("operations:process-doc",      ["SOP", "RACI", "document process"],                None),
    ("operations:runbook",          ["runbook", "on-call steps", "deployment steps"],   None),
    ("pm-skills:jira-expert",       ["Jira", "JQL", "sprint planning"],                 None),
    ("pm-skills:scrum-master",      ["scrum", "velocity", "retrospective"],             None),
    ("sales:account-research",      ["research company", "company intel", "look up company"], None),
    ("sales:draft-outreach",        ["cold email", "outreach email", "reach out to"],   None),
    ("productivity:task-management",["tasks", "to do", "what's on my plate"],           None),
    ("mcp-builder",                 ["build MCP", "MCP server", "FastMCP"],             None),
    ("ai-agents-architect",         ["build agent", "AI agent", "autonomous agent"],    None),
    ("stop-slop",                   ["remove AI writing", "AI slop", "writing audit"],  None),
]

DISAMBIGUATION = """\
## Disambiguation

| Confused about... | Rule |
|---|---|
| `docx` vs `pdf` | docx = Word files; pdf = create/extract/OCR PDF |
| `pdf` vs `pdf-viewer:view-pdf` | pdf = file ops; pdf-viewer = interactive annotate/sign |
| `data:analyze` vs `data:explore-data` | analyze = answer a question; explore = first-look profiling |
| `data:write-query` vs `data:sql-queries` | write-query = best practice SQL; sql-queries = dialect-specific syntax |
| `data:create-viz` vs `data:build-dashboard` | create-viz = single chart; build-dashboard = multi-chart HTML page |
| `internal-comms` vs `pm-skills:team-communications` | internal-comms = general; team-comms = PM/Atlassian context |
| `caveman:caveman` vs `caveman:cs-caveman` | caveman = one-shot compressed reply; cs-caveman = persistent session mode |
| `pptx` vs `2slides-ppt-generator` | pptx = python-pptx local; 2slides = API-powered AI deck |"""


def write_quick_reference(skills):
    out_path = INDEX_DIR / "Skill Quick Reference.md"
    today = date.today().isoformat()

    lines = [
        "---",
        "note-type: skill-quick-ref",
        f"generated: {today}",
        "---",
        "",
        "# Skill Quick Reference",
        "",
        "Match intent to trigger, invoke with `Skill tool -> skill-id`.",
        f"Refresh: `python _scripts/build_skill_brain.py` | {len(skills)} skills indexed.",
        "",
        "---",
        "",
        "## Top 25 Skills",
        "",
        "| skill-id | triggers | note |",
        "|---|---|---|",
    ]

    for (sid, triggers, note) in TOP_25:
        trig_str = " / ".join(f"`{t}`" for t in triggers)
        note_str = note or ""
        lines.append(f"| `{sid}` | {trig_str} | {note_str} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(DISAMBIGUATION)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## All Skills by Category")
    lines.append("")
    lines.append("*(Full trigger list in `skills-lookup.yaml`)*")
    lines.append("")

    by_cat = defaultdict(list)
    for s in skills:
        cat = s['category'] or 'Other'
        by_cat[cat].append(s)

    CATEGORY_ORDER = [
        "Anthropic", "Data", "Design", "Operations", "Sales",
        "PM Skills", "Finance", "Productivity", "Engineering",
        "Superpowers", "Obsidian", "Markdown HTML", "PDF Viewer",
        "Desktop Commander", "Plugin Management", "Writing",
        "Executive Mentor", "SharePoint SPFx",
    ]
    ordered = CATEGORY_ORDER + [c for c in sorted(by_cat) if c not in CATEGORY_ORDER]

    for cat in ordered:
        if cat not in by_cat:
            continue
        lines.append(f"**{cat}**")
        cat_skills = sorted(by_cat[cat], key=lambda s: s['skill-id'])
        for s in cat_skills:
            t3 = s['triggers'][:3]
            trig_str = ", ".join(t3) if t3 else ""
            lines.append(f"- `{s['skill-id']}` -- {trig_str}")
        lines.append("")

    content = '\n'.join(lines) + '\n'
    out_path.write_text(content, encoding='utf-8')
    print(f"Wrote {out_path.name} -- {len(content.splitlines())} lines")


def main():
    print(f"Scanning {SKILLS_DIR} ...")

    skills = []
    skipped = []

    for md_file in sorted(SKILLS_DIR.rglob('*.md')):
        skill = parse_skill(md_file)
        if skill:
            skills.append(skill)
        else:
            skipped.append(md_file.name)

    print(f"Indexed: {len(skills)} skills")
    if skipped:
        print(f"Skipped ({len(skipped)} files with no skill-id): "
              + ", ".join(skipped[:10]) + ("..." if len(skipped) > 10 else ""))

    INDEX_DIR.mkdir(exist_ok=True)

    write_lookup_yaml(skills)
    write_quick_reference(skills)

    print("Done.")


if __name__ == '__main__':
    main()
