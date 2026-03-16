# Changes

## Files created
- `client/.env.example` — `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`
- `server/.env.example` — `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `PORT`, `SARVAM_API_KEY`
- `docs/changelog/` folder with README and `001-increase-upload-limit-to-300mb.md`

## Files modified
- `server/app/config.py` — `load_dotenv` now uses explicit path to `server/.env`
- `client/src/components/PdfUploader.jsx` — `MAX_SIZE_MB` changed from `50` to `300`
- `CLAUDE.md` — multiple updates:
  - Added guiding principle ("docs/ is the single source of truth")
  - Added "Keep full detail" to Archive rule (plans)
  - Added "Keep full detail" to Decision Log rule
  - Changed Paper Trail from "Summarize" to "Report"
  - Added Changelog rule (rule 7) for `docs/changelog/`
  - Updated Paper Trail (now rule 8) to include changelog entries
  - Updated folder structure to include `docs/changelog/`

## Files deleted
- Root `.env.example` (replaced by per-app `.env.example` files)
