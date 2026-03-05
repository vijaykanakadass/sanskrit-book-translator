# 002 — Add Decision Log

## Context
The developer wants every decision recorded in the repo so there's a traceable history of *why* things are the way they are. Follows the ADR (Architecture Decision Record) pattern.

## Approach
1. Create `docs/decisions/` with a README explaining the format
2. Backfill 5 decisions already made: tech stack, Supabase, JS over TS, Tailwind, agentic workflow
3. Add a decision-logging rule to `CLAUDE.md` so future sessions auto-record decisions
4. Update folder structure in `CLAUDE.md`

## Files created/modified
- `docs/decisions/README.md` (new)
- `docs/decisions/001` through `005` (new — backfilled)
- `CLAUDE.md` (modified — added rule 6, updated folder structure)

## Outcome
Completed. Decision log established with 5 backfilled records. CLAUDE.md updated with rule to auto-record future decisions.
