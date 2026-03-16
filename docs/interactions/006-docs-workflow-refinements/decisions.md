# Decisions

## 1. Separate .env files for client and server

**Date:** 2026-03-05
**Status:** Accepted

### Context
The project initially had a single `.env.example` at the project root that mixed client-side and server-side environment variables together. This was problematic because:

- The client (React + Vite) and server (FastAPI + Python) are independent applications with their own runtimes, dependency management, and deployment concerns
- Vite requires client-side env vars to be prefixed with `VITE_` and reads them from the client directory by default
- Python's `dotenv` reads from the working directory (or an explicit path), which is the server directory
- Mixing them in one file creates confusion about which vars belong to which app, and risks accidentally exposing server secrets (like `SUPABASE_SERVICE_ROLE_KEY`) to the client bundle
- A developer working on just the client or just the server would need to see only the vars relevant to their app

### Decision
Split the single root `.env.example` into two separate files:

#### `client/.env.example`
Contains only Vite-compatible client-side variables:
- `VITE_SUPABASE_URL` — Supabase project URL (public, safe for client)
- `VITE_SUPABASE_ANON_KEY` — Supabase anonymous key (public, safe for client)

#### `server/.env.example`
Contains only server-side variables:
- `SUPABASE_URL` — Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY` — Supabase service role key (secret, server-only)
- `PORT` — Server port (defaults to 3001)
- `SARVAM_API_KEY` — Sarvam AI API key (secret, server-only)

Also updated `server/app/config.py` to use an explicit path for `load_dotenv`:
```python
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
```
This resolves to `server/.env` regardless of the current working directory.

### Alternatives Considered

#### Keep a single root .env.example
- Simpler (one file), but mixes concerns and creates confusion
- Risk of exposing server secrets to client via Vite's env processing
- Doesn't follow the convention of each app managing its own configuration

#### Use a monorepo tool (like dotenv-vault or direnv)
- Overkill for a two-app project
- Adds tooling complexity for minimal benefit

### Consequences
- Each app has clear ownership of its env vars
- `.gitignore` pattern `.env` already covers subdirectory `.env` files
- Developers (or AI) working on one app only see relevant configuration
- If someone has an existing root `.env`, they need to split it into `client/.env` and `server/.env` manually

---

## 2. Docs as single source of truth

**Date:** 2026-03-05
**Status:** Accepted

### Context
The user identified that plans and decisions were being saved as condensed summaries rather than full detailed records. The guiding principle is that the `docs/` folder should be detailed enough that the entire codebase could be re-created from docs alone — by a developer or AI who has never seen the code.

### Decision
- All plans must keep full implementation detail (architecture decisions, API shapes, component structure, data flow)
- All decisions must keep full context (options considered, reasons for acceptance/rejection, trade-offs, constraints)
- Never condense or summarize — the user can always summarize later with LLMs
- The raw detail is what's valuable for the repo history
- Paper Trail rule changed from "Summarize" to "Report" to avoid implying condensation

### Consequences
- Larger doc files, but more useful for reconstruction
- AI agents must include complete context when writing docs, not abbreviate
