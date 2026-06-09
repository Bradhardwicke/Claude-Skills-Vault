---
name: architect-system-design
skill-id: "architect-system-design:architect-system-design"
plugin: Architect System Design
category: Architect
tags: [skill, architect, system-design, microservices, distributed-systems]
aliases: ["System Design", "Architecture Patterns", "Distributed Systems Design"]
triggers:
  - design system architecture
  - system decomposition
  - microservices patterns
  - break apart monolith
  - domain driven design
  - event driven architecture
  - CQRS design
  - API gateway design
  - service mesh
  - caching strategy
  - data partitioning
  - design new system from scratch
  - monolith migration
  - how do I structure my services
  - help designing a microservices architecture
  - how to split a large application
  - how do I design a distributed system
  - what architecture pattern should I use
  - DDD bounded contexts
  - how to migrate from a monolith
  - design a new system from scratch
  - system architecture interview prep
  - design for loose coupling
  - event sourcing vs traditional storage
  - how to design an event-driven system
  - TOGAF
  - enterprise architecture framework
  - TOGAF ADM
  - TOGAF phase
  - TOGAF application architecture
---

---
name: architect-system-design
description: "Architecture patterns, system decomposition, DDD, microservices, event-driven, CQRS. Grounded in TOGAF, IASA BTABoK, ISO 42010."
license: MIT
metadata:
  version: 1.0.0
  author: Seth Ford
  category: architect
---

# System Design Plugin

Master architecture patterns, system decomposition, and distributed systems design for building resilient, scalable systems.

## Skills

### Core Architecture

- **system-decomposition** — Break systems into bounded contexts and independent services using DDD principles
- **domain-driven-design** — Model business domains explicitly, design aggregates, establish ubiquitous language
- **microservices-patterns** — Apply saga, circuit breaker, bulkhead, and eventual consistency patterns

### Assessment & Evolution

- **monolith-assessment** — Evaluate whether to split, refactor, or optimise monolithic systems
- **event-driven-architecture** — Design loosely-coupled systems using event pub-sub and event sourcing

### Advanced Patterns

- **cqrs-design** — Separate command and query models for complex domains
- **api-gateway-design** — Design robust API gateways with routing, auth, rate limiting, and aggregation
- **service-mesh-patterns** — Implement service mesh for observability, resilience, and traffic management

### Scaling & Performance

- **data-partitioning** — Shard and partition data for horizontal scaling
- **caching-strategy** — Design multi-layer caching to reduce latency and database load

## Commands

### architect-system

Design complete system architecture from requirements. Combines system-decomposition, domain-driven-design, microservices-patterns to produce C4 diagrams, bounded contexts, and integration specifications.

**Usage**: `architect-system [problem statement]`

### decompose-monolith

Assess monolith and plan migration to services. Uses monolith-assessment, system-decomposition, event-driven-architecture to provide step-by-step extraction roadmap.

**Usage**: `decompose-monolith [monolith description]`

### design-api

Create API gateway and service contract specifications. Applies api-gateway-design, cqrs-design, microservices-patterns to design scalable APIs.

**Usage**: `design-api [backend services]`

### evaluate-architecture

Audit existing architecture for resilience and scalability. Assesses caching-strategy, data-partitioning, service-mesh-patterns and produces recommendations.

**Usage**: `evaluate-architecture [current system]`

## When to Use This Plugin

- Starting a new system from scratch
- Refactoring or breaking apart a monolith
- Scaling system beyond single database or service limits
- Designing service-to-service communication
- Optimising latency and throughput
- Managing distributed system complexity
