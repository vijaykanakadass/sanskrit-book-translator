# Project: Sanskrit Book Translator

A web app to upload Sanskrit book PDFs and get beautifully formatted English translations.

## Tech Stack

- **Frontend:** React 19, Vite, JavaScript (JSX)
- **Backend:** FastAPI, Python
- **Database & Storage:** Supabase (PostgreSQL + file storage)
- **Styling:** Tailwind CSS v4
- **PDF Parsing:** pdfplumber (server-side, Python)

## Workflow Rules

1. **Blueprint** — Plan before coding. Every change — feature, fix, or refactor — must start with a written plan.
2. **Archive** — Save plans to the repo. Write each plan to `docs/plans/` with a numbered, descriptive filename:
   - Format: `NNN-short-description.md` (e.g., `002-pdf-upload-endpoint.md`)
   - Number sequentially based on the last plan in the folder.
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
   - If a decision supersedes an older one, update the old file's status to `Superseded`.
7. **Paper Trail** — Summarize docs changes at the end of every task. After completing any coding task, list:
   - Plans added or modified in `docs/plans/`
   - Decisions added or modified in `docs/decisions/`

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
```
