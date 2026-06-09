---
note-type: skill-quick-ref
generated: 2026-06-08
---

# Skill Quick Reference

Match intent to trigger, invoke with `Skill tool -> skill-id`.
Refresh: `python _scripts/build_skill_brain.py` | 201 skills indexed.

---

## Top 25 Skills

| skill-id | triggers | note |
|---|---|---|
| `docx` | `word doc` / `.docx` / `report` |  |
| `xlsx` | `spreadsheet` / `.xlsx` / `Excel` |  |
| `pptx` | `slides` / `deck` / `.pptx` |  |
| `pdf` | `PDF` / `.pdf` / `extract PDF` | create/extract/merge -- not interactive viewing |
| `pdf-viewer:view-pdf` | `view PDF` / `annotate PDF` / `sign PDF` | interactive viewer -- not text extraction |
| `data:analyze` | `data analysis` / `what drove` / `metric lookup` |  |
| `data:write-query` | `write SQL` / `SQL query` / `natural language to SQL` |  |
| `data:create-viz` | `chart` / `plot` / `graph` |  |
| `data:build-dashboard` | `HTML dashboard` / `KPI cards` / `shareable report` |  |
| `data:explore-data` | `profile data` / `null check` / `new dataset` | first-look profiling; use data:analyze for questions |
| `data:statistical-analysis` | `statistics` / `hypothesis test` / `A/B test` |  |
| `design:ux-copy` | `microcopy` / `error message` / `button text` |  |
| `design:design-critique` | `design feedback` / `review mockup` / `UX review` |  |
| `design:accessibility-review` | `a11y audit` / `WCAG` / `color contrast` |  |
| `operations:status-report` | `status report` / `project health` / `RAG status` |  |
| `operations:process-doc` | `SOP` / `RACI` / `document process` |  |
| `operations:runbook` | `runbook` / `on-call steps` / `deployment steps` |  |
| `pm-skills:jira-expert` | `Jira` / `JQL` / `sprint planning` |  |
| `pm-skills:scrum-master` | `scrum` / `velocity` / `retrospective` |  |
| `sales:account-research` | `research company` / `company intel` / `look up company` |  |
| `sales:draft-outreach` | `cold email` / `outreach email` / `reach out to` |  |
| `productivity:task-management` | `tasks` / `to do` / `what's on my plate` |  |
| `mcp-builder` | `build MCP` / `MCP server` / `FastMCP` |  |
| `ai-agents-architect` | `build agent` / `AI agent` / `autonomous agent` |  |
| `stop-slop` | `remove AI writing` / `AI slop` / `writing audit` |  |

---

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
| `pptx` vs `2slides-ppt-generator` | pptx = python-pptx local; 2slides = API-powered AI deck |

---

## All Skills by Category

*(Full trigger list in `skills-lookup.yaml`)*

**Anthropic**
- `2slides-ppt-generator` -- create presentation via API, 2slides, AI-powered slides
- `ai-agents-architect` -- build agent, AI agent, autonomous agent
- `algorithmic-art` -- generative art, algorithmic art, flow field
- `avoid-ai-writing` -- sounds like AI, AI writing patterns, remove AI tells
- `brand-guidelines` -- Anthropic brand, brand colors, brand fonts
- `business-analyst` -- KPI framework, business metrics, predictive model
- `canvas-design` -- poster, flyer, visual art
- `consolidate-memory` -- clean memory, merge memories, fix stale memory
- `design-system` -- brand setup, markdown HTML config, design tokens onboarding
- `doc-coauthoring` -- write documentation, co-author doc, technical spec
- `docx` -- word doc, .docx, Word document
- `figma-automation` -- Figma, design file, Figma MCP
- `internal-comms` -- internal update, 3P update, company newsletter
- `mcp-builder` -- build MCP, MCP server, Model Context Protocol
- `pdf` -- PDF, .pdf, extract PDF
- `pm-skills` -- Jira, Confluence, project management
- `pptx` -- slides, deck, presentation
- `schedule` -- schedule task, recurring task, every day
- `setup-cowork` -- set up Cowork, install plugins, configure Cowork
- `skill-creator` -- create skill, write skill, build skill
- `stop-slop` -- remove AI writing, AI writing patterns, slop
- `theme-factory` -- theme, style artifact, color scheme
- `web-artifacts-builder` -- React component, shadcn, Tailwind artifact
- `xlsx` -- Excel, spreadsheet, .xlsx

