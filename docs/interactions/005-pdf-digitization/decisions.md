# Decisions

## 1. Sarvam AI for translation and digitization

**Date:** 2026-03-05
**Status:** Accepted

### Context
Needed to choose a translation service for Sanskrit-to-English translation. The developer has an existing Sarvam AI integration from a prior video translation project (`D:\AI_ML\VideoTranslation_Sarvam`) with working scripts.

### Decision
Use Sarvam AI as the translation and digitization service:
- **Document Intelligence:** Sarvam's async job-based API for PDF OCR/digitization
- **Text translation:** `mayura:v1` model via `client.text.translate()`
- **LLM refinement:** `sarvam-m` model via `client.chat.completions()` for quality correction
- **Python SDK:** `sarvamai` package
- **Source language:** `sa-IN` (Sanskrit), **Target:** `en-IN` (English)

### Reasoning
- Developer already has a working Sarvam AI subscription and API key
- Proven scripts exist for Sanskrit text translation with chunking and rate limiting
- Sarvam supports Sanskrit (`sa-IN`) as a source language natively
- The `mayura:v1` model handles formal/colloquial translation modes
- LLM-based quality correction (formal → colloquial refinement) is already proven in the reference scripts

### Reference scripts (read-only, not to be modified)
- `D:\AI_ML\VideoTranslation_Sarvam\translate_text.py` — plain text translation with chunking
- `D:\AI_ML\VideoTranslation_Sarvam\correct_srt.py` — LLM-based quality correction
- `D:\AI_ML\VideoTranslation_Sarvam\sanskrit_learn_module.html` — interactive web view template

---

## 2. Reference projects identified for pattern reuse

**Date:** 2026-03-05
**Status:** Accepted

### Context
Needed proven patterns for translation, PDF processing, and bilingual presentation rather than building everything from scratch.

### Decision
Two external reference projects (read-only, not to be modified) will be used as pattern sources:

#### `D:\AI_ML\VideoTranslation_Sarvam\`
- **Reuse:** Sarvam AI SDK integration, text translation with chunking, rate limiting, LLM quality correction
- **Key files:** `translate_text.py`, `correct_srt.py`, `sanskrit_learn_module.html`

#### `D:\WebApps\DocumentTranslation\`
- **Reuse:** Exponential backoff (`min(2 ** (attempt + 2), 60)` → 4s, 8s, 16s, 32s, capped at 60s), parallel chunk processing, state persistence/resume, PDF splitting, structural parsing (act/section/prologue detection), language classification (Devanagari ratio), bilingual React reader
- **Key files:** `digitize.py`, `extract_bilingual.py`, `split_pdf.py`, `ReactProject/`

### Reasoning
These projects were built by the same developer, use the same Sarvam AI platform, and solve adjacent problems (video translation, manuscript digitization). Reusing their patterns avoids reinventing retry logic, chunking, structural parsing, and bilingual presentation.

---

## 3. Async digitization with in-memory job store

**Date:** 2026-03-05
**Status:** Accepted

### Context
The Sarvam Document Intelligence API is inherently async — the workflow is: create a job → upload a file to it → start the job → poll for status → download the output ZIP when complete. A single digitization can take anywhere from 30 seconds to several minutes depending on PDF size. We needed a way to handle this without blocking the `POST /api/upload` HTTP request, while still letting the frontend track progress and display results when ready.

The reference implementation at `D:\WebApps\DocumentTranslation\digitize.py` uses a similar pattern (background processing with status tracking), which informed this design.

### Decision

#### Background threads for async processing
- Use Python's `threading.Thread` (with `daemon=True`) to run the Sarvam API workflow in the background
- The upload endpoint returns immediately with a `job_id`, while the thread handles the full create → upload → start → poll → download → extract cycle
- Chose threads over `asyncio` because the Sarvam SDK (`sarvamai`) uses synchronous/blocking calls, and wrapping them in `asyncio.to_thread` would add complexity without benefit at this stage

