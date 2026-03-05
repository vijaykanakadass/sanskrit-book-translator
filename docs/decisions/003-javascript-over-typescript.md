# 003 — JavaScript over TypeScript

**Date:** 2026-03-05
**Status:** Accepted

## Context
Project was initially scaffolded with TypeScript. Developer indicated to swich to JavaScript.

## Decision
Convert the entire project from TypeScript to plain JavaScript (`.js`/`.jsx`).

## Reasoning
The developer needs to read, understand, and modify the AI-generated code. TypeScript's type annotations, interfaces, and generics would add friction without helping someone who is more comfortable with Javscript than Typescript. JavaScript keeps the code approachable. Migration to TypeScript is always possible later if needed.
