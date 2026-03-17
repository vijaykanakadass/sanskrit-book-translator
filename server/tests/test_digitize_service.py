"""Unit tests for app.services.digitize — job store, HTML extraction, polling logic."""

import threading
from app.services.digitize import (
    create_job,
    get_job,
    update_job,
    adaptive_poll_interval,
    extract_html_from_zip,
)
from tests.conftest import make_html_zip


# ═══════════════════════════════════════════════════════════════════════════
# Job Store Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestCreateJob:
    def test_returns_uuid_string(self):
        job_id = create_job("test.pdf", 5)
        assert isinstance(job_id, str)
        assert len(job_id) == 36  # UUID format

    def test_initial_status_is_uploading(self):
        job_id = create_job("test.pdf", 5)
        job = get_job(job_id)
        assert job["status"] == "uploading"

    def test_stores_filename_and_pages(self):
        job_id = create_job("sanskrit_book.pdf", 42)
        job = get_job(job_id)
        assert job["filename"] == "sanskrit_book.pdf"
        assert job["pages"] == 42

    def test_html_and_error_initially_none(self):
        job_id = create_job("test.pdf", 1)
        job = get_job(job_id)
        assert job["html"] is None
        assert job["error"] is None

    def test_multiple_jobs_independent(self):
        id1 = create_job("a.pdf", 5)
        id2 = create_job("b.pdf", 10)
        assert id1 != id2
        assert get_job(id1)["filename"] == "a.pdf"
        assert get_job(id2)["filename"] == "b.pdf"


class TestGetJob:
    def test_returns_empty_dict_for_nonexistent_job(self):
        job = get_job("nonexistent-id")
        assert job == {}

    def test_returns_copy_not_reference(self):
        job_id = create_job("test.pdf", 1)
        job_copy = get_job(job_id)
        job_copy["status"] = "tampered"
        # Original should be unchanged
        assert get_job(job_id)["status"] == "uploading"


class TestUpdateJob:
    def test_updates_status(self):
        job_id = create_job("test.pdf", 1)
        update_job(job_id, status="processing", detail="Working...")
        job = get_job(job_id)
        assert job["status"] == "processing"
        assert job["detail"] == "Working..."

    def test_update_nonexistent_job_does_not_crash(self):
        # Should silently do nothing
        update_job("fake-id", status="processing")

    def test_update_preserves_other_fields(self):
        job_id = create_job("test.pdf", 5)
        update_job(job_id, status="completed")
        job = get_job(job_id)
        assert job["filename"] == "test.pdf"
        assert job["pages"] == 5


class TestJobStoreThreadSafety:
    def test_concurrent_creates(self):
        """Multiple threads creating jobs should not lose any."""
        ids = []
        lock = threading.Lock()

        def create():
            job_id = create_job("test.pdf", 1)
            with lock:
                ids.append(job_id)

        threads = [threading.Thread(target=create) for _ in range(50)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert len(ids) == 50
        assert len(set(ids)) == 50  # All unique

    def test_concurrent_updates(self):
        """Multiple threads updating the same job should not corrupt it."""
        job_id = create_job("test.pdf", 1)

        def updater(n):
            update_job(job_id, detail=f"Update {n}")

        threads = [threading.Thread(target=updater, args=(i,)) for i in range(50)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        job = get_job(job_id)
        assert job["detail"].startswith("Update ")


# ═══════════════════════════════════════════════════════════════════════════
# Adaptive Poll Interval Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestAdaptivePollInterval:
    def test_small_doc_always_5s(self):
        """Documents under 10 pages should always poll at 5s."""
        assert adaptive_poll_interval(0, 5) == 5.0
        assert adaptive_poll_interval(100, 5) == 5.0
        assert adaptive_poll_interval(500, 5) == 5.0

    def test_large_doc_early_5s(self):
        """Large docs poll at 5s for the first 30 seconds."""
        assert adaptive_poll_interval(0, 50) == 5.0
        assert adaptive_poll_interval(29, 50) == 5.0

    def test_large_doc_mid_10s(self):
        """Large docs poll at 10s between 30-300 seconds."""
        assert adaptive_poll_interval(30, 50) == 10.0
        assert adaptive_poll_interval(150, 50) == 10.0
        assert adaptive_poll_interval(299, 50) == 10.0

    def test_large_doc_late_15s(self):
        """Large docs poll at 15s after 300 seconds."""
        assert adaptive_poll_interval(300, 50) == 15.0
        assert adaptive_poll_interval(600, 50) == 15.0

    def test_boundary_at_10_pages(self):
        """10 pages is the threshold for adaptive polling."""
        # 9 pages = always 5s
        assert adaptive_poll_interval(100, 9) == 5.0
        # 10 pages = adaptive (should be 10s at 100 elapsed)
        assert adaptive_poll_interval(100, 10) == 10.0


# ═══════════════════════════════════════════════════════════════════════════
# HTML Extraction Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestExtractHtmlFromZip:
    def test_single_page(self, single_page_zip):
        html = extract_html_from_zip(single_page_zip)
        assert 'id="page-1"' in html
        assert "Content 1" in html
        assert "Page 1" in html

    def test_multi_page_preserves_order(self, multi_page_zip):
        html = extract_html_from_zip(multi_page_zip)
        assert 'id="page-1"' in html
        assert 'id="page-2"' in html
        assert 'id="page-3"' in html
        # Order check
        pos1 = html.index("Content 1")
        pos2 = html.index("Content 2")
        pos3 = html.index("Content 3")
        assert pos1 < pos2 < pos3

    def test_strips_html_wrappers(self, single_page_zip):
        html = extract_html_from_zip(single_page_zip)
        assert "<html" not in html.lower()
        assert "<head" not in html.lower()
        assert "<body" not in html.lower()
        assert "</html>" not in html.lower()

    def test_empty_zip_returns_empty_string(self, empty_zip):
        html = extract_html_from_zip(empty_zip)
        assert html == ""

    def test_page_headers_added(self, multi_page_zip):
        html = extract_html_from_zip(multi_page_zip)
        assert "page-header" in html
        assert "Page 1" in html
        assert "Page 2" in html
        assert "Page 3" in html

    def test_large_number_of_pages(self):
        """Test extraction with many pages (simulating a large book)."""
        pages = [
            (f"page_{i:03d}.html", f"<html><body><p>Page {i} content</p></body></html>")
            for i in range(1, 101)
        ]
        zip_bytes = make_html_zip(pages)
        html = extract_html_from_zip(zip_bytes)
        assert 'id="page-100"' in html
        assert "Page 100 content" in html

    def test_unicode_content(self):
        """Sanskrit text should survive extraction."""
        pages = [
            ("page_1.html", "<html><body><p>ॐ नमः शिवाय</p></body></html>")
        ]
        zip_bytes = make_html_zip(pages)
        html = extract_html_from_zip(zip_bytes)
        assert "ॐ नमः शिवाय" in html
