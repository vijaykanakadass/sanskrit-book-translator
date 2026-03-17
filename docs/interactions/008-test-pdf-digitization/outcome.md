# Outcome

**Date:** 2026-03-17

## What Was Built

A comprehensive test suite with **51 tests** covering PDF upload and digitization. All tests pass.

## Test Results

```
51 passed in 16.39s
```

### Test Breakdown

| Test File | Tests | Focus |
|-----------|-------|-------|
| `test_digitize_service.py` | 24 | Job store, polling logic, HTML extraction |
| `test_upload.py` | 10 | Upload endpoint validation, large PDFs, job status |
| `test_large_pdf_digitization.py` | 17 | Bug detection for large PDF failures |

## Bugs Identified (Root Causes for Large PDF Failures)

### BUG #1: No Polling Timeout (CRITICAL)
- **Location:** `server/app/services/digitize.py:123` — `while True:` loop
- **Impact:** If Sarvam API never returns "Completed" for a large PDF, the background thread polls **forever**. No max duration, no deadline.
- **Evidence:** Test `test_polling_should_timeout_for_stuck_jobs` — thread still alive after 15s timeout.

### BUG #2: No Server-Side File Size Limit (HIGH)
- **Location:** `server/app/routers/upload.py:14` — `contents = await file.read()`
- **Impact:** The server reads the **entire file into memory** with no size check. A 500MB PDF would consume 500MB of server RAM. Only the client enforces 300MB, which can be bypassed via direct API calls.
- **Evidence:** Test `test_no_server_side_size_limit_exists` confirms no size validation in source code.

### BUG #3: No Page Count Limit (MEDIUM)
- **Location:** `server/app/routers/upload.py` — no validation after `pages = len(pdf.pages)`
- **Impact:** A 1000-page PDF is sent to Sarvam API which may reject it, take extremely long, or hit rate limits.
- **Evidence:** Test `test_no_page_count_limit` confirms no page validation in source code.

### BUG #4: Temp File Leaks on Failure (MEDIUM)
- **Location:** `server/app/services/digitize.py:90-91` — temp file created outside try/finally
- **Impact:** If Sarvam API fails during create_job or download_output, temp PDF and ZIP files are never cleaned up. Over time this can fill disk.
- **Evidence:** Tests `test_temp_file_leaks_on_sarvam_api_failure` and `test_temp_file_leaks_on_download_failure` detect leaked files.

### BUG #5: Memory Doubling for Large PDFs (MEDIUM)
- **Location:** `server/app/services/digitize.py:84,91` — `pdf_bytes` kept in scope after writing to temp file
- **Impact:** For a 100MB PDF: 100MB in `pdf_bytes` variable + 100MB temp file on disk. The `pdf_bytes` reference is never freed until the function returns.
- **Evidence:** Test `test_pdf_bytes_passed_by_reference_to_thread` confirms no `del pdf_bytes` after temp file write.

## Most Likely Root Cause for "Large PDFs Not Getting Digitized"

**BUG #1 (no polling timeout)** is the most likely culprit. Large PDFs take longer for Sarvam to process. If the processing exceeds what the user is willing to wait, or if the Sarvam job stalls, the background thread will poll indefinitely — the job will show "processing" forever and never complete or fail.

Combined with **BUG #2** (no size limit) causing potential memory issues and **BUG #4** (temp file leaks) degrading the server over time, large PDFs face a "death by a thousand cuts" scenario.

## Recommended Fixes (Priority Order)

1. Add a max polling duration (e.g., 10 minutes) to `run_digitization` — mark job as failed if exceeded
2. Add server-side file size limit (e.g., 50MB) in the upload endpoint
3. Add page count limit (e.g., 200 pages) in the upload endpoint
4. Use try/finally for temp file cleanup in `run_digitization`
5. Add `del pdf_bytes` after writing to temp file to free memory
