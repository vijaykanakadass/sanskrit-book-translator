# Plan

## Context
The app needs strong PDF parsing, OCR, and Sanskrit NLP capabilities. Python's ecosystem is significantly better for these tasks. Decision made to switch from Express/JS to FastAPI/Python.

## Approach
1. Delete entire Express `server/` directory
2. Create FastAPI server with: `main.py`, `config.py`, `routers/`, `services/translation.py`, `lib/supabase.py`
3. Install deps: `fastapi`, `uvicorn`, `python-dotenv`, `supabase`, `pdfplumber`, `python-multipart`
4. Update `.gitignore` with Python patterns (`__pycache__/`, `*.pyc`, `venv/`, `*.egg-info/`)
5. Update `CLAUDE.md` — tech stack, folder structure, code conventions
6. Update `README.md` — tech stack table, prerequisites, setup instructions
7. Supersede decision 001, create decision 006

## Files deleted
- `server/` (entire Express directory — `package.json`, `src/index.js`, `src/lib/supabase.js`, `src/services/translationService.js`)

## Files created
- `server/requirements.txt` — fastapi, uvicorn[standard], python-dotenv, supabase, pdfplumber, python-multipart
- `server/app/__init__.py`, `server/app/main.py` — FastAPI app with CORS, health check
- `server/app/config.py` — Settings class reading from env vars
- `server/app/routers/__init__.py`
- `server/app/services/__init__.py`, `server/app/services/translation.py` — placeholder
- `server/app/lib/__init__.py`, `server/app/lib/supabase.py` — Supabase admin client

## Files modified
- `.gitignore` — added Python patterns
- `CLAUDE.md` — backend: FastAPI/Python, updated folder structure, code conventions
- `README.md` — updated tech stack, prerequisites (Python 3.11+), setup instructions

## Verification
- `cd server && pip install -r requirements.txt && uvicorn app.main:app --port 3001` → starts, health check works
- Client proxy unchanged — frontend still works with `/api` → `localhost:3001`
