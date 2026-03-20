# Plan

**Date:** 2026-03-17

## Context

Large PDFs fail to digitize. No tests exist in the codebase. We need to use TDD to systematically identify the failure point.

## Suspected Issues with Large PDFs

After code review, these are potential failure points for large PDFs:

1. **No server-side file size limit** — `await file.read()` loads entire PDF into memory; large files can cause OOM or timeouts
2. **No upload timeout** — FastAPI default request timeout could be exceeded for large files
3. **Entire PDF bytes held in memory** — passed from upload handler → background thread → temp file; doubles memory usage
4. **No polling timeout** — `while True` loop in `run_digitization` has no maximum wait; large PDFs could take very long and poll forever
5. **Sarvam API may have undocumented file size limits** — no handling for API-side rejection of large files
6. **Rate limiting more likely with large docs** — more pages = more processing = higher chance of hitting rate limits during create/upload/start phase
7. **Temp file cleanup on exception** — if exception occurs after temp file creation but before cleanup, files leak on disk
8. **No page count limits** — a 500-page PDF is accepted the same as a 5-page one

## Approach

### Step 1: Test Infrastructure
- Add pytest + httpx (for async FastAPI testing) to dev dependencies
- Create `server/tests/` directory with `conftest.py`
- Create PDF generation fixtures (small, medium, large page counts)

### Step 2: Unit Tests — `test_digitize_service.py`
- Job store CRUD (create, get, update)
- `adaptive_poll_interval` logic
- `extract_html_from_zip` with various inputs
- Thread safety of job store

### Step 3: Integration Tests — `test_upload.py`
- Valid PDF upload (small)
- Invalid file type rejection
- Corrupted PDF rejection
- Large PDF upload (many pages)
- Large PDF upload (large file size)

### Step 4: Large PDF Failure Tests — `test_large_pdf_digitization.py`
- Memory behavior with large PDFs
- Polling timeout behavior (mock Sarvam to never complete)
- Rate limit exhaustion during upload phase
- Sarvam API error handling for large files
- Temp file cleanup on failure

### Step 5: Run & Analyze
- Run all tests, identify which fail
- Use failures to pinpoint root cause

## Files to Create
- `server/tests/__init__.py`
- `server/tests/conftest.py` — shared fixtures (PDF generators, test client)
- `server/tests/test_digitize_service.py` — unit tests for digitize module
- `server/tests/test_upload.py` — integration tests for upload endpoint
- `server/tests/test_large_pdf_digitization.py` — large PDF specific failure tests
- `server/pytest.ini` — pytest configuration

## Files to Modify
- `server/requirements.txt` — add pytest, httpx, pytest-asyncio dev dependencies

## Verification
- All tests run with `cd server && python -m pytest -v`
- Tests for known issues should fail, identifying the root cause
