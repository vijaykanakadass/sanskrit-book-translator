# Plan

## Context
First real user-facing feature: a polished landing page where users can upload a Sanskrit PDF. Server receives the file and prints metadata to the console. No auth, no translation — just the upload pipeline end-to-end.

## Approach
1. Create `client/src/lib/api.js` — API helper with `uploadPdf(file)` that POSTs to `/api/upload` with FormData
2. Create `client/src/components/PdfUploader.jsx` — drag-and-drop + click file picker, validates PDF type and size (max 50MB), shows upload states (idle/dragging/uploading/success/error)
3. Rewrite `client/src/pages/HomePage.jsx` — nav bar ("Sanskrit Translator"), hero section with heading + subtext, upload area, "how it works" 3-step cards
4. Create `server/app/routers/upload.py` — `POST /api/upload`, validates PDF content type, extracts page count with pdfplumber, prints metadata to console, returns `{ filename, size, pages }`
5. Register router in `server/app/main.py`

## Files created
- `client/src/lib/api.js`
- `client/src/components/PdfUploader.jsx`
- `server/app/routers/upload.py`

## Files modified
- `client/src/pages/HomePage.jsx` (full rewrite)
- `server/app/main.py` (added router include)

## Verification
- Both servers start
- Landing page renders with upload zone
- Upload a PDF → server prints metadata, frontend shows success
- Upload non-PDF → error shown
