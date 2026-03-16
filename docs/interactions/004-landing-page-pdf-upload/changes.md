# Changes

## Files created
- `client/src/lib/api.js` — `uploadPdf(file)` function, POSTs FormData to `/api/upload`
- `client/src/components/PdfUploader.jsx` — drag-and-drop + click file picker, PDF validation, upload states (idle/dragging/uploading/success/error), max 50MB
- `server/app/routers/upload.py` — `POST /api/upload`, validates PDF, counts pages with pdfplumber, prints to console

## Files modified
- `client/src/pages/HomePage.jsx` — full rewrite: nav bar, hero section, PdfUploader component, "How it works" 3-step cards
- `server/app/main.py` — registered upload router