#### In-memory job store
- Jobs stored in a plain Python dict (`jobs = {}`) protected by `threading.Lock` for thread safety
- Each job entry contains: `job_id`, `filename`, `pages`, `status`, `detail` (human-readable progress text), `html` (result), `error`
- `get_job()` returns a `.copy()` of the dict to prevent concurrent mutation issues
- No persistence — jobs are lost on server restart

#### Frontend polling
- Frontend polls `GET /api/jobs/{job_id}` every 3 seconds via `setTimeout` (not `setInterval`, to avoid overlapping requests if one is slow)
- Polling stops as soon as status is `completed` or `failed`
- The 3-second interval was chosen as a balance between responsiveness and not hammering the server — the actual Sarvam API polling on the server side is slower (5-15s), so the frontend poll mostly just reads the in-memory dict

#### Server-side adaptive polling of Sarvam API
- For small documents (<10 pages): poll every 5 seconds (they finish quickly)
- For larger documents: start at 5s, increase to 10s after 30 seconds elapsed, increase to 15s after 5 minutes elapsed
- This reduces unnecessary API calls for large documents that take minutes to process

#### Exponential backoff on rate limits
- Ported from the reference project's pattern: `min(2 ** (attempt + 2), 60)` → delays of 4s, 8s, 16s, 32s, capped at 60s
- Max 5 retry attempts on the job creation step (the most likely point to hit rate limits)
- Only retries on rate limit errors (HTTP 429 or "rate limit" in error message); other errors fail immediately
- Job detail text is updated during retries so the frontend can show "Rate limited, retrying in Xs..."

#### Job status progression
- `uploading` → initial state while submitting to Sarvam API
- `processing` → Sarvam job is running, server is polling
- `completed` → output downloaded, HTML extracted and stored in job
- `failed` → any error at any stage, error message stored

### Alternatives Considered

#### Celery / Redis task queue
- Would provide persistence, retries, and proper task management
- Requires running Redis and a Celery worker process alongside the FastAPI server
- Overkill for the current single-user development stage — adds operational complexity (3 processes instead of 1) for no immediate benefit
- Could migrate to this later if we need multi-user support, job persistence across restarts, or horizontal scaling

#### Server-Sent Events (SSE) or WebSocket for real-time updates
- Would eliminate the need for frontend polling — server pushes updates as they happen
- SSE is simpler than WebSocket and would be a natural fit (unidirectional updates)
- However, adds complexity to both server (managing open connections, handling disconnects) and client (EventSource API, reconnection logic)
- Polling every 3 seconds on a local in-memory dict is effectively instant and perfectly adequate for the current use case
- Could upgrade to SSE later if polling becomes a bottleneck or if we want sub-second status updates

#### Database-backed job store (Supabase)
- We already have Supabase configured in the project
- Would give us persistence across server restarts, ability to query job history, and multi-server support
- Adds latency to every status check (network round-trip to Supabase vs. in-memory dict lookup)
- Not needed until we have actual persistence requirements (user accounts, job history, etc.)
- Easy migration path: swap the dict + lock for Supabase table queries in `get_job`/`update_job`/`create_job`

#### FastAPI BackgroundTasks
- FastAPI has built-in `BackgroundTasks` for fire-and-forget work
- However, it doesn't provide a good way to track task status or retrieve results
- We need bidirectional communication (update status, store results), which the in-memory dict provides
- `threading.Thread` gives us the same fire-and-forget capability with full control over state management

### Consequences
- Simple architecture — single Python process, no external dependencies beyond the Sarvam API
- No infrastructure overhead — no Redis, no message broker, no additional database tables
- Jobs are ephemeral — lost on server restart (acceptable for development; the user can just re-upload)
- The in-memory dict will grow unbounded if many jobs are created without cleanup (not a concern for single-user dev, but would need a TTL/cleanup mechanism in production)
- Easy migration path to any of the alternatives above when the need arises — the `get_job`/`update_job`/`create_job` abstraction makes the storage backend swappable
