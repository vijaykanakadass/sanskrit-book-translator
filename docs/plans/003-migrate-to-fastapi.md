# 003 — Migrate Server from Express (JS) to FastAPI (Python)

## Context
The app needs strong PDF parsing, OCR, and Sanskrit NLP capabilities. Python's ecosystem is significantly better for these tasks. Decision made to switch from Express/JS to FastAPI/Python.

## Approach
1. Delete entire Express `server/` directory
2. Create FastAPI server with: `main.py`, `config.py`, `routers/`, `services/translation.py`, `lib/supabase.py`
3. Install deps: `fastapi`, `uvicorn`, `python-dotenv`, `supabase`, `pdfplumber`, `python-multipart`
4. Update `.gitignore` with Python patterns
5. Update `CLAUDE.md` — tech stack, folder structure, code conventions
6. Update `README.md` — tech stack table, prerequisites, setup instructions
7. Supersede decision 001, create decision 006

## Files deleted
- `server/` (entire Express directory)

## Files created
- `server/requirements.txt`
- `server/app/__init__.py`, `main.py`, `config.py`
- `server/app/routers/__init__.py`
- `server/app/services/__init__.py`, `translation.py`
- `server/app/lib/__init__.py`, `supabase.py`

## Files modified
- `.gitignore`, `CLAUDE.md`, `README.md`

## Outcome
Completed. FastAPI server starts on port 3001, health check returns `{"status": "ok"}`. Client proxy unchanged — frontend still works.
