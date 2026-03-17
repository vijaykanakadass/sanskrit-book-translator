# Changes

**Date:** 2026-03-17

## Files Created

| File | Purpose |
|------|---------|
| `server/pytest.ini` | Pytest configuration with test markers (slow, large_pdf) |
| `server/tests/__init__.py` | Makes tests a Python package |
| `server/tests/conftest.py` | Shared fixtures: test client, PDF generators, ZIP generators, job store cleanup |
| `server/tests/test_digitize_service.py` | 24 unit tests for job store CRUD, thread safety, adaptive polling, HTML extraction |
| `server/tests/test_upload.py` | 10 integration tests for /api/upload and /api/jobs endpoints |
| `server/tests/test_large_pdf_digitization.py` | 17 tests targeting large PDF failure scenarios and bug detection |

## Files Modified

| File | Change |
|------|--------|
| `server/requirements.txt` | Added pytest, pytest-asyncio, httpx, reportlab as test dependencies |
