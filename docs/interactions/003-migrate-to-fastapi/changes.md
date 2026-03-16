# Changes

## Files deleted
- `server/package.json`, `server/src/index.js`, `server/src/lib/supabase.js`, `server/src/services/translationService.js` (entire Express server)

## Files created
- `server/requirements.txt`
- `server/app/__init__.py`, `server/app/main.py`, `server/app/config.py`
- `server/app/routers/__init__.py`
- `server/app/services/__init__.py`, `server/app/services/translation.py`
- `server/app/lib/__init__.py`, `server/app/lib/supabase.py`

## Files modified
- `.gitignore` — added `__pycache__/`, `*.pyc`, `venv/`, `*.egg-info/`
- `CLAUDE.md` — backend changed to FastAPI/Python, updated folder structure and code conventions
- `README.md` — updated tech stack table, prerequisites (Python 3.11+), setup instructions
