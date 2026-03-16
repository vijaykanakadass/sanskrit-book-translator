# Changes

## Files created
- `README.md` — project description, WIP checklist, tech stack, "Built by AI, steered by humans" callout
- `.gitignore` — node_modules, dist, .env, Python patterns
- `.env.example` — Supabase + server config placeholders
- `client/package.json`, `client/vite.config.js`, `client/index.html`
- `client/src/main.jsx`, `client/src/App.jsx`, `client/src/index.css`
- `client/src/pages/HomePage.jsx` — placeholder landing page
- `client/src/lib/supabase.js` — Supabase client initialized from VITE_ env vars
- `server/package.json`, `server/src/index.js` — Express server with health check
- `server/src/lib/supabase.js` — Supabase admin client
- `server/src/services/translationService.js` — placeholder for future translation logic
- `CLAUDE.md` — project instructions for Claude Code (tech stack, workflow rules, folder structure)

## Notes
- Originally scaffolded with TypeScript, then converted to JavaScript per developer preference
- Vite proxy configured: `/api` → `http://localhost:3001`