**Data**
- `data:analyze` -- data question, data analysis, metric lookup
- `data:build-dashboard` -- interactive dashboard, HTML dashboard, KPI cards
- `data:create-viz` -- chart, plot, graph
- `data:data-context-extractor` -- data context skill, warehouse schema, company data setup
- `data:data-visualization` -- data visualization best practice, chart type selection, matplotlib seaborn
- `data:explore-data` -- profile data, explore dataset, null check
- `data:sql-queries` -- SQL dialect, Snowflake SQL, BigQuery SQL
- `data:statistical-analysis` -- statistics, hypothesis test, p-value
- `data:validate-data` -- QA analysis, validate analysis, check methodology
- `data:write-query` -- write SQL, SQL query, translate to SQL

**Design**
- `design:accessibility-review` -- accessibility audit, WCAG, a11y
- `design:design-critique` -- design feedback, review mockup, critique design
- `design:design-handoff` -- dev handoff, spec sheet, design to code
- `design:design-system` -- audit design system, design tokens naming, component documentation
- `design:research-synthesis` -- synthesize research, interview themes, survey results
- `design:user-research` -- user research, interview guide, usability test
- `design:ux-copy` -- microcopy, error message, button text

**Operations**
- `operations:capacity-plan` -- capacity planning, resource capacity, utilisation
- `operations:change-request` -- change management, change record, CAB
- `operations:compliance-tracking` -- compliance, SOC 2, ISO 27001
- `operations:process-doc` -- document process, SOP, RACI
- `operations:process-optimization` -- improve process, streamline workflow, bottleneck
- `operations:risk-assessment` -- risk assessment, risk register, what could go wrong
- `operations:runbook` -- runbook, operational procedure, on-call steps
- `operations:status-report` -- status report, project health, KPI update
- `operations:vendor-review` -- vendor evaluation, vendor review, contract renewal

**Sales**
- `sales:account-research` -- research company, company intel, prospect research
- `sales:call-prep` -- prep for call, call preparation, meeting prep
- `sales:call-summary` -- call notes, call summary, meeting notes
- `sales:competitive-intelligence` -- competitive intel, battlecard, competitor research
- `sales:create-an-asset` -- sales asset, landing page, one-pager
- `sales:daily-briefing` -- morning briefing, daily brief, what's on my plate
- `sales:draft-outreach` -- cold email, outreach email, prospect email
- `sales:forecast` -- sales forecast, pipeline forecast, quota
- `sales:pipeline-review` -- pipeline review, deal health, pipeline health

**PM Skills**
- `pm-skills:atlassian-admin` -- Atlassian admin, Jira admin, user management
- `pm-skills:atlassian-templates` -- Confluence template, Jira template, blueprint
- `pm-skills:confluence-expert` -- Confluence, wiki, Confluence space
- `pm-skills:jira-expert` -- Jira, JQL, Jira project
- `pm-skills:meeting-analyzer` -- meeting transcript, analyze meeting, communication habits
- `pm-skills:scrum-master` -- sprint planning, velocity, retrospective
- `pm-skills:senior-pm` -- project management, PM, project plan
- `pm-skills:team-communications` -- internal communications, 3P update, weekly update

**Finance**
- `finance-skills:finance-skills` -- financial modelling, finance toolkit, ratio analysis overview
- `finance-skills:financial-analyst` -- financial analysis, DCF valuation, ratio analysis
- `finance-skills:saas-metrics-coach` -- SaaS metrics, ARR, MRR

**Productivity**
- `productivity:memory-management` -- manage memory, update memory, decode shorthand
- `productivity:start` -- start productivity, open dashboard, set up tasks
- `productivity:task-management` -- tasks, to do, task list
- `productivity:update` -- sync tasks, refresh memory, pull from project tracker

