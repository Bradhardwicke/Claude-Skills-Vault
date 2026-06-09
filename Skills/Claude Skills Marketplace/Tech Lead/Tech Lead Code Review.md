---
name: tech-lead-code-review
skill-id: "tech-lead-code-review:tech-lead-code-review"
plugin: Tech Lead Code Review
category: Tech Lead
tags: [skill, tech-lead, code-review, quality-gates, review-culture, feedback]
aliases: ["Code Review Leadership", "Review Culture", "Quality Gates", "Code Review Standards"]
triggers:
  - code review standards
  - review culture
  - constructive feedback code review
  - review checklist design
  - merge strategy
  - quality gate definition
  - automated review setup
  - review metrics
  - define code review standards
  - setup quality gates
  - code review leadership
  - how do I improve our code reviews
  - code reviews are taking too long
  - reviews are not thorough enough
  - how to give better code review feedback
  - how to create a code review process
  - how to measure code review effectiveness
  - how to fix poor review culture
  - automate code review checks
  - how to get engineers to review code
  - how to handle code review disagreements
  - review is blocking delivery
  - what makes a good code review
---

---
name: tech-lead-code-review
description: "Code review standards, quality gates, review culture, constructive feedback patterns."
license: MIT
metadata:
  version: 1.0.0
  author: Seth Ford
  category: tech-lead
---

# Code Review Leadership Plugin

Establish comprehensive code review practices that balance quality, speed, and team health.

## Skills

This plugin includes 8 skills for building effective code review culture and infrastructure:

### Standards & Culture

- **code-review-standards** — Define acceptance criteria, approval roles, and escalation paths
- **review-culture-guide** — Build a culture where feedback improves code and team relationships
- **constructive-feedback** — Teach reviewers to give feedback that improves code without harming trust

### Practical Tools

- **review-checklist-design** — Create domain-specific review checklists that surface defects without creating busywork
- **merge-strategy** — Choose merge strategies (squash, rebase, commit) that match your workflow
- **quality-gate-definition** — Define automated gates (coverage, linting, security) that block before manual review

### Infrastructure & Measurement

- **automated-review-setup** — Configure CI/CD tooling, linters, and security scanners
- **review-metrics** — Track cycle time, participation diversity, and defect escape to measure and improve review health

## Commands

Chain skills to build complete review infrastructure:

- **define-standards** — Create comprehensive code review standards document with checklists and merge strategy
- **setup-quality-gates** — Configure automated tooling and gates with clear thresholds
- **review-metrics** — Establish metrics dashboard and health measurement process

## Key Principles

1. **Automate what's obvious**: Linting, formatting, security scans should be automated. Humans review design and logic
2. **Lead time matters most**: Optimise for fast reviews (< 24h) before optimising for depth
3. **Culture beats process**: Clear standards help, but a culture of trust and learning drives better outcomes
4. **Measurement without action is waste**: If you measure metrics, act on them when they trend wrong
5. **Feedback is a gift, not a burden**: Frame code review as mutual improvement, not gatekeeping

## How to Use

Each skill includes:

- Domain context grounded in research (Forsgren, Edmondson, McKinsey studies)
- Step-by-step instructions for creating artifacts (checklists, gates, culture norms)
- **Anti-Patterns section**: common mistakes (tool overload, culture without systems, metrics without action)
- Further reading from authoritative sources

Commands chain skills and suggest follow-up actions.

## Author

Seth Ford

## License

MIT
