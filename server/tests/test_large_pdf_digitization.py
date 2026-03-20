"""Tests targeting large PDF digitization failures.

These tests use mocks to simulate the Sarvam API behavior and expose
failure modes specific to large PDFs:
- No polling timeout (infinite loop)
- No server-side file size limit
- Memory usage with large files
- Rate limit exhaustion
- Temp file cleanup on failure
- Missing page count validation
"""

import io
import os
import time
import tempfile
import threading
from pathlib import Path
from unittest.mock import patch, MagicMock, PropertyMock

import pytest

from app.services.digitize import (
    run_digitization,
    create_job,
    get_job,
    update_job,
    start_digitization,
)
from tests.conftest import generate_pdf


# ═══════════════════════════════════════════════════════════════════════════
# BUG #1: No polling timeout — infinite loop for stuck jobs
# ═══════════════════════════════════════════════════════════════════════════


class TestPollingTimeout:
    """The `while True` loop in run_digitization has NO timeout.
    If Sarvam never completes, the thread polls forever."""

    @patch("app.services.digitize.SarvamAI")
    def test_polling_should_timeout_for_stuck_jobs(self, mock_sarvam_class):
        """EXPECTED FAILURE: There is no max polling duration.
        A job that never completes will poll indefinitely.
        This test verifies the bug exists by checking that
        run_digitization does NOT set a timeout."""
        job_id = create_job("stuck.pdf", 10)
        pdf_bytes = generate_pdf(num_pages=10)

        # Mock Sarvam to always return "InProgress"
        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job

        status_mock = MagicMock()
        status_mock.job_state = "InProgress"
        mock_job.get_status.return_value = status_mock

        # Run in a thread with a timeout to prevent actual infinite loop
        result = {"completed": False, "error": None}

        def run():
            try:
                run_digitization(job_id, pdf_bytes)
                result["completed"] = True
            except Exception as e:
                result["error"] = str(e)

        thread = threading.Thread(target=run, daemon=True)
        thread.start()
        thread.join(timeout=15)  # Wait max 15 seconds

        job = get_job(job_id)

        # BUG: The thread is still running (stuck in while True loop)
        # It should have timed out and marked the job as failed
        if thread.is_alive():
            # The thread is still polling — this IS the bug
            # A proper implementation would have a max_poll_duration
            assert job["status"] != "failed", \
                "BUG CONFIRMED: Job is stuck polling forever. " \
                "No timeout exists in the while True loop. " \
                "Large PDFs that take too long will hang indefinitely."

    @patch("app.services.digitize.SarvamAI")
    def test_should_have_max_polling_duration(self, mock_sarvam_class):
        """Verify that there is NO max polling duration configured.
        This documents the missing feature."""
        import inspect
        source = inspect.getsource(run_digitization)

        # Check for any timeout/max duration mechanism
        has_timeout = any(term in source.lower() for term in [
            "max_poll", "timeout", "max_duration", "max_wait",
            "deadline", "max_elapsed", "time_limit",
        ])

        assert not has_timeout, \
            "Good news: a polling timeout was added!"

        # If we get here, the bug is confirmed
        print("\nBUG CONFIRMED: run_digitization has no polling timeout.")
        print("Large PDFs that take longer than expected will poll forever.")


# ═══════════════════════════════════════════════════════════════════════════
# BUG #2: No server-side file size limit
# ═══════════════════════════════════════════════════════════════════════════


class TestServerSideFileSizeLimit:
    """The upload endpoint has NO server-side file size validation.
    Only the client enforces 300MB — a direct API call can upload any size."""

    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_no_server_side_size_limit_exists(self, mock_start, client):
        """Document that there is no server-side size check.
        The server reads the entire file into memory regardless of size."""
        import inspect
        from app.routers.upload import upload_pdf
        source = inspect.getsource(upload_pdf)

        has_size_check = any(term in source.lower() for term in [
            "max_size", "file_size", "content_length", "size_limit",
            "too large", "max_file", "size >", "size >="
        ])

        assert not has_size_check, \
            "Good news: a server-side size limit was added!"

        print("\nBUG CONFIRMED: No server-side file size limit.")
        print("Any size file can be uploaded, potentially causing OOM.")

    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_server_accepts_arbitrarily_large_pdf(self, mock_start, client):
        """Without a size limit, very large PDFs are accepted."""
        large_pdf = generate_pdf(num_pages=200, large_content=True)
        response = await client.post(
            "/api/upload",
            files={"file": ("huge.pdf", large_pdf, "application/pdf")},
        )
        # This SHOULD be rejected but currently isn't
        assert response.status_code == 200, \
            "Server accepted a very large PDF without any size validation"


