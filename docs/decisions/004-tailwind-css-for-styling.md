# 004 — Tailwind CSS for styling

**Date:** 2026-03-05
**Status:** Accepted

## Context
Needed a styling approach for the React frontend.

## Decision
Use Tailwind CSS v4 with the Vite plugin (`@tailwindcss/vite`).

## Reasoning
Tailwind's utility-first approach means styles live directly in the JSX — no separate CSS files to manage, no naming conventions to follow. It's fast to iterate with and works well with AI-generated code since styles are co-located with markup.
