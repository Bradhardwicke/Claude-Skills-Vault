---
name: tech-lead-planning
skill-id: "tech-lead-planning:tech-lead-planning"
plugin: Tech Lead Planning
category: Tech Lead
tags: [skill, tech-lead, planning, estimation, roadmap, capacity]
aliases: ["Technical Planning", "Sprint Planning", "Technical Roadmap", "Estimation", "Dependency Mapping"]
triggers:
  - technical roadmap
  - capacity planning
  - sprint planning
  - estimation techniques
  - velocity analysis
  - work breakdown structure
  - dependency mapping
  - risk register
  - technical debt prioritisation
  - plan sprint
  - estimate work
  - build roadmap
  - how do I plan a sprint
  - how to estimate engineering work
  - how to create a technical roadmap
  - capacity planning for an engineering team
  - how to map dependencies between teams
  - how to identify and track risks
  - how to manage the tech debt backlog
  - how to track team velocity
  - how to plan the next quarter
  - team workload planning
  - how to break down a large project
  - plan technical work alongside product roadmap
---

---
name: tech-lead-planning
description: "Technical roadmaps, estimation, sprint planning, capacity planning, dependency mapping."
license: MIT
metadata:
  version: 1.0.0
  author: Seth Ford
  category: tech-lead
---

# Technical Planning Plugin

Master sprint planning, estimation, roadmaps, and capacity management for tech leads.

## Skills

This plugin includes 9 skills for comprehensive technical planning:

### Core Planning

- **technical-roadmap** — Build multi-quarter technical roadmaps aligned with business goals, with clear narratives and trade-offs
- **capacity-planning** — Model team capacity across quarters, accounting for hiring, attrition, and ramp time
- **sprint-planning-guide** — Facilitate sprint planning that balances delivery, learning, and team health

### Estimation & Measurement

- **estimation-techniques** — Apply evidence-based methods (story points, t-shirt sizing, planning poker) with confidence bands
- **velocity-analysis** — Track and interpret sprint velocity to forecast capacity, identify bottlenecks, and improve forecasts

### Complex Work Management

- **work-breakdown-structure** — Decompose large initiatives into manageable epics with clear ownership and milestones
- **dependency-mapping** — Identify and visualise dependencies to prevent blocked work and optimise critical path
- **risk-register** — Create living risk documents with mitigation strategies for high-impact uncertainties
- **technical-debt-prioritization** — Systematically evaluate and prioritise debt against features, with ROI modelling

## Commands

Chain skills together to run complete planning workflows:

- **plan-sprint** — Full sprint planning from capacity calculation to committed sprint backlog
- **estimate-work** — Estimate features or epics with risk-based confidence bands
- **build-roadmap** — Create a 3-12 month technical roadmap with quarterly milestones and dependencies
- **map-dependencies** — Visualise and manage critical path across teams and initiatives

## How to Use

Each skill includes:

- Domain context grounded in real frameworks and authors (Larson, Fournier, Reilly, etc.)
- Step-by-step instructions for creating artifacts (plans, estimates, registers, maps)
- **Anti-Patterns section**: common LLM mistakes to avoid (e.g., ignoring ramp time, treating estimates as commitments, skipping spike phases)
- Further reading from authoritative sources

Commands chain multiple skills and suggest follow-ups.

## Key Principles

1. **Capacity is destiny**: Team size, not optimisation, determines output. Model capacity before committing
2. **Estimation reveals uncertainty**: Estimates are for planning and conversation, not prediction. Always include confidence bands and risks
3. **Technical debt is a business decision**: Debt exists because trade-offs were made. Measure its velocity impact, then decide if it's still worth keeping
4. **Dependencies drive timelines**: The critical path, not total work, determines delivery date. Manage it explicitly
5. **Velocity is for planning, not judgment**: Use it to forecast capacity, never to shame teams. Track estimates vs. actuals to improve

## Author

Seth Ford

## License

MIT