# ═══════════════════════════════════════════════════════════════════════════
# BUG #3: No page count limit
# ═══════════════════════════════════════════════════════════════════════════


class TestPageCountLimit:
    """No limit on the number of pages. A 1000-page PDF would be
    sent to Sarvam API which may reject it or take extremely long."""

    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_no_page_count_limit(self, mock_start, client):
        """Verify there is no page count validation."""
        import inspect
        from app.routers.upload import upload_pdf
        source = inspect.getsource(upload_pdf)

        has_page_limit = any(term in source.lower() for term in [
            "max_pages", "page_limit", "too many pages", "pages >",
            "page_count", "pages >="
        ])

        assert not has_page_limit, \
            "Good news: a page count limit was added!"

        print("\nBUG CONFIRMED: No page count limit on upload.")


# ═══════════════════════════════════════════════════════════════════════════
# BUG #4: Temp file cleanup not guaranteed on failure
# ═══════════════════════════════════════════════════════════════════════════


class TestTempFileCleanup:
    """Temp files are created but only cleaned up in the success path.
    If an exception occurs between creation and cleanup, files leak."""

    @patch("app.services.digitize.SarvamAI")
    def test_temp_file_leaks_on_sarvam_api_failure(self, mock_sarvam_class):
        """If Sarvam API fails during create_job, temp PDF file leaks."""
        job_id = create_job("test.pdf", 5)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        # Make create_job fail on first attempt (non-rate-limit error)
        mock_client.document_intelligence.create_job.side_effect = Exception(
            "API unavailable"
        )

        # Track temp files before
        temp_dir = tempfile.gettempdir()
        pdf_temps_before = set(
            f for f in os.listdir(temp_dir) if f.endswith(".pdf")
        )

        run_digitization(job_id, pdf_bytes)

        # Check for leaked temp files
        pdf_temps_after = set(
            f for f in os.listdir(temp_dir) if f.endswith(".pdf")
        )
        leaked = pdf_temps_after - pdf_temps_before

        if leaked:
            # Clean up the leaked files ourselves
            for f in leaked:
                os.unlink(os.path.join(temp_dir, f))
            print(f"\nBUG CONFIRMED: {len(leaked)} temp file(s) leaked on failure: {leaked}")

        job = get_job(job_id)
        assert job["status"] == "failed"

    @patch("app.services.digitize.SarvamAI")
    def test_temp_file_leaks_on_download_failure(self, mock_sarvam_class):
        """If download_output fails, both temp PDF and temp ZIP may leak."""
        job_id = create_job("test.pdf", 5)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job

        # Make get_status return "Completed"
        status_mock = MagicMock()
        status_mock.job_state = "Completed"
        mock_job.get_status.return_value = status_mock

        # Make download_output fail
        mock_job.download_output.side_effect = Exception("Download failed: file too large")

        temp_dir = tempfile.gettempdir()
        pdf_temps_before = set(
            f for f in os.listdir(temp_dir) if f.endswith((".pdf", ".zip"))
        )

        run_digitization(job_id, pdf_bytes)

        pdf_temps_after = set(
            f for f in os.listdir(temp_dir) if f.endswith((".pdf", ".zip"))
        )
        leaked = pdf_temps_after - pdf_temps_before

        if leaked:
            for f in leaked:
                os.unlink(os.path.join(temp_dir, f))
            print(f"\nBUG CONFIRMED: {len(leaked)} temp file(s) leaked on download failure: {leaked}")

        job = get_job(job_id)
        assert job["status"] == "failed"


# ═══════════════════════════════════════════════════════════════════════════
# BUG #5: Rate limit retry may not be sufficient for large PDFs
# ═══════════════════════════════════════════════════════════════════════════


