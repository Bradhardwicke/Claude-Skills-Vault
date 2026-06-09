---
note-type: dashboard
status: active
last-updated: 2026-06-08
---

# Vault Health Dashboard

Live Dataview queries for monitoring vault completeness and quality. Requires the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin.

---

## Skill Count by Plugin

```dataview
TABLE length(rows) AS "Skill Count"
FROM "Skills"
WHERE contains(tags, "skill")
GROUP BY plugin
SORT length(rows) DESC
```

---

## Skills Without Triggers

Skills that will not appear in the auto-generated `skills-lookup.yaml`.

```dataview
LIST
FROM "Skills"
WHERE contains(tags, "skill") AND (!triggers OR length(triggers) = 0)
SORT file.name ASC
```

---

## Skills Without Aliases

```dataview
LIST
FROM "Skills"
WHERE contains(tags, "skill") AND (!aliases OR length(aliases) = 0)
SORT file.name ASC
```

---

## Skills Without a skill-id

Misconfigured notes that will break the build script.

```dataview
LIST
FROM "Skills"
WHERE contains(tags, "skill") AND !file.frontmatter["skill-id"]
SORT file.name ASC
```

---

## Recently Updated Skills

```dataview
TABLE plugin, file.mtime AS "Last Modified"
FROM "Skills"
WHERE contains(tags, "skill")
SORT file.mtime DESC
LIMIT 10
```

---

## All Skills by Category

```dataview
TABLE plugin
FROM "Skills"
WHERE contains(tags, "skill")
SORT plugin ASC, file.name ASC
```

---

## Notes

- Run `python "_scripts/build_skill_brain.py"` after fixing any issues surfaced above
- Target: zero skills without triggers or skill-id
