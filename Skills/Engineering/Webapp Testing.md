---
name: webapp-testing
skill-id: "document-skills:webapp-testing"
plugin: Document Skills
category: Engineering
tags: [skill, engineering, testing, playwright, browser, frontend]
aliases: ["Web App Testing", "Playwright Testing", "Browser Testing"]
triggers:
  - test web app
  - playwright
  - browser automation
  - frontend testing
  - UI testing
  - test local app
  - browser screenshot
  - verify UI
  - debug UI behaviour
  - browser logs
  - test React app
---

---
name: webapp-testing
description: "Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behaviour, capturing browser screenshots, and viewing browser logs."
license: Complete terms in LICENSE.txt
---

# Web Application Testing

Test local web apps using Playwright scripts.

## Helper Scripts

- `scripts/with_server.py` — manages server lifecycle (run with `--help` first)

## Approach

Static HTML → read file directly for selectors. Dynamic app → use Playwright with `with_server.py`.

Always run helper scripts with `--help` before reading source — they're black-box utilities, not context to ingest.
