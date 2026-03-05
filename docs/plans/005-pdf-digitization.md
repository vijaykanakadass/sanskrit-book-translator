# 005 — PDF Digitization via Sarvam Document Intelligence

## Context
After uploading a PDF, digitize it using the Sarvam Document Intelligence API and display the digitized content to the user. No translation at this stage — just OCR/digitization and display. The user stays on the same page and sees progress during the async processing.

## Architecture
The Sarvam API is async (create job → upload → start → poll → download), so:
- `POST /api/upload` uploads PDF, submits to Sarvam, returns a `job_id`
- `GET /api/jobs/{job_id}` returns status (processing/completed/failed) + result when done
- Frontend polls the status endpoint and renders digitized HTML when ready
- Jobs stored in-memory dict (no DB needed yet)

## Approach

### 1. Server: Add `SARVAM_API_KEY` to config
- Update `server/app/config.py` to read `SARVAM_API_KEY` from env
- Update `.env.example` with `SARVAM_API_KEY` placeholder
- Add `sarvamai` to `requirements.txt`

### 2. Server: Create `server/app/services/digitize.py`
Digitization service ported from reference `D:\WebApps\DocumentTranslation\digitize.py`:
- In-memory job store (`jobs = {}`) protected by `threading.Lock`
- `create_job(filename, pages)` — creates job entry with uuid, returns `job_id`
- `get_job(job_id)` — thread-safe read (returns copy)
- `update_job(job_id, **kwargs)` — thread-safe update
- `start_digitization(job_id, pdf_bytes)` — launches `run_digitization` in a daemon thread
- `run_digitization(job_id, pdf_bytes)` — background task:
  1. Save PDF to temp file
  2. Create Sarvam Document Intelligence job (`language="sa-IN"`, `output_format="html"`)
  3. Upload file to job
  4. Start job
  5. Poll with adaptive intervals (5s for <10 pages or <30s elapsed, 10s for <300s, 15s after) until complete
  6. Download ZIP output, extract per-page HTML
  7. Merge into single HTML string with page dividers
  8. Store result in jobs dict
- Exponential backoff on rate limit errors: `min(2 ** (attempt + 2), 60)` → 4s, 8s, 16s, 32s, capped at 60s, max 5 retries
- Job status progression: `uploading → processing → completed/failed`
- `extract_html_from_zip(zip_bytes)` — opens ZIP, sorts HTML files, strips HTML/HEAD/BODY wrappers, wraps each in `<div class="page" id="page-N">` with a page header

### 3. Server: Modify `server/app/routers/upload.py`
- Import `create_job`, `start_digitization` from digitize service
- After PDF validation + page count, call `create_job(filename, pages)` and `start_digitization(job_id, contents)`
- Return `{ job_id, filename, size, pages, status: "processing" }` immediately (no longer just prints to console)

### 4. Server: Create `server/app/routers/jobs.py`
- `GET /api/jobs/{job_id}` — calls `get_job(job_id)`, returns 404 if not found, otherwise returns full job dict:
  ```json
  { "job_id": "...", "filename": "...", "pages": 5, "status": "processing|completed|failed", "detail": "...", "html": "...", "error": "..." }
  ```
- Register in `main.py` via `app.include_router(jobs.router)`

### 5. Client: Update `client/src/lib/api.js`
- Add `getJobStatus(jobId)` — fetches `GET /api/jobs/${jobId}`, throws on error, returns JSON

### 6. Client: Create `client/src/components/DigitizerProgress.jsx`
- Props: `jobId`, `filename`, `pages`, `onComplete(html)`, `onError(msg)`
- Shows spinner, filename, page count, status detail text, elapsed timer
- Polls `getJobStatus` every 3 seconds via `useEffect` with cancellation
- Elapsed timer updates every 1 second via separate `setInterval`
- On `status === "completed"` → calls `onComplete(job.html)`
- On `status === "failed"` → calls `onError(job.error)`
- On fetch error → calls `onError("Lost connection to server")`

### 7. Client: Create `client/src/components/DigitizedViewer.jsx`
- Props: `html`, `filename`, `onReset`
- Header bar with filename and "Upload another" button
- Renders digitized HTML via `dangerouslySetInnerHTML` in a styled container with class `digitized-content`
- CSS in `index.css` styles `.page` dividers and `.page-header` labels (amber color scheme)

### 8. Client: Update `client/src/components/PdfUploader.jsx`
- Accept `onJobStarted` prop
- After successful upload, if response contains `job_id`, call `onJobStarted(data)` to notify parent
- Removed the success/green confirmation state (parent handles transition now)

### 9. Client: Update `client/src/pages/HomePage.jsx`
- Manage state flow with `phase` state: `"upload" | "digitizing" | "viewing" | "error"`
- `jobInfo` state stores upload response (job_id, filename, pages)
- `html` state stores digitized HTML result
- Phase transitions:
  - `upload` → shows `PdfUploader` with `onJobStarted` callback
  - `digitizing` → shows `DigitizerProgress` with `onComplete`/`onError` callbacks
  - `viewing` → shows `DigitizedViewer` (full-width, replaces hero section)
  - `error` → shows error card with "Try again" button that calls `reset()`
- "How it works" steps only shown during upload phase
- Steps text updated from "AI Translates" to "AI Digitizes" to match current stage

### 10. Client: Add digitized page styles to `client/src/index.css`
- `.digitized-content .page` — bottom margin, padding, amber border divider between pages
- `.digitized-content .page:last-child` — no divider on last page
- `.digitized-content .page-header` — small uppercase amber label with bottom border

## Files created
- `server/app/services/digitize.py`
- `server/app/routers/jobs.py`
- `client/src/components/DigitizerProgress.jsx`
- `client/src/components/DigitizedViewer.jsx`

## Files modified
- `server/app/config.py` (added SARVAM_API_KEY)
- `server/requirements.txt` (added sarvamai)
- `server/app/routers/upload.py` (triggers digitization, returns job_id)
- `server/app/main.py` (registered jobs router)
- `client/src/lib/api.js` (added getJobStatus)
- `client/src/components/PdfUploader.jsx` (added onJobStarted callback, removed success state)
- `client/src/pages/HomePage.jsx` (state flow: upload → digitizing → viewing)
- `client/src/index.css` (added digitized page styles)
- `.env.example` (added SARVAM_API_KEY)

## Verification
1. Add `SARVAM_API_KEY` to `.env`
2. Start both servers
3. Upload a Sanskrit PDF → see "Digitizing..." progress with elapsed timer
4. Wait for completion → digitized HTML renders on screen with page dividers
5. Server console shows Sarvam API calls and job status transitions

## Outcome
Completed. Client builds clean. Server imports clean. Upload triggers async Sarvam digitization, frontend polls for status and renders digitized HTML when complete.