**Engineering**
- `caveman:caveman` -- caveman mode, less tokens, be brief
- `caveman:cs-caveman` -- /cs:caveman, activate caveman mode, persistent caveman
- `document-skills:frontend-design` -- build web component, landing page, React component
- `document-skills:slack-gif-creator` -- slack gif, animated gif, create gif for slack
- `document-skills:webapp-testing` -- test web app, playwright, browser automation
- `helm-chart-builder:helm-chart-builder` -- helm chart, create helm chart, values.yaml
- `inkscape:inkscape-mcp` -- inkscape, export svg, svg to png
- `slopmop:slopmop` -- slopmop, sm swab, sm scour
- `slopmop:sm-barnacle` -- sm barnacle, report tooling friction, file slopmop issue
- `slopmop:sm-buff` -- sm buff, PR CI results, review feedback triage
- `slopmop:sm-refit` -- sm refit, repository onboarding, one-time repo setup
- `slopmop:sm-sail` -- sm sail, auto-advance workflow, workflow loop
- `slopmop:sm-scour` -- sm scour, pre-PR sweep, comprehensive review before PR
- `slopmop:sm-swab` -- sm swab, fast iterative validation, development loop
- `superpowers-developing-for-claude-code:developing-claude-code-plugins` -- plugin development, create plugin, Claude Code plugin
- `superpowers-developing-for-claude-code:working-with-claude-code` -- Claude Code CLI, Claude Code features, MCP servers
- `superpowers:brainstorming` -- brainstorming, feature planning, design before coding
- `superpowers:dispatching-parallel-agents` -- parallel tasks, independent tasks, fan out agents
- `superpowers:executing-plans` -- execute plan, implement plan, carry out plan
- `superpowers:finishing-a-development-branch` -- merge branch, PR options, complete feature
- `superpowers:receiving-code-review` -- review feedback, implement review comments, code review feedback
- `superpowers:requesting-code-review` -- code review, review my code, PR review
- `superpowers:subagent-driven-development` -- subagent driven development, parallel implementation, multi-agent coding
- `superpowers:systematic-debugging` -- debugging, bug investigation, test failure
- `superpowers:test-driven-development` -- TDD, test-driven development, write tests first
- `superpowers:using-git-worktrees` -- git worktree, isolated workspace, feature branch isolation
- `superpowers:using-superpowers` -- which skill should I use, skill discovery, start conversation
- `superpowers:verification-before-completion` -- verify work, confirm tests pass, check before done
- `superpowers:writing-plans` -- write a plan, implementation plan, plan before coding
- `superpowers:writing-skills` -- create skill, write skill, author skill
- `workflow-builder:cs-workflow-build` -- /cs:workflow-build, cs workflow build command
- `workflow-builder:workflow-builder` -- design workflow, multi-agent workflow, Claude Code workflow
- `write-a-skill:cs-write-a-skill` -- /cs:write-a-skill, cs write a skill command, start new skill
- `write-a-skill:write-a-skill` -- create skill, write skill, author skill

**Obsidian**
- `defuddle` -- fetch URL clean, extract article, clean web page
- `json-canvas` -- canvas file, Obsidian canvas, mind map
- `obsidian-bases` -- Obsidian Base, .base file, database view
- `obsidian-cli` -- Obsidian vault, manage notes, vault search
- `obsidian-markdown` -- Obsidian note, wikilink, callout

**PDF Viewer**
- `pdf-viewer:view-pdf` -- open PDF, view PDF, annotate PDF

**Desktop Commander**
- `desktop-commander:desktop-commander-overview` -- Desktop Commander, persistent shell, REPL

**Plugin Management**
- `cowork-plugin-management:cowork-plugin-customizer` -- customize plugin, configure plugin, tailor plugin
- `cowork-plugin-management:create-cowork-plugin` -- create plugin, build plugin, new plugin

