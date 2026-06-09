---
name: security-secure-development
skill-id: "security-secure-development:security-secure-development"
plugin: Security Secure Development
category: Security
tags: [skill, security, OWASP, secure-coding, authentication, cryptography]
aliases: ["Secure Development", "OWASP Top 10", "Secure Coding Review", "Authentication Design"]
triggers:
  - secure coding review
  - OWASP Top 10
  - input validation patterns
  - output encoding
  - authentication design
  - authorisation design
  - session management
  - cryptography selection
  - secrets management
  - review security code
  - audit auth
  - check OWASP
  - how do I write secure code
  - how to prevent OWASP vulnerabilities
  - how to handle passwords securely
  - how to implement authentication securely
  - how to prevent injection attacks
  - secure my login system
  - how to store secrets and credentials
  - how to implement role-based authorisation
  - how to handle user sessions securely
  - how to avoid security vulnerabilities in code
  - secure coding training for developers
  - review my auth implementation
---

---
name: security-secure-development
description: "Secure coding review, OWASP Top 10, authentication/authorisation design, cryptography."
license: MIT
metadata:
  version: 1.0.0
  author: Seth Ford
  category: security
---

# Secure Development Plugin

Comprehensive secure development toolkit covering OWASP Top 10, secure coding, input validation, authentication, authorisation, cryptography, and secrets management.

## Skills

### 1. secure-coding-review

Review code for security vulnerabilities using OWASP guidelines and secure coding patterns. Focus on privileged code (auth, input handling, crypto).

### 2. owasp-top-ten-check

Audit applications against OWASP Top 10 (2021) risks, from broken access control to insufficient logging.

### 3. input-validation-patterns

Design and implement input validation using whitelisting, boundary checks, and type validation to prevent injection attacks.

### 4. output-encoding

Implement context-specific output encoding (HTML, URL, JavaScript, CSS) to prevent XSS attacks.

### 5. authentication-design

Design secure authentication systems with strong password policies, MFA, secure password reset, and session management.

### 6. authorization-design

Design fine-grained authorisation systems using least privilege and role-based or capability-based access control.

### 7. session-management

Implement secure session handling with proper token generation, storage, expiry, and CSRF protection.

### 8. cryptography-selection

Select appropriate cryptographic algorithms and parameters for encryption, hashing, key derivation, and digital signatures.

### 9. secrets-management

Manage API keys, credentials, and secrets securely using vaults, environment variables, and rotation policies.

## Commands

### review-security

Conduct comprehensive security code review examining OWASP Top 10, secure coding patterns, input validation, and cryptography.

### audit-auth

Audit authentication and authorisation implementation for compliance with secure design principles.

### check-owasp

Check application against OWASP Top 10 and identify gaps in critical security controls.

## Quick Start

1. **New application security review**: Use `review-security` with your codebase
2. **Auth implementation audit**: Use `audit-auth` to verify secure authentication and authorisation
3. **Compliance check**: Use `check-owasp` to assess OWASP Top 10 compliance
4. **Code review guidance**: Use individual skills for specific concerns (input validation, secrets, etc.)

## Plugin Info

- **Version**: 1.0.0
- **Author**: Seth Ford
- **License**: MIT
- **Keywords**: secure-coding, OWASP, authentication, cryptography, secrets
