---
name: engineer-debugging
skill-id: "engineer-debugging:engineer-debugging"
plugin: Engineer Debugging
category: Engineer
tags: [skill, engineer, debugging, root-cause-analysis, postmortem, concurrency]
aliases: ["Debugging", "Root Cause Analysis", "Postmortem", "Memory Leak Detection"]
triggers:
  - systematic debugging
  - root cause analysis
  - 5 whys
  - memory leak detection
  - concurrency debugging
  - race condition
  - deadlock debugging
  - performance profiling
  - write postmortem
  - log analysis
  - binary search debugging
  - git bisect
  - how do I find this bug
  - I cannot reproduce this bug
  - debugging methodology
  - how to debug production issues
  - analyse crash logs
  - memory leak in production
  - threads are deadlocking
  - how to investigate a production incident
  - how to write a postmortem for an outage
  - how to profile my application
  - bug is intermittent and hard to find
  - my system keeps crashing
---

---
name: engineer-debugging
description: "Systematic debugging, root cause analysis, memory leaks, concurrency, postmortems."
license: MIT
metadata:
  version: 1.0.0
  author: Seth Ford
  category: engineer
---

# Debugging Plugin

Systematic approaches to identifying and fixing bugs through systematic debugging, root cause analysis, and postmortem analysis.

## Skills

1. **systematic-debugging** - Step-by-step debugging methodology, hypothesis testing
2. **root-cause-analysis** - 5 Whys, fishbone diagrams, core cause identification
3. **log-analysis** - Parsing logs, correlation analysis, timeline reconstruction
4. **memory-leak-detection** - Heap dumps, retention analysis, reference tracing
5. **concurrency-debugging** - Race conditions, deadlocks, thread analysis
6. **performance-profiling** - CPU/memory profiling, bottleneck identification
7. **binary-search-debugging** - Isolating failure with bisect, git bisect
8. **postmortem-analysis** - RCA writing, timeline documentation, action items

## Commands

1. **debug-issue** - Systematic debugging combining log analysis and profiling
2. **analyze-failure** - Root cause analysis with 5 Whys and fishbone
3. **write-postmortem** - Postmortem document with timeline and prevention

## Standards Reference

- Robert C. Martin, _The Clean Coder_, Chapter 8 (Debugging)
- Debugging Handbook by GDB developers
- Site Reliability Engineering (SRE) postmortem template (Google)
