# 001 — React + Vite frontend, Express backend

**Date:** 2026-03-05
**Status:** Superseded by [006-python-fastapi-backend.md](006-python-fastapi-backend.md)

## Context
Needed to choose a frontend framework and backend setup for the app. Options considered: Next.js (full-stack), React + Vite + Express (separate), SvelteKit.

## Decision
Use React + Vite for the frontend and Express for the backend, as two separate packages in a monorepo.

## Reasoning
The developer preferred a clear separation between frontend and backend rather than a full-stack framework. React + Vite gives fast dev experience with HMR, and Express is a familiar, minimal backend. This also keeps the architecture flexible — the frontend and backend can be deployed independently.