**Writing**
- `markdown-html-skills:cs-design-system` -- /cs:design-system, cs design system command, markdown HTML brand setup
- `markdown-html-skills:cs-grill-markdown-html` -- /cs:grill-markdown-html, grill markdown html, forcing questions for HTML
- `markdown-html-skills:cs-markdown-html` -- /cs:markdown-html, cs markdown html command, route markdown HTML
- `markdown-html-skills:cs-md-document` -- /cs:md-document, cs md document command
- `markdown-html-skills:cs-md-review` -- /cs:md-review, cs md review command
- `markdown-html-skills:cs-md-slides` -- /cs:md-slides, cs md slides command
- `markdown-html-skills:design-system` -- markdown HTML design system, brand for HTML, onboard markdown HTML
- `markdown-html-skills:markdown-html-orchestrator` -- convert markdown to HTML, markdown to HTML, interactive document
- `markdown-html-skills:md-document` -- long-form markdown document, spec to HTML, RFC to HTML
- `markdown-html-skills:md-review` -- PR writeup HTML, code review HTML, diff annotation
- `markdown-html-skills:md-slides` -- markdown slides, slide deck from markdown, presentation from markdown

**Executive Mentor**
- `executive-mentor:board-prep` -- board preparation, board meeting, investor update
- `executive-mentor:challenge` -- pre-mortem, challenge plan, find weaknesses
- `executive-mentor:executive-mentor` -- executive mentor, adversarial thinking partner, stress test plan
- `executive-mentor:hard-call` -- difficult decision, no good options, hard decision
- `executive-mentor:postmortem` -- post-mortem, postmortem, what went wrong
- `executive-mentor:stress-test` -- stress test, stress test assumptions, business assumption testing

**SharePoint SPFx**
- `spfx:ace` -- SPFx ACE, adaptive card extension, Viva Connections SPFx
- `spfx:deployment` -- SPFx deployment, deploy SPFx solution, SPFx app catalog
- `spfx:extensions` -- SPFx extension, application customizer, field customizer
- `spfx:graph` -- SPFx Microsoft Graph, MSGraphClientV3, msGraphClientFactory
- `spfx:property-pane` -- SPFx property pane, web part property pane, getPropertyPaneConfiguration
- `spfx:react-fluent-ui` -- SPFx React, Fluent UI SPFx, Office UI Fabric SPFx
- `spfx:rest-pnpjs` -- SPFx REST API, PnPjs SPFx, @pnp/sp
- `spfx:testing-debugging` -- SPFx testing, SPFx debugging, gulp serve SPFx
- `spfx:toolchain` -- scaffold SPFx project, create SPFx solution, set up SPFx environment
- `spfx:web-parts` -- SPFx web part, client-side web part, build web part

**Architect**
- `architect-communication:architect-communication` -- C4 diagram, architecture diagram, architecture RFC
- `architect-data-architecture:architect-data-architecture` -- design data architecture, data modeling, database selection
- `architect-decision-making:architect-decision-making` -- architecture decision record, ADR, technology radar
- `architect-governance:architect-governance` -- architecture governance, architecture principles, fitness functions
- `architect-infrastructure-design:architect-infrastructure-design` -- cloud architecture, infrastructure design, deployment topology
- `architect-quality-attributes:architect-quality-attributes` -- non-functional requirements, scalability analysis, reliability design
- `architect-system-design:architect-system-design` -- design system architecture, system decomposition, microservices patterns
- `architect-toolkit:architect-toolkit` -- architecture kata, architecture interview prep, architecture review facilitation

**Designer**
- `designer-interaction:designer-interaction` -- micro interaction spec, animation principles, state machine UI
- `designer-ops:designer-ops` -- design critique, handoff specification, design sprint planning
- `designer-prototyping-testing:designer-prototyping-testing` -- prototype strategy, usability test scenario, heuristic evaluation
- `designer-research:designer-research` -- user persona, empathy map, user journey map
- `designer-systems:designer-systems` -- design token, component specification, pattern library
- `designer-toolkit:designer-toolkit` -- design rationale, design presentation, design case study
- `designer-ui-design:designer-ui-design` -- layout grid, color system design, typography scale
- `designer-ux-strategy:designer-ux-strategy` -- competitive analysis UX, design principles, experience map

