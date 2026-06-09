---
name: helm-chart-builder
skill-id: "helm-chart-builder:helm-chart-builder"
plugin: Helm Chart Builder
category: Engineering
tags: [skill, engineering, kubernetes, helm, devops]
aliases: ["Helm", "Helm Charts", "K8s Charts"]
triggers:
  - helm chart
  - create helm chart
  - values.yaml
  - Chart.yaml
  - helm review
  - helm security audit
  - helm subchart
  - helm lint
  - helm test
  - kubernetes packaging
  - helm templates
  - _helpers.tpl
---

---
name: helm-chart-builder
description: "Helm chart development agent skill — chart scaffolding, values design, template patterns, dependency management, security hardening, and chart testing. Use when: user wants to create or improve Helm charts, design values.yaml files, implement template helpers, audit chart security (RBAC, network policies, pod security), manage subcharts, or run helm lint/test."
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: engineering
---

# Helm Chart Builder

Production-grade Helm charts. Sensible defaults. Secure by design.

## Slash Commands

| Command | What it does |
|---|---|
| `/helm:create` | Scaffold a production-ready chart |
| `/helm:review` | Analyse existing chart for issues |
| `/helm:security` | Audit for RBAC, network policies, secrets handling |

## When to Use

Any request involving: Helm chart, values.yaml, Chart.yaml, templates, _helpers.tpl, subcharts, helm lint/test, Kubernetes packaging.
