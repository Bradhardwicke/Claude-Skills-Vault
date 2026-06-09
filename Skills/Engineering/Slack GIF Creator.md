---
name: slack-gif-creator
skill-id: "document-skills:slack-gif-creator"
plugin: Document Skills
category: Engineering
tags: [skill, engineering, animation, gif, slack, media]
aliases: ["Slack GIF", "Animated GIF", "GIF Creator"]
triggers:
  - slack gif
  - animated gif
  - create gif for slack
  - make a gif
  - slack emoji gif
  - animated slack emoji
  - GIF animation
  - custom slack reaction
---

---
name: slack-gif-creator
description: "Knowledge and utilities for creating animated GIFs optimised for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like \"make me a GIF of X doing Y for Slack.\"."
license: Complete terms in LICENSE.txt
---

# Slack GIF Creator

Creates animated GIFs optimised for Slack constraints.

## Slack Requirements

| Type | Dimensions | Notes |
|---|---|---|
| Emoji GIF | 128x128 | Under 3 seconds |
| Message GIF | 480x480 | |

**Parameters:** FPS 10–30 (lower = smaller file), colours 48–128.

## Utilities

Core Python modules in `core/`: `gif_builder.py`, `frame_composer.py`, `easing.py`, `validators.py`.
