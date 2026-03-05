# 004 — Landing Page with PDF Upload

## Context
First real user-facing feature: a polished landing page where users can upload a Sanskrit PDF. Server receives the file and prints metadata to the console. No auth, no translation — just the upload pipeline end-to-end.

## Approach
1. Create `client/src/lib/api.js` — API helper with `uploadPdf(file)`
2. Create `client/src/components/PdfUploader.jsx` — drag-and-drop + file picker, validates PDF/size, shows upload states
3. Rewrite `client/src/pages/HomePage.jsx` — nav bar, hero section, upload area, "how it works" steps
4. Create `server/app/routers/upload.py` — `POST /api/upload`, validates PDF, extracts page count with pdfplumber, prints to console
5. Register router in `server/app/main.py`

## Files created
- `client/src/lib/api.js`
- `client/src/components/PdfUploader.jsx`
- `server/app/routers/upload.py`

## Files modified
- `client/src/pages/HomePage.jsx` (rewrite)
- `server/app/main.py` (added router include)

## Outcome
Completed. Both servers start. Landing page renders with upload zone. Server prints PDF metadata on upload.