**Engineer**
- `engineer-api-development:engineer-api-development` -- REST API design, GraphQL schema design, gRPC service design
- `engineer-code-quality:engineer-code-quality` -- clean code review, refactoring, SOLID principles
- `engineer-database-engineering:engineer-database-engineering` -- schema design, query optimisation, slow query analysis
- `engineer-debugging:engineer-debugging` -- systematic debugging, root cause analysis, 5 whys
- `engineer-devops-practices:engineer-devops-practices` -- CI/CD pipeline, GitHub Actions pipeline, Dockerfile best practices
- `engineer-implementation-patterns:engineer-implementation-patterns` -- design patterns, Gang of Four patterns, data structure selection
- `engineer-testing:engineer-testing` -- TDD workflow, test driven development, write unit tests
- `engineer-toolkit:engineer-toolkit` -- technical writing, git workflow, code review checklist

**Product Manager**
- `pm-analytics:pm-analytics` -- metrics framework, north star metric, experiment design
- `pm-discovery:pm-discovery` -- product discovery, customer interview guide, opportunity assessment
- `pm-launch:pm-launch` -- launch plan, go to market strategy, beta program design
- `pm-prioritization:pm-prioritization` -- RICE scoring, prioritise backlog, impact effort matrix
- `pm-requirements:pm-requirements` -- write PRD, user story mapping, acceptance criteria
- `pm-stakeholder-management:pm-stakeholder-management` -- stakeholder map, executive summary, status update
- `pm-strategy:pm-strategy` -- product vision, product strategy, positioning statement
- `pm-toolkit:pm-toolkit` -- product review, retrospective facilitation, one-pager

**QA Engineer**
- `qa-accessibility-testing:qa-accessibility-testing` -- WCAG audit, screen reader testing, keyboard navigation testing
- `qa-api-testing:qa-api-testing` -- API test plan, contract testing QA, schema validation testing
- `qa-automation:qa-automation` -- automation architecture, test framework selection, page object model
- `qa-functional-testing:qa-functional-testing` -- test case design, exploratory testing charter, boundary value analysis
- `qa-performance-testing:qa-performance-testing` -- load test design, stress test plan, endurance test plan
- `qa-quality-metrics:qa-quality-metrics` -- defect analysis, quality dashboard, test metrics framework
- `qa-test-strategy:qa-test-strategy` -- test strategy design, risk based test plan, test coverage analysis
- `qa-toolkit:qa-toolkit` -- bug report template, test plan review, QA onboarding

**SDLC**
- `sdlc-cross-role:sdlc-cross-role` -- SDLC phase gate, definition of ready, definition of done

**Security**
- `security-application-security:security-application-security` -- SAST configuration, DAST test plan, dependency vulnerability scan
- `security-compliance:security-compliance` -- compliance mapping, security policy template, audit preparation
- `security-incident-response:security-incident-response` -- incident response plan, forensic analysis, incident communication
- `security-infrastructure:security-infrastructure` -- cloud security posture, network segmentation, container security review
- `security-operations:security-operations` -- SIEM rule design, detection engineering, vulnerability management program
- `security-secure-development:security-secure-development` -- secure coding review, OWASP Top 10, input validation patterns
- `security-threat-modeling:security-threat-modeling` -- threat modeling, STRIDE analysis, attack tree modeling
- `security-toolkit:security-toolkit` -- security champion program, security awareness training, secure architecture review

**Tech Lead**
- `tech-lead-code-review:tech-lead-code-review` -- code review standards, review culture, constructive feedback code review
- `tech-lead-cross-functional:tech-lead-cross-functional` -- technical product partnership, design engineering handoff, stakeholder communication tech lead
- `tech-lead-decision-making:tech-lead-decision-making` -- RFC process, write RFC, technology evaluation
- `tech-lead-engineering-excellence:tech-lead-engineering-excellence` -- coding standards, developer experience audit, tooling strategy
- `tech-lead-planning:tech-lead-planning` -- technical roadmap, capacity planning, sprint planning
- `tech-lead-process-engineering:tech-lead-process-engineering` -- development workflow, branching strategy, Git Flow trunk based
- `tech-lead-team-development:tech-lead-team-development` -- one on one template, mentoring plan, skill matrix
- `tech-lead-toolkit:tech-lead-toolkit` -- tech lead journal, team health check, retrospective facilitation tech lead