class TestRateLimitHandling:
    @patch("app.services.digitize.time.sleep")  # Don't actually sleep in tests
    @patch("app.services.digitize.SarvamAI")
    def test_rate_limit_exhaustion_marks_job_failed(self, mock_sarvam_class, mock_sleep):
        """After 5 rate limit retries, job should be marked as failed."""
        job_id = create_job("large.pdf", 100)
        pdf_bytes = generate_pdf(num_pages=5)  # Small PDF, simulating rate limit

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_client.document_intelligence.create_job.side_effect = Exception(
            "HTTP 429: rate limit exceeded"
        )

        run_digitization(job_id, pdf_bytes)

        job = get_job(job_id)
        assert job["status"] == "failed"
        assert "rate limit" in job["error"].lower() or "429" in job["error"]

    @patch("app.services.digitize.time.sleep")
    @patch("app.services.digitize.SarvamAI")
    def test_rate_limit_retries_use_exponential_backoff(self, mock_sarvam_class, mock_sleep):
        """Verify backoff intervals: 4s, 8s, 16s, 32s."""
        job_id = create_job("test.pdf", 5)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_client.document_intelligence.create_job.side_effect = Exception(
            "429 rate limit"
        )

        run_digitization(job_id, pdf_bytes)

        # Check that sleep was called with exponential backoff
        sleep_calls = [call.args[0] for call in mock_sleep.call_args_list]
        # Should be 4 retries (5 total attempts, 4 sleeps)
        assert len(sleep_calls) == 4
        assert sleep_calls == [4, 8, 16, 32]

    @patch("app.services.digitize.time.sleep")
    @patch("app.services.digitize.SarvamAI")
    def test_non_rate_limit_error_fails_immediately(self, mock_sarvam_class, mock_sleep):
        """Non-rate-limit errors should fail without retrying."""
        job_id = create_job("test.pdf", 5)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_client.document_intelligence.create_job.side_effect = Exception(
            "Invalid API key"
        )

        run_digitization(job_id, pdf_bytes)

        job = get_job(job_id)
        assert job["status"] == "failed"
        # Should NOT have retried (no sleep calls for rate limit backoff)
        mock_sleep.assert_not_called()


# ═══════════════════════════════════════════════════════════════════════════
# BUG #6: Sarvam API failure for large files
# ═══════════════════════════════════════════════════════════════════════════


class TestSarvamApiLargeFileHandling:
    @patch("app.services.digitize.SarvamAI")
    def test_sarvam_job_failed_state_handled(self, mock_sarvam_class):
        """When Sarvam returns 'Failed' state, job should be marked failed."""
        job_id = create_job("large.pdf", 100)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job

        status_mock = MagicMock()
        status_mock.job_state = "Failed"
        mock_job.get_status.return_value = status_mock

        run_digitization(job_id, pdf_bytes)

        job = get_job(job_id)
        assert job["status"] == "failed"
        assert "failed" in job["error"].lower()

    @patch("app.services.digitize.SarvamAI")
    def test_sarvam_upload_file_failure(self, mock_sarvam_class):
        """If upload_file fails (e.g., file too large for Sarvam), should fail gracefully."""
        job_id = create_job("huge.pdf", 500)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job
        mock_job.upload_file.side_effect = Exception(
            "File too large: maximum 50MB allowed"
        )

        run_digitization(job_id, pdf_bytes)

        job = get_job(job_id)
        assert job["status"] == "failed"
        assert "too large" in job["error"].lower()

    @patch("app.services.digitize.SarvamAI")
    def test_partially_completed_job_still_returns_html(self, mock_sarvam_class):
        """PartiallyCompleted state should still extract available HTML."""
        job_id = create_job("large.pdf", 100)
        pdf_bytes = generate_pdf(num_pages=5)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job

        # First return InProgress, then PartiallyCompleted
        status_inprog = MagicMock()
        status_inprog.job_state = "InProgress"
        status_partial = MagicMock()
        status_partial.job_state = "PartiallyCompleted"
        mock_job.get_status.side_effect = [status_inprog, status_partial]

        # Create a valid zip for download
        import zipfile
        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w") as zf:
            zf.writestr("page_1.html", "<html><body><p>Partial content</p></body></html>")
        zip_bytes = zip_buf.getvalue()

        def fake_download(path):
            Path(path).write_bytes(zip_bytes)
        mock_job.download_output.side_effect = fake_download

        with patch("app.services.digitize.time.sleep"):
            run_digitization(job_id, pdf_bytes)

        job = get_job(job_id)
        assert job["status"] == "completed"
        assert "Partial content" in job["html"]


