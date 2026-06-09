---
name: security-application-security
skill-id: "security-application-security:security-application-security"
plugin: Security Application Security
category: Security
tags: [skill, security, SAST, DAST, dependency-scanning, penetration-testing]
aliases: ["Application Security", "SAST", "DAST", "Dependency Scanning", "Penetration Testing"]
triggers:
  - SAST configuration
  - DAST test plan
  - dependency vulnerability scan
  - security test plan
  - penetration test scope
  - API security review
  - web security headers
  - content security policy
  - scan dependencies
  - test application security
  - appsec review
  - bug scanning
  - how do I secure my application
  - find security vulnerabilities in my code
  - how to secure my API
  - my application has security vulnerabilities
  - how to prevent SQL injection XSS CSRF
  - security scan my application
  - how to do a security review
  - set up security testing in CI pipeline
  - vulnerability assessment for an app
  - how to handle security findings
  - application security review
  - how to test for common vulnerabilities
---

---
name: security-application-security
description: "SAST, DAST, dependency scanning, penetration test scoping, API security review."
license: MIT
metadata:
  version: 1.0.0
  author: Seth Ford
  category: security
---

# Application Security Plugin

Testing and scanning toolkit for application security including SAST, DAST, dependency scanning, API security, and web security headers.

## Skills

### 1. sast-configuration

Configure and deploy Static Application Security Testing (SAST) tools (SonarQube, Checkmarx, Semgrep) to find vulnerabilities in source code during development.

### 2. dast-test-plan

Design and execute Dynamic Application Security Testing (DAST) plans to find vulnerabilities in running applications including input validation, authentication, and logic flaws.

### 3. dependency-vulnerability-scan

Scan application dependencies for known vulnerabilities using SBOMs and vulnerability databases (NVD, GitHub Security Advisory, Snyk).

### 4. security-test-plan

Create comprehensive security testing plans covering functional security testing, security regression testing, and attack scenario validation.

### 5. penetration-test-scope

Define scope, rules of engagement, and success criteria for penetration testing engagements.

### 6. api-security-review

Review API design, authentication, rate limiting, input validation, and error handling for security best practices.

### 7. web-security-headers

Implement security headers (CSP, HSTS, X-Frame-Options, etc.) to mitigate browser-based attacks.

### 8. content-security-policy

Design and deploy Content Security Policy (CSP) headers to prevent XSS, clickjacking, and other injection attacks.

## Commands

### scan-dependencies

Scan application dependencies for known vulnerabilities and create remediation roadmap.

### test-security

Execute comprehensive security testing including SAST, DAST, and penetration testing.

### review-api-security

Audit API design, authentication, rate limiting, and input validation for security gaps.

## Quick Start

1. **Dependency security**: Use `scan-dependencies` to inventory and patch vulnerable dependencies
2. **Application security testing**: Use `test-security` to run SAST, DAST, and pen tests
3. **API security audit**: Use `review-api-security` to assess API security posture

## Plugin Info

- **Version**: 1.0.0
- **Author**: Seth Ford
- **License**: MIT
- **Keywords**: sast, dast, dependency-scanning, api-security, penetration-testing
