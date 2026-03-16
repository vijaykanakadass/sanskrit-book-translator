# Plan

## Context
The three independent doc folders (`plans/`, `decisions/`, `changelog/`) have separate numbering sequences that make it impossible to retrace the chronological flow of the project. Instead of adding a cross-referencing layer on top, restructure `docs/` around the natural unit of work: an **interaction** — a single task or action requested by the user, from request through to outcome.

## Approach

### 1. Create `docs/interactions/` and backfill existing history
Migrate the 16 existing entries (5 plans + 10 decisions + 1 changelog) into 6 interaction folders based on the actual project history:

- `001-initial-project-setup/` — scaffold monorepo (plan 001, decisions 001-005)
- `002-add-decision-log/` — establish docs workflow (plan 002)
- `003-migrate-to-fastapi/` — switch from Express to FastAPI (plan 003, decision 006)
- `004-landing-page-pdf-upload/` — landing page with PDF upload (plan 004)
- `005-pdf-digitization/` — digitize PDFs via Sarvam API (plan 005, decisions 007-009)
- `006-docs-workflow-refinements/` — env split, upload limit, CLAUDE.md updates (decision 010, changelog 001)

Each folder gets the appropriate subset of files: request.md, plan.md, decisions.md, changes.md, outcome.md.

### 2. Remove old folders
Delete `docs/plans/`, `docs/decisions/`, `docs/changelog/` and their READMEs.

### 3. Update `CLAUDE.md`
Replace the 8 workflow rules with 9 rules adapted to the interaction model:
1. Interaction folder — create numbered folder for every task
2. Request — save what the user asked
3. Blueprint — plan before coding
4. Plan detail — keep full detail
5. Green Light — get approval
6. Decisions — record choices in the interaction folder
7. Changes — record file changes
8. Outcome — write what was built
9. Paper Trail — report which interaction was created/updated

### 4. Create `docs/interactions/README.md`
Brief explanation of the structure and conventions.

## Files created
- `docs/interactions/README.md`
- 6 interaction folders (001-006) with ~25 total files

## Files modified
- `CLAUDE.md` — replaced workflow rules and folder structure

## Files deleted
- `docs/plans/` (5 plans + README)
- `docs/decisions/` (10 decisions + README)
- `docs/changelog/` (1 entry + README)

## Verification
1. Read interaction folders 001 through 006 in order — tells the full project story
2. Each interaction folder is self-contained
3. CLAUDE.md reflects the new workflow rules
4. No orphaned references to old folder paths