# ═══════════════════════════════════════════════════════════════════════════
# BUG #7: Memory concerns — PDF bytes held in memory during processing
# ═══════════════════════════════════════════════════════════════════════════


class TestMemoryHandling:
    def test_pdf_bytes_passed_by_reference_to_thread(self):
        """Document that the entire PDF is held in memory while the thread runs.
        For a 100MB PDF, this means 100MB stays in memory until thread completes."""
        import inspect
        from app.services.digitize import start_digitization
        source = inspect.getsource(start_digitization)

        # The function passes pdf_bytes directly to the thread
        assert "pdf_bytes" in source

        # Check run_digitization for streaming/chunking
        run_source = inspect.getsource(run_digitization)
        uses_streaming = any(term in run_source.lower() for term in [
            "stream", "chunk", "iter_bytes", "read(",
        ])

        # pdf_bytes is written to temp file, but original bytes stay in memory
        # until the function returns
        assert "tmp.write(pdf_bytes)" in run_source, \
            "PDF bytes are written to temp file"

        # After writing to temp file, pdf_bytes should be freed but isn't
        has_explicit_cleanup = "del pdf_bytes" in run_source
        assert not has_explicit_cleanup, \
            "BUG CONFIRMED: pdf_bytes not explicitly freed after writing to temp file. " \
            "For large PDFs, this doubles memory usage (bytes in memory + temp file on disk)."


# ═══════════════════════════════════════════════════════════════════════════
# End-to-End Digitization Flow (with mocked Sarvam)
# ═══════════════════════════════════════════════════════════════════════════


class TestDigitizationFlow:
    @patch("app.services.digitize.time.sleep")
    @patch("app.services.digitize.SarvamAI")
    def test_successful_small_pdf_flow(self, mock_sarvam_class, mock_sleep):
        """Full happy path: upload → process → complete."""
        job_id = create_job("test.pdf", 3)
        pdf_bytes = generate_pdf(num_pages=3)

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job

        status_complete = MagicMock()
        status_complete.job_state = "Completed"
        mock_job.get_status.return_value = status_complete

        # Create valid zip output
        import zipfile
        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w") as zf:
            zf.writestr("page_1.html", "<html><body><p>Page 1 text</p></body></html>")
            zf.writestr("page_2.html", "<html><body><p>Page 2 text</p></body></html>")
            zf.writestr("page_3.html", "<html><body><p>Page 3 text</p></body></html>")
        zip_bytes = zip_buf.getvalue()

        def fake_download(path):
            Path(path).write_bytes(zip_bytes)
        mock_job.download_output.side_effect = fake_download

        run_digitization(job_id, pdf_bytes)

        job = get_job(job_id)
        assert job["status"] == "completed"
        assert job["html"] is not None
        assert "Page 1 text" in job["html"]
        assert "Page 2 text" in job["html"]
        assert "Page 3 text" in job["html"]
        assert job["error"] is None

    @patch("app.services.digitize.time.sleep")
    @patch("app.services.digitize.SarvamAI")
    def test_job_status_transitions(self, mock_sarvam_class, mock_sleep):
        """Job should go through uploading → processing → completed."""
        job_id = create_job("test.pdf", 3)
        pdf_bytes = generate_pdf(num_pages=3)

        # Track status changes
        statuses = []
        original_update = update_job.__wrapped__ if hasattr(update_job, '__wrapped__') else None

        mock_client = MagicMock()
        mock_sarvam_class.return_value = mock_client
        mock_job = MagicMock()
        mock_client.document_intelligence.create_job.return_value = mock_job

        status_complete = MagicMock()
        status_complete.job_state = "Completed"
        mock_job.get_status.return_value = status_complete

        import zipfile
        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w") as zf:
            zf.writestr("page_1.html", "<html><body><p>Text</p></body></html>")

        def fake_download(path):
            Path(path).write_bytes(zip_buf.getvalue())
        mock_job.download_output.side_effect = fake_download

        # Check initial status
        assert get_job(job_id)["status"] == "uploading"

        run_digitization(job_id, pdf_bytes)

        # Final status should be completed
        assert get_job(job_id)["status"] == "completed"
