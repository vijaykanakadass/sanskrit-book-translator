# 005 — Agentic AI development with human steering

**Date:** 2026-03-05
**Status:** Accepted

## Context
Needed to establish how the project would be developed.

## Decision
The project is built by an AI coding agent (Claude Code), with a human developer steering direction, reviewing decisions, and approving plans. Every code change follows a plan-first workflow:
1. Write a plan → save to `docs/plans/`
2. Get human approval
3. Implement
4. Record decisions in `docs/decisions/`

## Reasoning
This approach lets a developer who knows JavaScript but may not have deep architectural experience build an ambitious app by leveraging AI for implementation while retaining full control over direction. The plan-and-decision trail ensures nothing happens without understanding and approval.
