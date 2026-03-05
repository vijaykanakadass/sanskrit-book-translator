# Project: Sanskrit Book Translator

A web app to upload Sanskrit book PDFs and get beautifully formatted English translations.

## Tech Stack

- **Frontend:** React 19, Vite, JavaScript (JSX)
- **Backend:** FastAPI, Python
- **Database & Storage:** Supabase (PostgreSQL + file storage)
- **Styling:** Tailwind CSS v4
- **PDF Parsing:** pdfplumber (server-side, Python)

## Workflow Rules

**Guiding principle:** The `docs/` folder is the single source of truth. Plans and decisions must contain enough detail that the entire codebase could be re-created from `docs/` alone — by a developer (or AI) who has never seen the code. Every plan should describe *what* was built and *how*; every decision should explain *what* was chosen and *why*. When in doubt, include more detail, not less.

1. **Blueprint** — Plan before coding. Every change — feature, fix, or refactor — must start with a written plan.
2. **Archive** — Save plans to the repo. Write each plan to `docs/plans/` with a numbered, descriptive filename:
   - Format: `NNN-short-description.md` (e.g., `002-pdf-upload-endpoint.md`)
   - Number sequentially based on the last plan in the folder.
   - **Keep full detail** — save the complete plan as it was during implementation (architecture decisions, API shapes, component structure, data flow, etc.). Do not condense or summarize. The user can always summarize later with LLMs; the raw detail is what's valuable for the repo history.
3. **Spec** — Plan contents must include:
   - **Context** — why the change is needed
   - **Approach** — what will be done, step by step
   - **Files to modify/create** — list specific paths
   - **Verification** — how to test that it works
4. **Green Light** — Get approval before implementing. Present the plan and wait for user confirmation.
5. **Retrospective** — After implementation, update the plan with an `## Outcome` section noting what was actually done (if it differed from the plan).
6. **Decision Log** — Record every decision. Whenever the user makes a choice — tech stack, architecture, library, convention, trade-off — save it to `docs/decisions/` with the next sequential number.
   - Format: `NNN-short-title.md` (e.g., `006-use-redis-for-caching.md`)
   - Include: date, status, context, decision, and reasoning.
   - **Keep full detail** — record the complete context: what options were considered, why each was accepted or rejected, specific technical trade-offs, and any constraints that influenced the decision. Do not condense or summarize.
   - If a decision supersedes an older one, update the old file's status to `Superseded`.
7. **Changelog** — Record every change to the codebase in `docs/changelog/`, no matter how small. If a change doesn't warrant a full plan or decision, it still gets a changelog entry.
   - Format: `NNN-short-description.md` (e.g., `003-increase-upload-limit.md`)
   - Number sequentially based on the last entry in the folder.
   - Include: date, what changed, which files were affected, and why.
8. **Paper Trail** — Report docs changes at the end of every task. After completing any coding task, list:
   - Plans added or modified in `docs/plans/`
   - Decisions added or modified in `docs/decisions/`
   - Changelog entries added in `docs/changelog/`

## Code Conventions

- **Frontend: JavaScript only** — no TypeScript. The developer knows JS, not TS.
- **Frontend: ESM modules** — client uses `"type": "module"` with `import`/`export`.
- **Frontend: Functional React components** — no class components.
- **Frontend: Tailwind CSS** — use utility classes, avoid custom CSS unless necessary.
- **Backend: Python** — FastAPI with uvicorn. Keep code simple and readable.

## Folder Structure

```
client/              # React + Vite frontend
  src/
    components/      # Reusable UI components
    pages/           # Route-level page components
    lib/             # Supabase client, API helpers
server/              # FastAPI backend (Python)
  app/
    routers/         # API route modules
    services/        # Business logic (translation, PDF parsing)
    lib/             # Supabase admin client, shared utilities
docs/plans/          # Saved implementation plans
docs/decisions/      # Architecture & design decision records
docs/changelog/      # Log of every change made to the codebase
```
