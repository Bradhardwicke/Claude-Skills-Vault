---
name: spfx-toolchain-scaffolding
skill-id: "spfx:toolchain"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, toolchain, scaffolding]
aliases: ["SPFx Setup", "SPFx Generator", "SPFx Yeoman", "SPFx Gulp", "SPFx Heft"]
triggers:
  - scaffold SPFx project
  - create SPFx solution
  - set up SPFx environment
  - SPFx toolchain
  - Yeoman SharePoint generator
  - yo sharepoint
  - SPFx Node version
  - gulp SPFx
  - SPFx Heft build
  - nvm SPFx
  - SPFx project structure
  - install SPFx generator
  - SPFx development environment
---

# SPFx Toolchain and Scaffolding

## Version Reference (current: SPFx 1.22)

| SPFx Version | Node.js | Build Tool | TypeScript |
|---|---|---|---|
| 1.22+ | 18 LTS or 22 LTS | Heft (default) or Gulp | 5.x |
| 1.18–1.21 | 18 LTS | Gulp | 4.7 |
| 1.16–1.17 | 16 LTS | Gulp | 4.5 |
| 1.14–1.15 | 14 LTS | Gulp | 4.x |

Use `nvm` to switch Node versions between projects.

## Global Prerequisites

```bash
npm install gulp-cli yo @microsoft/generator-sharepoint --global
```

## Scaffold a New Project

```bash
yo @microsoft/sharepoint
```

Prompts: solution name, location, tenant-wide deployment, component type (web part / extension / ACE), component name, framework (React / No JS framework).

## Key Project Files

```
{solution}/
├── config/
│   ├── package-solution.json   ← solution metadata, permissions, tenant deploy
│   ├── serve.json              ← local workbench config
│   └── deploy-azure-storage.json
├── src/
│   └── webparts/{name}/        ← component source
├── sharepoint/solution/        ← .sppkg built here
└── package.json
```

## SPFx 1.22 — Heft vs Gulp

- New projects default to **Heft** (RushStack build orchestrator)
- Legacy Gulp option: `yo @microsoft/sharepoint --skip-feature-deployment` then choose gulp at prompt
- Existing gulp projects continue working on 1.22 without changes
- `gulp serve` still works on gulp projects; Heft projects use `heft start`

## Common Commands (Gulp projects)

```bash
gulp serve                # local workbench + browser
gulp serve --nobrowser    # serve without opening browser
gulp bundle               # compile
gulp bundle --ship        # production build
gulp package-solution     # creates .sppkg
gulp package-solution --ship  # production package
gulp clean                # clean build artifacts
```

## Common Commands (Heft projects — SPFx 1.22+)

```bash
heft start                # serve / watch
heft build                # compile
heft build --production   # production build
gulp package-solution --ship  # packaging still uses gulp task
```

## Upgrade Existing Project

```bash
npm install -g @microsoft/sp-upgrade-action
spfx project upgrade --output md   # generates upgrade report
```

## CI/CD (Azure DevOps)

Use Node tool installer task to pin Node version. Bundle and package with `--ship`, then deploy `.sppkg` via `m365 spo app add` (CLI for Microsoft 365).
