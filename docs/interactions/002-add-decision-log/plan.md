# Plan

## Context
The developer wants every decision recorded in the repo so there's a traceable history of *why* things are the way they are. Follows the ADR (Architecture Decision Record) pattern.

## Approach
1. Create `docs/decisions/` with a README explaining the format
2. Backfill 5 decisions already made: tech stack, Supabase, JS over TS, Tailwind, agentic workflow
3. Add a decision-logging rule to `CLAUDE.md` so future sessions auto-record decisions
4. Name all workflow rules so they can be referenced: Blueprint, Archive, Spec, Green Light, Retrospective, Decision Log, Paper Trail
5. Update folder structure in `CLAUDE.md`

## Files created/modified
- `docs/decisions/README.md` (new)
- `docs/decisions/001` through `005` (new — backfilled)
- `docs/plans/README.md` (new)
- `CLAUDE.md` (modified — added rules, named all rules, updated folder structure)

## Verification
- `docs/decisions/` has 5 backfilled records
- CLAUDE.md has named rules 1-7
- Each rule is referenceable by name
