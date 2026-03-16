# Plan

## Context
Setting up the greenfield project scaffolding — a monorepo with a React frontend and Express backend, connected to Supabase, with a placeholder for the translation service.

## Approach
1. Create `README.md` with project description, features checklist, tech stack, and setup instructions
2. Scaffold `client/` — React 19 + Vite + Tailwind CSS with routing and Supabase client
3. Scaffold `server/` — Express with health-check endpoint, Supabase admin client, and translation service placeholder
4. Add root-level files — `.gitignore`, `.env.example`
5. Install dependencies and verify both dev servers start

## Files created
- `README.md`
- `.gitignore`
- `.env.example`
- `client/package.json`, `client/vite.config.js`, `client/index.html`
- `client/src/main.jsx`, `client/src/App.jsx`, `client/src/index.css`
- `client/src/pages/HomePage.jsx`
- `client/src/lib/supabase.js`
- `server/package.json`
- `server/src/index.js`
- `server/src/lib/supabase.js`
- `server/src/services/translationService.js`

## Verification
- `cd client && npm run dev` — Vite starts, landing page renders
- `cd server && npm run dev` — Express starts, `GET /api/health` returns `{ status: "ok" }`
