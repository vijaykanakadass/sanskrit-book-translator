# Changes

## Files created
- `server/app/services/digitize.py` — core digitization service (Sarvam API integration, background threads, adaptive polling, exponential backoff, ZIP→HTML extraction)
- `server/app/routers/jobs.py` — `GET /api/jobs/{job_id}` status endpoint
- `client/src/components/DigitizerProgress.jsx` — polling progress UI with elapsed timer
- `client/src/components/DigitizedViewer.jsx` — renders digitized HTML with page dividers

## Files modified
- `server/app/config.py` — added `SARVAM_API_KEY` setting
- `server/requirements.txt` — added `sarvamai`
- `server/app/routers/upload.py` — triggers digitization, returns `job_id`
- `server/app/main.py` — registered jobs router
- `client/src/lib/api.js` — added `getJobStatus(jobId)`
- `client/src/components/PdfUploader.jsx` — added `onJobStarted` callback, removed success state
- `client/src/pages/HomePage.jsx` — state flow: upload → digitizing → viewing → error
- `client/src/index.css` — added digitized page styles (`.page` dividers, `.page-header` labels)
- `.env.example` — added `SARVAM_API_KEY`
