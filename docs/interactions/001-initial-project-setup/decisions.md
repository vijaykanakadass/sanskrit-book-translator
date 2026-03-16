# Decisions

## 1. React + Vite frontend, Express backend

**Date:** 2026-03-05
**Status:** Superseded (backend portion replaced by FastAPI in interaction 003)

### Context
Needed to choose a frontend framework and backend setup for the app. Options considered: Next.js (full-stack), React + Vite + Express (separate), SvelteKit.

### Decision
Use React + Vite for the frontend and Express for the backend, as two separate packages in a monorepo.

### Reasoning
The developer preferred a clear separation between frontend and backend rather than a full-stack framework. React + Vite gives fast dev experience with HMR, and Express is a familiar, minimal backend. This also keeps the architecture flexible — the frontend and backend can be deployed independently.

---

## 2. Supabase for database and storage

**Date:** 2026-03-05
**Status:** Accepted

### Context
Needed a database to store books and translations, and file storage for uploaded PDFs. Options considered: SQLite, PostgreSQL, MongoDB, Supabase.

### Decision
Use Supabase — a hosted PostgreSQL service that also provides file storage, auth, and real-time features.

### Reasoning
Developer chose Supabase. It bundles PostgreSQL + file storage + auth in one service with a generous free tier, reducing infrastructure setup. The client and admin SDKs (`@supabase/supabase-js`) are straightforward to use.

---

## 3. JavaScript over TypeScript

**Date:** 2026-03-05
**Status:** Accepted

### Context
Project was initially scaffolded with TypeScript. Developer indicated they only know JavaScript.

### Decision
Convert the entire project from TypeScript to plain JavaScript (`.js`/`.jsx`).

### Reasoning
The developer needs to read, understand, and modify the AI-generated code. TypeScript's type annotations, interfaces, and generics would add friction without helping someone who is more comfortable with JavaScript. JavaScript keeps the code approachable. Migration to TypeScript is always possible later if needed.

---

## 4. Tailwind CSS for styling

**Date:** 2026-03-05
**Status:** Accepted

### Context
Needed a styling approach for the React frontend.

### Decision
Use Tailwind CSS v4 with the Vite plugin (`@tailwindcss/vite`).

### Reasoning
Tailwind's utility-first approach means styles live directly in the JSX — no separate CSS files to manage, no naming conventions to follow. It's fast to iterate with and works well with AI-generated code since styles are co-located with markup.

---

## 5. Agentic AI development with human steering

**Date:** 2026-03-05
**Status:** Accepted

### Context
Needed to establish how the project would be developed.

### Decision
The project is built by an AI coding agent (Claude Code), with a human developer steering direction, reviewing decisions, and approving plans. Every code change follows a plan-first workflow:
1. Write a plan → save to docs
2. Get human approval
3. Implement
4. Record decisions

### Reasoning
This approach lets a developer who knows JavaScript but may not have deep architectural experience build an ambitious app by leveraging AI for implementation while retaining full control over direction. The plan-and-decision trail ensures nothing happens without understanding and approval.
