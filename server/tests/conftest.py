"""Shared fixtures for PDF upload and digitization tests."""

import io
import zipfile
import pytest
from httpx import AsyncClient, ASGITransport
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from app.main import app
from app.services import digitize


# ---------------------------------------------------------------------------
# Test client
# ---------------------------------------------------------------------------

@pytest.fixture
def client():
    """Async test client for the FastAPI app."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


# ---------------------------------------------------------------------------
# Job store cleanup — isolate tests from each other
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def clean_job_store():
    """Clear the in-memory job store before and after each test."""
    with digitize.jobs_lock:
        digitize.jobs.clear()
    yield
    with digitize.jobs_lock:
        digitize.jobs.clear()


# ---------------------------------------------------------------------------
# PDF generators
# ---------------------------------------------------------------------------

def generate_pdf(num_pages=1, text_per_page="Sanskrit text sample", large_content=False):
    """Generate a valid PDF in memory.

    Args:
        num_pages: Number of pages to generate.
        text_per_page: Text to put on each page.
        large_content: If True, add substantial text to increase file size per page.

    Returns:
        bytes: The PDF file contents.
    """
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    for i in range(num_pages):
        c.drawString(72, 750, f"Page {i + 1}")
        if large_content:
            # Add many lines of text to increase file size
            for line_num in range(50):
                c.drawString(72, 720 - (line_num * 14),
                             f"Line {line_num}: {text_per_page} " * 3)
        else:
            c.drawString(72, 720, text_per_page)
        c.showPage()

    c.save()
    return buf.getvalue()


@pytest.fixture
def small_pdf():
    """A small 3-page PDF (~5 KB)."""
    return generate_pdf(num_pages=3)


@pytest.fixture
def medium_pdf():
    """A medium 30-page PDF."""
    return generate_pdf(num_pages=30, text_per_page="Medium document page content")


@pytest.fixture
def large_pdf():
    """A large 100-page PDF with substantial content per page."""
    return generate_pdf(num_pages=100, large_content=True)


@pytest.fixture
def very_large_pdf():
    """A very large 300-page PDF with substantial content per page."""
    return generate_pdf(num_pages=300, large_content=True)


@pytest.fixture
def corrupt_pdf():
    """A file that claims to be PDF but is garbage."""
    return b"%PDF-1.4 this is not a real pdf file\x00\x01\x02"


@pytest.fixture
def not_a_pdf():
    """A plain text file."""
    return b"Hello, I am not a PDF."


# ---------------------------------------------------------------------------
# ZIP fixtures (for HTML extraction tests)
# ---------------------------------------------------------------------------

def make_html_zip(pages_html):
    """Create a ZIP archive containing numbered HTML files.

    Args:
        pages_html: list of (filename, html_content) tuples.

    Returns:
        bytes: The ZIP file contents.
    """
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for filename, content in pages_html:
            zf.writestr(filename, content)
    return buf.getvalue()


@pytest.fixture
def single_page_zip():
    """ZIP with one HTML page."""
    return make_html_zip([
        ("page_1.html", "<html><head><title>P1</title></head><body><p>Content 1</p></body></html>")
    ])


@pytest.fixture
def multi_page_zip():
    """ZIP with three HTML pages."""
    return make_html_zip([
        ("page_1.html", "<html><body><p>Content 1</p></body></html>"),
        ("page_2.html", "<html><body><p>Content 2</p></body></html>"),
        ("page_3.html", "<html><body><p>Content 3</p></body></html>"),
    ])


@pytest.fixture
def empty_zip():
    """ZIP with no HTML files (only a non-HTML file)."""
    return make_html_zip([
        ("readme.txt", "This is not HTML"),
    ])
