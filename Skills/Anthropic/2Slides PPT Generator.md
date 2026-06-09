---
name: 2slides-ppt-generator
skill-id: "2slides-ppt-generator"
plugin: Anthropic Skills
category: Anthropic
tags: [skill, presentations, slides, api, ai]
aliases: ["2slides", "AI Deck Generator", "API Slides"]
triggers:
  - create presentation via API
  - 2slides
  - AI-powered slides
  - slides from document
  - AI deck generation
  - presentation from text
  - voice narration slides
  - match slide style from image
  - generate deck API
---

---
name: 2slides-ppt-generator
description: "AI-powered presentation generation via the 2slides API — create slides from text, match a reference image style, summarize documents into decks, add AI voice narration, and export pages/audio. Use for any \"make slides\", \"create a deck\", or \"slides from this document\" request."
category: api-integration
tags: [presentations, slides, powerpoint, ai, api-integration, pdf, narration, document-summarization]
---

# 2slides Presentation Generation

Generate professional presentations using the 2slides AI API. Supports:
- Content-based generation (Fast PPT with theme selection)
- Style matching from a reference image
- Custom PDF design
- Document summarisation
- AI voice narration
- Export slides as PNG + audio as WAV

## Requirements

- 2slides API key from https://2slides.com/api (500 free credits on signup)
- Credits per operation vary; check https://2slides.com/pricing

## Disambiguation

Use this over `pptx` when the user wants AI-generated deck content via the 2slides API with narration or style-matching. Use `pptx` for local python-pptx file creation/editing.
