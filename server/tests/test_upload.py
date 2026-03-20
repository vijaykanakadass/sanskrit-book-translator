"""Integration tests for the /api/upload endpoint."""

import io
import pytest
from unittest.mock import patch, MagicMock
from tests.conftest import generate_pdf


# ═══════════════════════════════════════════════════════════════════════════
# Upload Validation Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestUploadValidation:
    @pytest.mark.asyncio
    async def test_rejects_non_pdf_content_type(self, client):
        """Non-PDF files should be rejected with 400."""
        response = await client.post(
            "/api/upload",
            files={"file": ("test.txt", b"hello world", "text/plain")},
        )
        assert response.status_code == 400
        assert "Only PDF" in response.json()["detail"]

    @pytest.mark.asyncio
    async def test_rejects_corrupted_pdf(self, client, corrupt_pdf):
        """Corrupted PDFs should be rejected with 400."""
        response = await client.post(
            "/api/upload",
            files={"file": ("corrupt.pdf", corrupt_pdf, "application/pdf")},
        )
        assert response.status_code == 400
        assert "corrupted" in response.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_rejects_empty_pdf(self, client):
        """Empty bytes with PDF content type should be rejected."""
        response = await client.post(
            "/api/upload",
            files={"file": ("empty.pdf", b"", "application/pdf")},
        )
        assert response.status_code == 400


# ═══════════════════════════════════════════════════════════════════════════
# Successful Upload Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestSuccessfulUpload:
    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_small_pdf_upload_returns_job(self, mock_start, client, small_pdf):
        """A valid small PDF should return a job with status 'processing'."""
        response = await client.post(
            "/api/upload",
            files={"file": ("small.pdf", small_pdf, "application/pdf")},
        )
        assert response.status_code == 200
        data = response.json()
        assert "job_id" in data
        assert data["filename"] == "small.pdf"
        assert data["pages"] == 3
        assert data["status"] == "processing"
        assert data["size"] == len(small_pdf)
        mock_start.assert_called_once()

    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_medium_pdf_upload(self, mock_start, client, medium_pdf):
        """A valid 30-page PDF should be accepted."""
        response = await client.post(
            "/api/upload",
            files={"file": ("medium.pdf", medium_pdf, "application/pdf")},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["pages"] == 30

    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_upload_returns_correct_file_size(self, mock_start, client, small_pdf):
        """Response should include accurate file size in bytes."""
        response = await client.post(
            "/api/upload",
            files={"file": ("test.pdf", small_pdf, "application/pdf")},
        )
        assert response.json()["size"] == len(small_pdf)


# ═══════════════════════════════════════════════════════════════════════════
# Large PDF Upload Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestLargePdfUpload:
    @pytest.mark.asyncio
    @pytest.mark.large_pdf
    @patch("app.routers.upload.start_digitization")
    async def test_100_page_pdf_upload(self, mock_start, client, large_pdf):
        """A 100-page PDF should be accepted and page count extracted."""
        response = await client.post(
            "/api/upload",
            files={"file": ("large.pdf", large_pdf, "application/pdf")},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["pages"] == 100

    @pytest.mark.asyncio
    @pytest.mark.large_pdf
    @patch("app.routers.upload.start_digitization")
    async def test_300_page_pdf_upload(self, mock_start, client, very_large_pdf):
        """A 300-page PDF should be accepted."""
        response = await client.post(
            "/api/upload",
            files={"file": ("very_large.pdf", very_large_pdf, "application/pdf")},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["pages"] == 300

    @pytest.mark.asyncio
    @pytest.mark.large_pdf
    @patch("app.routers.upload.start_digitization")
    async def test_large_pdf_file_size_reported(self, mock_start, client, large_pdf):
        """File size should be accurately reported for large PDFs."""
        response = await client.post(
            "/api/upload",
            files={"file": ("large.pdf", large_pdf, "application/pdf")},
        )
        data = response.json()
        assert data["size"] == len(large_pdf)
        # A 100-page PDF with content should be non-trivially large
        assert data["size"] > 10_000  # At least 10KB


# ═══════════════════════════════════════════════════════════════════════════
# Job Status Endpoint Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestJobStatus:
    @pytest.mark.asyncio
    async def test_nonexistent_job_returns_404(self, client):
        response = await client.get("/api/jobs/nonexistent-id")
        assert response.status_code == 404

    @pytest.mark.asyncio
    @patch("app.routers.upload.start_digitization")
    async def test_job_status_after_upload(self, mock_start, client, small_pdf):
        """After upload, job should be retrievable via status endpoint."""
        upload_resp = await client.post(
            "/api/upload",
            files={"file": ("test.pdf", small_pdf, "application/pdf")},
        )
        job_id = upload_resp.json()["job_id"]

        status_resp = await client.get(f"/api/jobs/{job_id}")
        assert status_resp.status_code == 200
        data = status_resp.json()
        assert data["job_id"] == job_id
        assert data["filename"] == "test.pdf"
