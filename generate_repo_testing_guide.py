"""Generate a PDF guide: Testing Python — Explained Through the Sanskrit Book Translator.

Each chapter uses actual source and test code from this repository to teach
a testing concept from scratch.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Preformatted, KeepTogether,
    HRFlowable,
)
from reportlab.lib.colors import black, white, gray

OUTPUT = "/home/user/sanskrit-book-translator/testing-python-repo-guide.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    topMargin=0.8 * inch,
    bottomMargin=0.8 * inch,
    leftMargin=0.9 * inch,
    rightMargin=0.9 * inch,
)

styles = getSampleStyleSheet()

# ── Custom styles ────────────────────────────────────────────────
styles.add(ParagraphStyle(
    name='CoverTitle', fontName='Helvetica-Bold', fontSize=26,
    leading=32, alignment=TA_CENTER, spaceAfter=12,
    textColor=HexColor('#1a1a2e'),
))
styles.add(ParagraphStyle(
    name='CoverSubtitle', fontName='Helvetica', fontSize=13,
    leading=17, alignment=TA_CENTER, spaceAfter=6,
    textColor=HexColor('#555555'),
))
styles.add(ParagraphStyle(
    name='ChapterTitle', fontName='Helvetica-Bold', fontSize=22,
    leading=28, spaceBefore=6, spaceAfter=14,
    textColor=HexColor('#16213e'),
))
styles.add(ParagraphStyle(
    name='SectionTitle', fontName='Helvetica-Bold', fontSize=16,
    leading=20, spaceBefore=16, spaceAfter=8,
    textColor=HexColor('#0f3460'),
))
styles.add(ParagraphStyle(
    name='SubSection', fontName='Helvetica-Bold', fontSize=12,
    leading=16, spaceBefore=12, spaceAfter=6,
    textColor=HexColor('#333333'),
))
styles.add(ParagraphStyle(
    name='Body2', fontName='Helvetica', fontSize=10.5,
    leading=15, spaceBefore=4, spaceAfter=4,
    alignment=TA_JUSTIFY, textColor=HexColor('#222222'),
))
styles.add(ParagraphStyle(
    name='BulletItem', fontName='Helvetica', fontSize=10.5,
    leading=15, leftIndent=20, spaceBefore=2, spaceAfter=2,
    bulletIndent=8, textColor=HexColor('#222222'),
))
styles.add(ParagraphStyle(
    name='CodeStyle', fontName='Courier', fontSize=8.5,
    leading=11.5, leftIndent=16, rightIndent=16,
    spaceBefore=6, spaceAfter=6,
    backColor=HexColor('#f4f4f8'), borderColor=HexColor('#cccccc'),
    borderWidth=0.5, borderPadding=8, textColor=HexColor('#1a1a1a'),
))
styles.add(ParagraphStyle(
    name='Tip', fontName='Helvetica-Oblique', fontSize=10,
    leading=14, leftIndent=20, spaceBefore=6, spaceAfter=6,
    textColor=HexColor('#2e7d32'), borderColor=HexColor('#a5d6a7'),
    borderWidth=1, borderPadding=8, backColor=HexColor('#f1f8e9'),
))
styles.add(ParagraphStyle(
    name='Warning', fontName='Helvetica-Oblique', fontSize=10,
    leading=14, leftIndent=20, spaceBefore=6, spaceAfter=6,
    textColor=HexColor('#c62828'), borderColor=HexColor('#ef9a9a'),
    borderWidth=1, borderPadding=8, backColor=HexColor('#ffebee'),
))
styles.add(ParagraphStyle(
    name='Callout', fontName='Helvetica-Oblique', fontSize=10,
    leading=14, leftIndent=20, spaceBefore=6, spaceAfter=6,
    textColor=HexColor('#1565c0'), borderColor=HexColor('#90caf9'),
    borderWidth=1, borderPadding=8, backColor=HexColor('#e3f2fd'),
))
styles.add(ParagraphStyle(
    name='FileLabel', fontName='Courier-Bold', fontSize=9,
    leading=12, spaceBefore=10, spaceAfter=2,
    textColor=HexColor('#0d47a1'),
))

S = styles

# ── Helpers ──────────────────────────────────────────────────────
def title(text):      return Paragraph(text, S['ChapterTitle'])
def section(text):    return Paragraph(text, S['SectionTitle'])
def subsection(text): return Paragraph(text, S['SubSection'])
def body(text):       return Paragraph(text, S['Body2'])
def bullet(text):     return Paragraph(f"&#8226;  {text}", S['BulletItem'])
def code(text):       return Preformatted(text, S['CodeStyle'])
def tip(text):        return Paragraph(f"TIP: {text}", S['Tip'])
def warning(text):    return Paragraph(f"WARNING: {text}", S['Warning'])
def callout(text):    return Paragraph(text, S['Callout'])
def filelabel(text):  return Paragraph(text, S['FileLabel'])
def hr():
    return HRFlowable(width="100%", thickness=0.5,
                      color=HexColor('#cccccc'),
                      spaceBefore=8, spaceAfter=8)
def sp(h=6):          return Spacer(1, h)


# ═══════════════════════════════════════════════════════════════════
# BUILD CONTENT
# ═══════════════════════════════════════════════════════════════════
story = []

# ── COVER PAGE ────────────────────────────────────────────────────
story.append(Spacer(1, 2 * inch))
story.append(Paragraph("Testing Python Modules", S['CoverTitle']))
story.append(Spacer(1, 8))
story.append(Paragraph("Explained Through the Sanskrit Book Translator", S['CoverSubtitle']))
story.append(Spacer(1, 6))
story.append(Paragraph("Every concept taught with real code from one repository", S['CoverSubtitle']))
story.append(Spacer(1, 1.5 * inch))
story.append(hr())
story.append(Spacer(1, 12))
story.append(Paragraph(
    "Covers: pytest, fixtures, mocking, async tests, thread safety,<br/>"
    "bug-hunting tests, end-to-end flows, and custom markers",
    ParagraphStyle('CoverDesc', parent=S['CoverSubtitle'], fontSize=11),
))
story.append(Spacer(1, 0.5 * inch))
story.append(Paragraph("March 2026", S['CoverSubtitle']))
story.append(PageBreak())


# ── TABLE OF CONTENTS ─────────────────────────────────────────────
story.append(title("Table of Contents"))
story.append(sp())

toc_items = [
    ("1", "Meet the Project"),
    ("2", "Test Infrastructure"),
    ("3", "Unit Testing Pure Functions"),
    ("4", "Testing Thread Safety"),
    ("5", "Data-Driven Tests (Parametrize Style)"),
    ("6", "Async Integration Tests"),
    ("7", "Mocking External APIs"),
    ("8", "Bug-Hunting Tests"),
    ("9", "End-to-End Flow Tests"),
    ("10", "Custom Markers &amp; Running Subsets"),
]

toc_data = [[Paragraph(f"<b>Chapter {n}</b>", S['Body2']),
              Paragraph(t, S['Body2'])] for n, t in toc_items]
toc_table = Table(toc_data, colWidths=[1.2 * inch, 4.5 * inch])
toc_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(toc_table)
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 1 — Meet the Project
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 1: Meet the Project"))
story.append(sp())

story.append(body(
    "Before we dive into testing, let us understand <b>what</b> we are testing. "
    "The Sanskrit Book Translator is a web application that lets users upload "
    "Sanskrit book PDFs and receive beautifully formatted English translations. "
    "The backend is built with <b>FastAPI</b> (Python) and uses the <b>Sarvam AI</b> "
    "API for optical character recognition (digitization) of Sanskrit text."
))
story.append(sp())

story.append(section("Architecture at a Glance"))
story.append(body(
    "The system has three layers:"
))
story.append(bullet("<b>Upload endpoint</b> (<i>/api/upload</i>) &mdash; receives a PDF, validates it, "
                     "extracts the page count with pdfplumber, and kicks off background digitization."))
story.append(bullet("<b>Digitization service</b> &mdash; sends the PDF to Sarvam AI, polls for completion, "
                     "downloads a ZIP of per-page HTML files, and merges them."))
story.append(bullet("<b>Job status endpoint</b> (<i>/api/jobs/&lt;id&gt;</i>) &mdash; returns the current "
                     "state of a digitization job."))
story.append(sp())

story.append(section("Folder Structure"))
story.append(code(
    "server/\n"
    "  app/\n"
    "    main.py              # FastAPI app, CORS, router registration\n"
    "    config.py            # Settings from .env (API keys, port)\n"
    "    routers/\n"
    "      upload.py          # POST /api/upload\n"
    "      jobs.py            # GET  /api/jobs/{job_id}\n"
    "    services/\n"
    "      digitize.py        # Job store, polling, HTML extraction\n"
    "      translation.py     # Placeholder translation service\n"
    "    lib/\n"
    "      supabase.py        # Supabase admin client\n"
    "  tests/\n"
    "    conftest.py          # Shared fixtures\n"
    "    test_upload.py       # Upload endpoint tests\n"
    "    test_digitize_service.py      # Unit tests for digitize.py\n"
    "    test_large_pdf_digitization.py # Bug-hunting & E2E tests\n"
    "  pytest.ini             # pytest configuration"
))
story.append(sp())

story.append(section("The Source Code Under Test"))
story.append(body(
    "There are three main source files we will be testing throughout this guide. "
    "Let us look at each one briefly."
))
story.append(sp())

story.append(subsection("1. digitize.py &mdash; The Core Service"))
story.append(body(
    "This file contains the in-memory job store (a Python dictionary guarded by a "
    "threading.Lock), the adaptive polling logic, HTML extraction from ZIP files, "
    "and the main digitization workflow that talks to the Sarvam API."
))
story.append(filelabel("server/app/services/digitize.py (key excerpts)"))
story.append(code(
    "import uuid, threading, tempfile, time, zipfile, io, re\n"
    "from pathlib import Path\n"
    "from sarvamai import SarvamAI\n"
    "from app.config import settings\n"
    "\n"
    "# In-memory job store\n"
    "jobs = {}                          # dict[str, dict]\n"
    "jobs_lock = threading.Lock()       # thread-safe access\n"
    "\n"
    "def create_job(filename, pages):\n"
    '    job_id = str(uuid.uuid4())\n'
    "    with jobs_lock:\n"
    "        jobs[job_id] = {\n"
    '            "job_id": job_id,\n'
    '            "filename": filename,\n'
    '            "pages": pages,\n'
    '            "status": "uploading",\n'
    '            "detail": "Submitting to Sarvam...",\n'
    '            "html": None,\n'
    '            "error": None,\n'
    "        }\n"
    "    return job_id\n"
    "\n"
    "def get_job(job_id):\n"
    "    with jobs_lock:\n"
    "        return jobs.get(job_id, {}).copy()  # returns a COPY\n"
    "\n"
    "def update_job(job_id, **kwargs):\n"
    "    with jobs_lock:\n"
    "        if job_id in jobs:\n"
    "            jobs[job_id].update(kwargs)"
))
story.append(callout(
    "KEY INSIGHT: <b>get_job</b> returns a <b>.copy()</b> of the job dictionary. "
    "This means external code cannot accidentally mutate the store. "
    "We will write a test to verify this in Chapter 3."
))
story.append(sp())

story.append(subsection("2. upload.py &mdash; The Upload Endpoint"))
story.append(filelabel("server/app/routers/upload.py"))
story.append(code(
    "from fastapi import APIRouter, UploadFile, HTTPException\n"
    "import pdfplumber, io\n"
    "from app.services.digitize import create_job, start_digitization\n"
    "\n"
    "router = APIRouter()\n"
    "\n"
    '@router.post("/api/upload")\n'
    "async def upload_pdf(file: UploadFile):\n"
    '    if file.content_type != "application/pdf":\n'
    '        raise HTTPException(400, detail="Only PDF files are accepted.")\n'
    "\n"
    "    contents = await file.read()\n"
    "    size = len(contents)\n"
    "\n"
    "    try:\n"
    "        with pdfplumber.open(io.BytesIO(contents)) as pdf:\n"
    "            pages = len(pdf.pages)\n"
    "    except Exception:\n"
    '        raise HTTPException(400, detail="Could not read PDF. '
    'The file may be corrupted.")\n'
    "\n"
    "    job_id = create_job(file.filename, pages)\n"
    "    start_digitization(job_id, contents)\n"
    "\n"
    '    return {"job_id": job_id, "filename": file.filename,\n'
    '            "size": size, "pages": pages, "status": "processing"}'
))
story.append(sp())

story.append(subsection("3. jobs.py &mdash; The Status Endpoint"))
story.append(filelabel("server/app/routers/jobs.py"))
story.append(code(
    "from fastapi import APIRouter, HTTPException\n"
    "from app.services.digitize import get_job\n"
    "\n"
    "router = APIRouter()\n"
    "\n"
    '@router.get("/api/jobs/{job_id}")\n'
    "def job_status(job_id: str):\n"
    "    job = get_job(job_id)\n"
    "    if not job:\n"
    '        raise HTTPException(404, detail="Job not found")\n'
    "    return job"
))
story.append(sp())

story.append(body(
    "Now that you know the application, let us set up the testing infrastructure."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 2 — Test Infrastructure
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 2: Test Infrastructure"))
story.append(sp())

story.append(body(
    "Before writing a single test, we need two pieces of infrastructure: "
    "a <b>pytest configuration file</b> and a <b>conftest.py</b> with shared fixtures. "
    "These two files form the foundation of every test in the project."
))
story.append(sp())

# ── pytest.ini ──
story.append(section("2.1 &mdash; pytest.ini"))
story.append(body(
    "pytest.ini lives at the root of the <i>server/</i> directory and tells pytest "
    "where to find tests, how to handle async code, and what custom markers exist."
))
story.append(filelabel("server/pytest.ini"))
story.append(code(
    "[pytest]\n"
    "testpaths = tests\n"
    "asyncio_mode = auto\n"
    "markers =\n"
    '    slow: marks tests as slow (deselect with \'-m "not slow"\')\n'
    "    large_pdf: marks tests that generate large PDFs"
))
story.append(sp())

story.append(subsection("Line-by-line breakdown"))
story.append(bullet("<b>testpaths = tests</b> &mdash; Tells pytest to only look in the <i>tests/</i> "
                     "directory for test files. Without this, pytest would scan every folder."))
story.append(bullet("<b>asyncio_mode = auto</b> &mdash; This is a pytest-asyncio setting. With 'auto' mode, "
                     "any <i>async def test_...</i> function is automatically treated as an async test. "
                     "Without it, you would need to manually decorate every async test with "
                     "<i>@pytest.mark.asyncio</i>."))
story.append(bullet("<b>markers</b> &mdash; Custom markers let you tag tests and run subsets. "
                     "We define <i>slow</i> and <i>large_pdf</i> here. Registering them avoids "
                     "pytest's 'unknown marker' warning."))
story.append(sp())

story.append(tip(
    "Run only fast tests: <b>pytest -m 'not slow and not large_pdf'</b>. "
    "Run only large PDF tests: <b>pytest -m large_pdf</b>. "
    "We will explore this in Chapter 10."
))
story.append(sp())

# ── conftest.py ──
story.append(section("2.2 &mdash; conftest.py: The Fixture Hub"))
story.append(body(
    "conftest.py is a <b>magic filename</b> in pytest. Any file named conftest.py is "
    "automatically loaded, and its fixtures become available to every test in that "
    "directory (and subdirectories). Our conftest.py provides five categories of fixtures."
))
story.append(sp())

story.append(subsection("Category 1: The Test Client"))
story.append(filelabel("server/tests/conftest.py"))
story.append(code(
    "import pytest\n"
    "from httpx import AsyncClient, ASGITransport\n"
    "from app.main import app\n"
    "\n"
    "@pytest.fixture\n"
    "def client():\n"
    '    """Async test client for the FastAPI app."""\n'
    "    transport = ASGITransport(app=app)\n"
    '    return AsyncClient(transport=transport, base_url="http://test")'
))
story.append(sp())
story.append(body(
    "This fixture creates an <b>httpx.AsyncClient</b> that talks directly to our FastAPI "
    "app in memory &mdash; no real HTTP server is started. The <b>ASGITransport</b> adapter "
    "connects httpx to FastAPI's ASGI interface. Any test that needs to call our API "
    "endpoints simply declares <i>client</i> as a parameter."
))
story.append(sp())

story.append(callout(
    "WHY httpx instead of requests? FastAPI is an async framework. httpx supports "
    "async HTTP calls natively, while requests does not. The ASGITransport lets us "
    "test without starting uvicorn."
))
story.append(sp())

story.append(subsection("Category 2: Job Store Cleanup (autouse)"))
story.append(code(
    "from app.services import digitize\n"
    "\n"
    "@pytest.fixture(autouse=True)\n"
    "def clean_job_store():\n"
    '    """Clear the in-memory job store before and after each test."""\n'
    "    with digitize.jobs_lock:\n"
    "        digitize.jobs.clear()\n"
    "    yield\n"
    "    with digitize.jobs_lock:\n"
    "        digitize.jobs.clear()"
))
story.append(sp())
story.append(body(
    "This is an <b>autouse fixture</b>. The <i>autouse=True</i> parameter means every test "
    "automatically uses this fixture without declaring it. It clears the in-memory job "
    "store both before and after each test, ensuring test isolation."
))
story.append(sp())
story.append(body(
    "Notice the <b>yield</b> keyword. This splits the fixture into setup (before yield) "
    "and teardown (after yield). pytest runs the code before yield, then runs the test, "
    "then runs the code after yield. This pattern is called a <b>yield fixture</b> and "
    "replaces the traditional setUp/tearDown from unittest."
))
story.append(sp())

story.append(warning(
    "Without this fixture, tests that create jobs would leave data behind, "
    "causing later tests to see unexpected jobs. Test isolation is critical."
))
story.append(sp())

story.append(subsection("Category 3: PDF Generator Function &amp; Fixtures"))
story.append(code(
    "import io\n"
    "from reportlab.lib.pagesizes import A4\n"
    "from reportlab.pdfgen import canvas\n"
    "\n"
    "def generate_pdf(num_pages=1, text_per_page='Sanskrit text sample',\n"
    "                 large_content=False):\n"
    '    """Generate a valid PDF in memory."""\n'
    "    buf = io.BytesIO()\n"
    "    c = canvas.Canvas(buf, pagesize=A4)\n"
    "    for i in range(num_pages):\n"
    "        c.drawString(72, 750, f'Page {i + 1}')\n"
    "        if large_content:\n"
    "            for line_num in range(50):\n"
    "                c.drawString(72, 720 - (line_num * 14),\n"
    "                             f'Line {line_num}: {text_per_page} ' * 3)\n"
    "        else:\n"
    "            c.drawString(72, 720, text_per_page)\n"
    "        c.showPage()\n"
    "    c.save()\n"
    "    return buf.getvalue()"
))
story.append(sp())
story.append(body(
    "This is a <b>helper function</b> (not a fixture) that creates real, valid PDF files "
    "in memory using ReportLab. It accepts parameters for page count, text content, and "
    "whether to generate large content (for testing performance). Several fixtures use it:"
))
story.append(sp())
story.append(code(
    "@pytest.fixture\n"
    "def small_pdf():\n"
    '    """A small 3-page PDF (~5 KB)."""\n'
    "    return generate_pdf(num_pages=3)\n"
    "\n"
    "@pytest.fixture\n"
    "def medium_pdf():\n"
    '    """A medium 30-page PDF."""\n'
    "    return generate_pdf(num_pages=30, text_per_page='Medium document')\n"
    "\n"
    "@pytest.fixture\n"
    "def large_pdf():\n"
    '    """A large 100-page PDF with substantial content."""\n'
    "    return generate_pdf(num_pages=100, large_content=True)\n"
    "\n"
    "@pytest.fixture\n"
    "def very_large_pdf():\n"
    '    """A very large 300-page PDF."""\n'
    "    return generate_pdf(num_pages=300, large_content=True)\n"
    "\n"
    "@pytest.fixture\n"
    "def corrupt_pdf():\n"
    '    """A file that claims to be PDF but is garbage."""\n'
    '    return b"%PDF-1.4 this is not a real pdf file\\x00\\x01\\x02"\n'
    "\n"
    "@pytest.fixture\n"
    "def not_a_pdf():\n"
    '    """A plain text file."""\n'
    '    return b"Hello, I am not a PDF."'
))
story.append(sp())
story.append(body(
    "Each fixture has a clear docstring explaining what it provides. Notice the pattern: "
    "<b>corrupt_pdf</b> starts with the PDF magic bytes (<i>%PDF-1.4</i>) but is otherwise garbage, "
    "while <b>not_a_pdf</b> is plain text. This lets us test both 'looks like PDF but is broken' "
    "and 'not a PDF at all' scenarios."
))
story.append(sp())

story.append(subsection("Category 4: ZIP Fixtures (for HTML Extraction)"))
story.append(code(
    "import zipfile\n"
    "\n"
    "def make_html_zip(pages_html):\n"
    '    """Create a ZIP containing numbered HTML files."""\n'
    "    buf = io.BytesIO()\n"
    "    with zipfile.ZipFile(buf, 'w') as zf:\n"
    "        for filename, content in pages_html:\n"
    "            zf.writestr(filename, content)\n"
    "    return buf.getvalue()\n"
    "\n"
    "@pytest.fixture\n"
    "def single_page_zip():\n"
    "    return make_html_zip([\n"
    '        ("page_1.html", "<html><head><title>P1</title></head>'
    '<body><p>Content 1</p></body></html>")\n'
    "    ])\n"
    "\n"
    "@pytest.fixture\n"
    "def multi_page_zip():\n"
    "    return make_html_zip([\n"
    '        ("page_1.html", "<html><body><p>Content 1</p></body></html>"),\n'
    '        ("page_2.html", "<html><body><p>Content 2</p></body></html>"),\n'
    '        ("page_3.html", "<html><body><p>Content 3</p></body></html>"),\n'
    "    ])\n"
    "\n"
    "@pytest.fixture\n"
    "def empty_zip():\n"
    '    """ZIP with no HTML files (only a non-HTML file)."""\n'
    "    return make_html_zip([\n"
    '        ("readme.txt", "This is not HTML"),\n'
    "    ])"
))
story.append(sp())
story.append(body(
    "These fixtures create in-memory ZIP files that simulate the output from Sarvam AI. "
    "The <b>empty_zip</b> fixture is particularly clever &mdash; it contains a file, but not "
    "an HTML file. This tests the edge case where the ZIP exists but has no usable content."
))
story.append(sp())

story.append(tip(
    "DESIGN PATTERN: Notice how <b>generate_pdf()</b> and <b>make_html_zip()</b> are regular "
    "functions, not fixtures. This lets tests call them directly with custom arguments "
    "(e.g., <i>generate_pdf(num_pages=200)</i>) while the fixtures provide convenient defaults."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 3 — Unit Testing Pure Functions
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 3: Unit Testing Pure Functions"))
story.append(sp())

story.append(body(
    "A <b>unit test</b> tests a single function in isolation. The simplest functions to "
    "unit test are <b>pure functions</b> &mdash; functions whose output depends only on their "
    "inputs, with no side effects. Our job store functions (<i>create_job</i>, <i>get_job</i>, "
    "<i>update_job</i>) are close to pure: they read and write a shared dictionary, but "
    "their behavior is deterministic and easy to verify."
))
story.append(sp())

story.append(section("3.1 &mdash; TestCreateJob: Testing Object Creation"))
story.append(body(
    "Let us start with the simplest tests. We call <i>create_job()</i> and verify what it returns."
))
story.append(filelabel("server/tests/test_digitize_service.py"))
story.append(code(
    "from app.services.digitize import create_job, get_job, update_job\n"
    "\n"
    "class TestCreateJob:\n"
    "    def test_returns_uuid_string(self):\n"
    "        job_id = create_job('test.pdf', 5)\n"
    "        assert isinstance(job_id, str)\n"
    "        assert len(job_id) == 36  # UUID format\n"
    "\n"
    "    def test_initial_status_is_uploading(self):\n"
    "        job_id = create_job('test.pdf', 5)\n"
    "        job = get_job(job_id)\n"
    '        assert job["status"] == "uploading"\n'
    "\n"
    "    def test_stores_filename_and_pages(self):\n"
    '        job_id = create_job("sanskrit_book.pdf", 42)\n'
    "        job = get_job(job_id)\n"
    '        assert job["filename"] == "sanskrit_book.pdf"\n'
    '        assert job["pages"] == 42\n'
    "\n"
    "    def test_html_and_error_initially_none(self):\n"
    '        job_id = create_job("test.pdf", 1)\n'
    "        job = get_job(job_id)\n"
    '        assert job["html"] is None\n'
    '        assert job["error"] is None\n'
    "\n"
    "    def test_multiple_jobs_independent(self):\n"
    '        id1 = create_job("a.pdf", 5)\n'
    '        id2 = create_job("b.pdf", 10)\n'
    "        assert id1 != id2\n"
    '        assert get_job(id1)["filename"] == "a.pdf"\n'
    '        assert get_job(id2)["filename"] == "b.pdf"'
))
story.append(sp())

story.append(subsection("What We Learn From These Tests"))
story.append(bullet("<b>Class-based grouping</b> &mdash; Related tests are grouped in a class "
                     "(<i>TestCreateJob</i>). pytest discovers classes starting with <i>Test</i> "
                     "and methods starting with <i>test_</i>. No inheritance needed (unlike unittest.TestCase)."))
story.append(bullet("<b>assert statements</b> &mdash; pytest uses plain Python <i>assert</i>. "
                     "If an assert fails, pytest shows a detailed diff. No need for assertEqual, "
                     "assertTrue, etc."))
story.append(bullet("<b>isinstance()</b> check &mdash; Verifies the return type. We expect a string."))
story.append(bullet("<b>len() == 36</b> &mdash; UUIDs like <i>550e8400-e29b-41d4-a716-446655440000</i> "
                     "are always 36 characters (32 hex digits + 4 hyphens)."))
story.append(bullet("<b>Testing initial state</b> &mdash; After creation, status should be 'uploading', "
                     "html and error should be None. This documents the contract."))
story.append(bullet("<b>Independence test</b> &mdash; Creating two jobs should give different IDs and "
                     "neither should affect the other."))
story.append(sp())

story.append(callout(
    "NAMING CONVENTION: Each test name describes the expected behavior: "
    "<i>test_returns_uuid_string</i>, <i>test_initial_status_is_uploading</i>. "
    "When a test fails, the name tells you exactly what broke."
))
story.append(sp())

# ── TestGetJob ──
story.append(section("3.2 &mdash; TestGetJob: Testing Retrieval &amp; Immutability"))
story.append(code(
    "class TestGetJob:\n"
    "    def test_returns_empty_dict_for_nonexistent_job(self):\n"
    '        job = get_job("nonexistent-id")\n'
    "        assert job == {}\n"
    "\n"
    "    def test_returns_copy_not_reference(self):\n"
    '        job_id = create_job("test.pdf", 1)\n'
    "        job_copy = get_job(job_id)\n"
    '        job_copy["status"] = "tampered"\n'
    "        # Original should be unchanged\n"
    '        assert get_job(job_id)["status"] == "uploading"'
))
story.append(sp())

story.append(body(
    "The second test here is particularly important. It verifies a <b>defensive programming "
    "pattern</b>: get_job() returns a copy of the dictionary, not a reference to the original. "
    "If it returned a reference, any code that modifies the returned dict would silently "
    "corrupt the job store."
))
story.append(sp())

story.append(body(
    "Let us look at the source code side by side to understand why this test exists:"
))
story.append(filelabel("Source: get_job()")
)
story.append(code(
    "def get_job(job_id):\n"
    "    with jobs_lock:\n"
    "        return jobs.get(job_id, {}).copy()  # <-- .copy() is critical"
))
story.append(sp())
story.append(body(
    "Without <i>.copy()</i>, the test would fail because modifying <i>job_copy</i> would "
    "also modify the original dictionary in the store."
))
story.append(sp())

# ── TestUpdateJob ──
story.append(section("3.3 &mdash; TestUpdateJob: Testing Mutations"))
story.append(code(
    "class TestUpdateJob:\n"
    "    def test_updates_status(self):\n"
    '        job_id = create_job("test.pdf", 1)\n'
    '        update_job(job_id, status="processing", detail="Working...")\n'
    "        job = get_job(job_id)\n"
    '        assert job["status"] == "processing"\n'
    '        assert job["detail"] == "Working..."\n'
    "\n"
    "    def test_update_nonexistent_job_does_not_crash(self):\n"
    "        # Should silently do nothing\n"
    '        update_job("fake-id", status="processing")\n'
    "\n"
    "    def test_update_preserves_other_fields(self):\n"
    '        job_id = create_job("test.pdf", 5)\n'
    '        update_job(job_id, status="completed")\n'
    "        job = get_job(job_id)\n"
    '        assert job["filename"] == "test.pdf"\n'
    '        assert job["pages"] == 5'
))
story.append(sp())

story.append(subsection("Key Testing Patterns"))
story.append(bullet("<b>Testing the no-op case</b> &mdash; <i>test_update_nonexistent_job_does_not_crash</i> "
                     "verifies that updating a non-existent job does not raise an exception. "
                     "This tests error resilience, not functionality."))
story.append(bullet("<b>Testing field preservation</b> &mdash; After updating <i>status</i>, the test "
                     "verifies that <i>filename</i> and <i>pages</i> remain unchanged. This catches "
                     "a common bug where an update accidentally overwrites the entire dictionary."))
story.append(sp())

story.append(body(
    "Let us verify this against the source code:"
))
story.append(filelabel("Source: update_job()"))
story.append(code(
    "def update_job(job_id, **kwargs):\n"
    "    with jobs_lock:\n"
    "        if job_id in jobs:        # <-- silently skips unknown IDs\n"
    "            jobs[job_id].update(kwargs)  # <-- merges, doesn't replace"
))
story.append(sp())
story.append(body(
    "The <i>dict.update(kwargs)</i> call merges the new key-value pairs into the existing "
    "dictionary, preserving all other fields. The <i>if job_id in jobs</i> guard ensures "
    "no KeyError for unknown IDs."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 4 — Testing Thread Safety
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 4: Testing Thread Safety"))
story.append(sp())

story.append(body(
    "Our digitization service uses a background <b>thread</b> to process PDFs. This means "
    "multiple threads can access the job store simultaneously. If the code is not thread-safe, "
    "jobs could be lost, corrupted, or duplicated. Testing thread safety requires a specific "
    "technique: <b>spawn many threads that all hit the same code simultaneously</b>, then "
    "verify that no data was lost or corrupted."
))
story.append(sp())

story.append(section("4.1 &mdash; Why Thread Safety Matters"))
story.append(body(
    "Our source code uses a <b>threading.Lock</b> to protect the job dictionary:"
))
story.append(filelabel("Source: digitize.py (job store)")
)
story.append(code(
    "jobs = {}                       # shared mutable state\n"
    "jobs_lock = threading.Lock()    # protects the dictionary\n"
    "\n"
    "def create_job(filename, pages):\n"
    "    job_id = str(uuid.uuid4())\n"
    "    with jobs_lock:             # <-- acquires lock\n"
    "        jobs[job_id] = { ... }  # <-- safe write\n"
    "    return job_id               # <-- lock released"
))
story.append(sp())
story.append(body(
    "Without the lock, two threads calling <i>create_job</i> at the same instant could "
    "cause a race condition. The test below verifies the lock works correctly."
))
story.append(sp())

story.append(section("4.2 &mdash; TestJobStoreThreadSafety"))
story.append(filelabel("server/tests/test_digitize_service.py"))
story.append(code(
    "import threading\n"
    "\n"
    "class TestJobStoreThreadSafety:\n"
    "    def test_concurrent_creates(self):\n"
    '        """Multiple threads creating jobs should not lose any."""\n'
    "        ids = []\n"
    "        lock = threading.Lock()\n"
    "\n"
    "        def create():\n"
    '            job_id = create_job("test.pdf", 1)\n'
    "            with lock:\n"
    "                ids.append(job_id)\n"
    "\n"
    "        threads = [threading.Thread(target=create) for _ in range(50)]\n"
    "        for t in threads:\n"
    "            t.start()\n"
    "        for t in threads:\n"
    "            t.join()\n"
    "\n"
    "        assert len(ids) == 50\n"
    "        assert len(set(ids)) == 50  # All unique"
))
story.append(sp())

story.append(subsection("Line-by-line walkthrough"))
story.append(bullet("<b>ids = []</b> and <b>lock = threading.Lock()</b> &mdash; "
                     "We create a local list to collect job IDs and a lock to protect it. "
                     "Note: this is a <i>test-side</i> lock, separate from the production lock."))
story.append(bullet("<b>def create()</b> &mdash; Each thread runs this function: create a job, "
                     "then safely append the ID to our collection list."))
story.append(bullet("<b>range(50)</b> &mdash; We spawn 50 threads. This is enough to trigger "
                     "race conditions if the production code is not thread-safe."))
story.append(bullet("<b>t.start()</b> &mdash; Launches all threads. They run concurrently."))
story.append(bullet("<b>t.join()</b> &mdash; Waits for all threads to finish before asserting."))
story.append(bullet("<b>assert len(ids) == 50</b> &mdash; Verifies no jobs were lost."))
story.append(bullet("<b>assert len(set(ids)) == 50</b> &mdash; Verifies all UUIDs are unique. "
                     "Converting to a set removes duplicates; if the count matches, there are no duplicates."))
story.append(sp())

story.append(section("4.3 &mdash; Concurrent Updates"))
story.append(code(
    "    def test_concurrent_updates(self):\n"
    '        """Multiple threads updating the same job should not corrupt it."""\n'
    '        job_id = create_job("test.pdf", 1)\n'
    "\n"
    "        def updater(n):\n"
    '            update_job(job_id, detail=f"Update {n}")\n'
    "\n"
    "        threads = [threading.Thread(target=updater, args=(i,))\n"
    "                   for i in range(50)]\n"
    "        for t in threads:\n"
    "            t.start()\n"
    "        for t in threads:\n"
    "            t.join()\n"
    "\n"
    "        job = get_job(job_id)\n"
    '        assert job["detail"].startswith("Update ")'
))
story.append(sp())
story.append(body(
    "This test creates one job and then has 50 threads update its <i>detail</i> field "
    "simultaneously. We do not know <i>which</i> thread's update will 'win' (that depends on "
    "OS scheduling), but we assert that the final value is a valid update string &mdash; not "
    "garbage, not None, not a partial write."
))
story.append(sp())

story.append(callout(
    "TESTING INSIGHT: Thread safety tests are <b>probabilistic</b>. A passing test "
    "does not <i>prove</i> thread safety (the race condition might not trigger every run), "
    "but a failing test definitely proves a bug exists. Running with more threads "
    "or in a loop increases confidence."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 5 — Data-Driven Tests (Parametrize Style)
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 5: Data-Driven Tests"))
story.append(sp())

story.append(body(
    "When a function has clearly defined input/output boundaries, you often want to "
    "test multiple input scenarios. Instead of writing a separate test for each, you "
    "can use <b>data-driven testing</b> &mdash; writing one test structure and feeding it "
    "multiple data points. Our <i>TestAdaptivePollInterval</i> class demonstrates this "
    "pattern, even without using <i>@pytest.mark.parametrize</i> explicitly."
))
story.append(sp())

story.append(section("5.1 &mdash; The Function Under Test"))
story.append(body(
    "The <i>adaptive_poll_interval</i> function decides how long to wait between polls "
    "based on how much time has elapsed and how many pages the document has."
))
story.append(filelabel("Source: digitize.py"))
story.append(code(
    "def adaptive_poll_interval(elapsed, total_pages):\n"
    "    if total_pages < 10:      # Small documents\n"
    "        return 5.0            # Always 5 seconds\n"
    "    if elapsed < 30:          # Large docs, early phase\n"
    "        return 5.0\n"
    "    elif elapsed < 300:       # Large docs, mid phase\n"
    "        return 10.0\n"
    "    else:                     # Large docs, late phase\n"
    "        return 15.0"
))
story.append(sp())
story.append(body(
    "This function has a clear decision tree with exact boundary values. It is a "
    "perfect candidate for boundary value testing."
))
story.append(sp())

story.append(section("5.2 &mdash; TestAdaptivePollInterval"))
story.append(filelabel("server/tests/test_digitize_service.py"))
story.append(code(
    "class TestAdaptivePollInterval:\n"
    "    def test_small_doc_always_5s(self):\n"
    '        """Documents under 10 pages should always poll at 5s."""\n'
    "        assert adaptive_poll_interval(0, 5) == 5.0\n"
    "        assert adaptive_poll_interval(100, 5) == 5.0\n"
    "        assert adaptive_poll_interval(500, 5) == 5.0\n"
    "\n"
    "    def test_large_doc_early_5s(self):\n"
    '        """Large docs poll at 5s for the first 30 seconds."""\n'
    "        assert adaptive_poll_interval(0, 50) == 5.0\n"
    "        assert adaptive_poll_interval(29, 50) == 5.0\n"
    "\n"
    "    def test_large_doc_mid_10s(self):\n"
    '        """Large docs poll at 10s between 30-300 seconds."""\n'
    "        assert adaptive_poll_interval(30, 50) == 10.0\n"
    "        assert adaptive_poll_interval(150, 50) == 10.0\n"
    "        assert adaptive_poll_interval(299, 50) == 10.0\n"
    "\n"
    "    def test_large_doc_late_15s(self):\n"
    '        """Large docs poll at 15s after 300 seconds."""\n'
    "        assert adaptive_poll_interval(300, 50) == 15.0\n"
    "        assert adaptive_poll_interval(600, 50) == 15.0\n"
    "\n"
    "    def test_boundary_at_10_pages(self):\n"
    '        """10 pages is the threshold for adaptive polling."""\n'
    "        # 9 pages = always 5s\n"
    "        assert adaptive_poll_interval(100, 9) == 5.0\n"
    "        # 10 pages = adaptive (should be 10s at 100 elapsed)\n"
    "        assert adaptive_poll_interval(100, 10) == 10.0"
))
story.append(sp())

story.append(subsection("Boundary Value Analysis"))
story.append(body(
    "Each test method targets a specific region of the decision tree:"
))
story.append(sp())

boundary_data = [
    ["Test", "Input Range", "Expected", "Why"],
    ["small_doc_always_5s", "pages &lt; 10", "5.0", "Small docs don't need adaptive polling"],
    ["large_doc_early_5s", "pages >= 10, elapsed &lt; 30", "5.0", "Poll frequently at first"],
    ["large_doc_mid_10s", "pages >= 10, 30 &lt;= elapsed &lt; 300", "10.0", "Slow down in middle"],
    ["large_doc_late_15s", "pages >= 10, elapsed >= 300", "15.0", "Slow down further after 5 min"],
    ["boundary_at_10_pages", "pages = 9 vs 10", "5.0 vs 10.0", "Tests exact boundary"],
]
bt = Table(boundary_data, colWidths=[1.6*inch, 1.8*inch, 0.8*inch, 1.8*inch])
bt.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8.5),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(bt)
story.append(sp())

story.append(subsection("How This Could Use @pytest.mark.parametrize"))
story.append(body(
    "The same tests could be written with <i>@pytest.mark.parametrize</i> to reduce repetition. "
    "Here is how you would refactor:"
))
story.append(code(
    "import pytest\n"
    "\n"
    "@pytest.mark.parametrize('elapsed, pages, expected', [\n"
    "    (0,   5,  5.0),   # small doc\n"
    "    (100, 5,  5.0),   # small doc, any elapsed\n"
    "    (0,   50, 5.0),   # large doc, early\n"
    "    (29,  50, 5.0),   # large doc, just before boundary\n"
    "    (30,  50, 10.0),  # large doc, at boundary\n"
    "    (150, 50, 10.0),  # large doc, mid\n"
    "    (299, 50, 10.0),  # large doc, just before late\n"
    "    (300, 50, 15.0),  # large doc, at late boundary\n"
    "    (600, 50, 15.0),  # large doc, well into late\n"
    "])\n"
    "def test_adaptive_poll(elapsed, pages, expected):\n"
    "    assert adaptive_poll_interval(elapsed, pages) == expected"
))
story.append(sp())

story.append(body(
    "Both approaches are valid. The class-based approach in our codebase groups tests by "
    "scenario (small doc, early, mid, late, boundary). The parametrize approach runs all "
    "data points as separate test cases. Choose based on readability."
))
story.append(sp())

story.append(tip(
    "BOUNDARY VALUE TESTING: Always test <b>at</b> the boundary (30, 300), "
    "<b>just below</b> (29, 299), and <b>just above</b> (31, 301). "
    "Off-by-one errors are the most common bugs in boundary logic."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 6 — Async Integration Tests
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 6: Async Integration Tests"))
story.append(sp())

story.append(body(
    "Unit tests verify individual functions. <b>Integration tests</b> verify that multiple "
    "components work together. In our case, this means testing the <b>HTTP endpoints</b> &mdash; "
    "sending a request to <i>/api/upload</i> and checking that the response is correct. "
    "Since FastAPI is an async framework, our integration tests use <b>async/await</b>."
))
story.append(sp())

story.append(section("6.1 &mdash; The Async Test Setup"))
story.append(body(
    "Remember the <i>client</i> fixture from Chapter 2:"
))
story.append(code(
    "@pytest.fixture\n"
    "def client():\n"
    "    transport = ASGITransport(app=app)\n"
    '    return AsyncClient(transport=transport, base_url="http://test")'
))
story.append(sp())
story.append(body(
    "Combined with <i>asyncio_mode = auto</i> in pytest.ini, any async test function "
    "that declares <i>client</i> as a parameter gets the async test client injected automatically."
))
story.append(sp())

story.append(section("6.2 &mdash; TestUploadValidation: Rejection Tests"))
story.append(filelabel("server/tests/test_upload.py"))
story.append(code(
    "import pytest\n"
    "from unittest.mock import patch, MagicMock\n"
    "\n"
    "class TestUploadValidation:\n"
    "    @pytest.mark.asyncio\n"
    "    async def test_rejects_non_pdf_content_type(self, client):\n"
    '        """Non-PDF files should be rejected with 400."""\n'
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("test.txt", b"hello world", "text/plain")},\n'
    "        )\n"
    "        assert response.status_code == 400\n"
    '        assert "Only PDF" in response.json()["detail"]\n'
    "\n"
    "    @pytest.mark.asyncio\n"
    "    async def test_rejects_corrupted_pdf(self, client, corrupt_pdf):\n"
    '        """Corrupted PDFs should be rejected with 400."""\n'
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("corrupt.pdf", corrupt_pdf, "application/pdf")},\n'
    "        )\n"
    "        assert response.status_code == 400\n"
    '        assert "corrupted" in response.json()["detail"].lower()\n'
    "\n"
    "    @pytest.mark.asyncio\n"
    "    async def test_rejects_empty_pdf(self, client):\n"
    '        """Empty bytes with PDF content type should be rejected."""\n'
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("empty.pdf", b"", "application/pdf")},\n'
    "        )\n"
    "        assert response.status_code == 400"
))
story.append(sp())

story.append(subsection("Key Concepts Introduced"))
story.append(bullet("<b>@pytest.mark.asyncio</b> &mdash; Marks a test as asynchronous. "
                     "With <i>asyncio_mode = auto</i> in pytest.ini this decorator is technically "
                     "optional, but we include it for clarity."))
story.append(bullet("<b>async def test_...</b> &mdash; The test function is a coroutine. "
                     "pytest-asyncio creates an event loop and runs it."))
story.append(bullet("<b>await client.post(...)</b> &mdash; Sends an async HTTP POST request "
                     "to our FastAPI app (in-memory, no real network)."))
story.append(bullet('<b>files={"file": (name, data, content_type)}</b> &mdash; '
                     "httpx file upload syntax. The tuple is (filename, content_bytes, MIME type). "
                     "This mimics a real browser file upload."))
story.append(bullet("<b>response.status_code</b> and <b>response.json()</b> &mdash; "
                     "Standard httpx response methods. We check both the status code and the "
                     "error message in the JSON body."))
story.append(sp())

story.append(callout(
    "TESTING STRATEGY: We test three rejection cases &mdash; wrong content type, "
    "corrupted PDF, and empty file. Each hits a different validation branch in "
    "the upload endpoint. This ensures all error paths are covered."
))
story.append(sp())

story.append(section("6.3 &mdash; TestSuccessfulUpload: Happy Path"))
story.append(code(
    "class TestSuccessfulUpload:\n"
    "    @pytest.mark.asyncio\n"
    '    @patch("app.routers.upload.start_digitization")\n'
    "    async def test_small_pdf_upload_returns_job(\n"
    "            self, mock_start, client, small_pdf):\n"
    '        """A valid small PDF should return a job with status \'processing\'."""\n'
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("small.pdf", small_pdf, "application/pdf")},\n'
    "        )\n"
    "        assert response.status_code == 200\n"
    "        data = response.json()\n"
    '        assert "job_id" in data\n'
    '        assert data["filename"] == "small.pdf"\n'
    '        assert data["pages"] == 3\n'
    '        assert data["status"] == "processing"\n'
    '        assert data["size"] == len(small_pdf)\n'
    "        mock_start.assert_called_once()"
))
story.append(sp())

story.append(subsection("Why @patch start_digitization?"))
story.append(body(
    "The upload endpoint calls <i>start_digitization(job_id, contents)</i> which spawns a "
    "background thread to talk to the Sarvam API. In our integration test, we do NOT want "
    "to actually contact the Sarvam API. So we <b>patch</b> (replace) <i>start_digitization</i> "
    "with a mock that does nothing."
))
story.append(sp())
story.append(body(
    "The decorator <i>@patch('app.routers.upload.start_digitization')</i> replaces the "
    "function at the location where it is <b>imported</b>, not where it is defined. "
    "Since upload.py does <i>from app.services.digitize import start_digitization</i>, "
    "the patch target is <i>app.routers.upload.start_digitization</i>."
))
story.append(sp())

story.append(warning(
    "COMMON MISTAKE: Patching where the function is <b>defined</b> "
    "(<i>app.services.digitize.start_digitization</i>) instead of where it is "
    "<b>imported</b> (<i>app.routers.upload.start_digitization</i>). "
    "The patch must target the name as it appears in the module under test."
))
story.append(sp())

story.append(subsection("Parameter Order With @patch"))
story.append(body(
    "Notice the method signature: <i>async def test_...(self, mock_start, client, small_pdf)</i>. "
    "When you use <i>@patch</i> as a decorator, the mock is injected as an <b>extra parameter</b> "
    "after <i>self</i> but <b>before</b> the fixtures. This is a common source of confusion. "
    "The rule is: <i>@patch</i> parameters are injected first (innermost decorator = first param), "
    "then pytest fixtures follow."
))
story.append(sp())

story.append(section("6.4 &mdash; TestJobStatus: Endpoint Chaining"))
story.append(code(
    "class TestJobStatus:\n"
    "    @pytest.mark.asyncio\n"
    "    async def test_nonexistent_job_returns_404(self, client):\n"
    '        response = await client.get("/api/jobs/nonexistent-id")\n'
    "        assert response.status_code == 404\n"
    "\n"
    "    @pytest.mark.asyncio\n"
    '    @patch("app.routers.upload.start_digitization")\n'
    "    async def test_job_status_after_upload(\n"
    "            self, mock_start, client, small_pdf):\n"
    '        """After upload, job should be retrievable via status endpoint."""\n'
    "        upload_resp = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("test.pdf", small_pdf, "application/pdf")},\n'
    "        )\n"
    '        job_id = upload_resp.json()["job_id"]\n'
    "\n"
    '        status_resp = await client.get(f"/api/jobs/{job_id}")\n'
    "        assert status_resp.status_code == 200\n"
    "        data = status_resp.json()\n"
    '        assert data["job_id"] == job_id\n'
    '        assert data["filename"] == "test.pdf"'
))
story.append(sp())
story.append(body(
    "This test chains two API calls: first upload a PDF, then query the job status. "
    "It verifies that the upload creates a job and the status endpoint can retrieve it. "
    "This is a mini <b>integration test</b> &mdash; testing two endpoints working together."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 7 — Mocking External APIs
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 7: Mocking External APIs"))
story.append(sp())

story.append(body(
    "Our digitization service calls the <b>Sarvam AI API</b> &mdash; an external service "
    "that we cannot control in tests. We do not want tests to make real API calls because: "
    "(1) they would be slow, (2) they would cost money, (3) they would be flaky if the "
    "API is down. The solution is <b>mocking</b>: replacing the real Sarvam client with "
    "a fake object that behaves exactly how we tell it to."
))
story.append(sp())

story.append(section("7.1 &mdash; The Mock Toolbox"))
story.append(body("Python's <i>unittest.mock</i> module provides three key tools:"))
story.append(sp())

mock_tools = [
    ["Tool", "What It Does", "When to Use"],
    ["@patch(target)", "Replaces target with a MagicMock\nduring the test", "When you need to replace\na module-level import"],
    ["MagicMock()", "A fake object that records\nall calls made to it", "When you need a fake\nobject with attributes"],
    ["side_effect", "Controls what happens when\nthe mock is called", "When you need the mock to\nraise errors or return\ndifferent values per call"],
    ["return_value", "Sets the value returned\nwhen the mock is called", "When you need a fixed\nreturn value"],
]
mt = Table(mock_tools, colWidths=[1.5*inch, 2.2*inch, 2.2*inch])
mt.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8.5),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(mt)
story.append(sp())

story.append(section("7.2 &mdash; The Sarvam Mock Chain"))
story.append(body(
    "The real Sarvam API call chain in <i>run_digitization()</i> looks like this:"
))
story.append(code(
    "# Real call chain in run_digitization():\n"
    "client = SarvamAI(api_subscription_key=settings.SARVAM_API_KEY)\n"
    "sarvam_job = client.document_intelligence.create_job(...)\n"
    "sarvam_job.upload_file(tmp_path)\n"
    "sarvam_job.start()\n"
    "status = sarvam_job.get_status()\n"
    "sarvam_job.download_output(zip_path)"
))
story.append(sp())
story.append(body(
    "To mock this entire chain, we need to replace <i>SarvamAI</i> and configure the "
    "mock to return objects at each step. Here is how:"
))
story.append(sp())

story.append(filelabel("server/tests/test_large_pdf_digitization.py (successful flow mock)"))
story.append(code(
    "from unittest.mock import patch, MagicMock\n"
    "from pathlib import Path\n"
    "\n"
    "@patch('app.services.digitize.time.sleep')    # Don't actually sleep\n"
    "@patch('app.services.digitize.SarvamAI')       # Replace the class\n"
    "def test_successful_flow(mock_sarvam_class, mock_sleep):\n"
    "    # Step 1: SarvamAI() returns a mock client\n"
    "    mock_client = MagicMock()\n"
    "    mock_sarvam_class.return_value = mock_client\n"
    "\n"
    "    # Step 2: client.document_intelligence.create_job() returns mock_job\n"
    "    mock_job = MagicMock()\n"
    "    mock_client.document_intelligence.create_job.return_value = mock_job\n"
    "\n"
    "    # Step 3: mock_job.get_status() returns 'Completed'\n"
    "    status_complete = MagicMock()\n"
    '    status_complete.job_state = "Completed"\n'
    "    mock_job.get_status.return_value = status_complete\n"
    "\n"
    "    # Step 4: mock_job.download_output() writes a ZIP file to disk\n"
    "    def fake_download(path):\n"
    "        Path(path).write_bytes(zip_bytes)  # pre-built ZIP\n"
    "    mock_job.download_output.side_effect = fake_download"
))
story.append(sp())

story.append(subsection("Breaking Down the Mock Chain"))
story.append(bullet("<b>@patch('app.services.digitize.SarvamAI')</b> &mdash; Replaces the "
                     "SarvamAI class wherever it is used in digitize.py. Every call to SarvamAI(...) "
                     "now returns a MagicMock."))
story.append(bullet("<b>mock_sarvam_class.return_value = mock_client</b> &mdash; When the code calls "
                     "<i>SarvamAI(api_subscription_key=...)</i>, it gets <i>mock_client</i> back."))
story.append(bullet("<b>mock_client.document_intelligence.create_job.return_value = mock_job</b> &mdash; "
                     "Chained attribute access. MagicMock automatically creates attributes on demand. "
                     "We configure create_job to return our mock_job."))
story.append(bullet("<b>status_complete.job_state = 'Completed'</b> &mdash; We set an attribute on "
                     "the mock to simulate a completed job status."))
story.append(bullet("<b>mock_job.download_output.side_effect = fake_download</b> &mdash; "
                     "side_effect lets us run a custom function when download_output is called. "
                     "Our fake writes a pre-built ZIP file to disk, simulating a real download."))
story.append(sp())

story.append(section("7.3 &mdash; Mocking Failures With side_effect"))
story.append(body(
    "side_effect is also used to simulate API failures. Here is how we test what happens "
    "when the Sarvam upload fails:"
))
story.append(code(
    "@patch('app.services.digitize.SarvamAI')\n"
    "def test_sarvam_upload_file_failure(mock_sarvam_class):\n"
    '    job_id = create_job("huge.pdf", 500)\n'
    "    pdf_bytes = generate_pdf(num_pages=5)\n"
    "\n"
    "    mock_client = MagicMock()\n"
    "    mock_sarvam_class.return_value = mock_client\n"
    "    mock_job = MagicMock()\n"
    "    mock_client.document_intelligence.create_job.return_value = mock_job\n"
    "\n"
    "    # upload_file raises an exception\n"
    "    mock_job.upload_file.side_effect = Exception(\n"
    '        "File too large: maximum 50MB allowed"\n'
    "    )\n"
    "\n"
    "    run_digitization(job_id, pdf_bytes)\n"
    "\n"
    "    job = get_job(job_id)\n"
    '    assert job["status"] == "failed"\n'
    '    assert "too large" in job["error"].lower()'
))
story.append(sp())
story.append(body(
    "Here, <b>side_effect = Exception(...)</b> makes the mock <i>raise</i> an exception "
    "when called. This simulates the Sarvam API rejecting a file that is too large."
))
story.append(sp())

story.append(section("7.4 &mdash; Mocking Sequential Responses"))
story.append(body(
    "Sometimes an API returns different responses on successive calls. Use "
    "<i>side_effect</i> with a <b>list</b> to return different values each time:"
))
story.append(code(
    "# First call: InProgress, second call: PartiallyCompleted\n"
    "status_inprog = MagicMock()\n"
    'status_inprog.job_state = "InProgress"\n'
    "status_partial = MagicMock()\n"
    'status_partial.job_state = "PartiallyCompleted"\n'
    "mock_job.get_status.side_effect = [status_inprog, status_partial]"
))
story.append(sp())
story.append(body(
    "The first call to <i>get_status()</i> returns <i>status_inprog</i>. The second "
    "call returns <i>status_partial</i>. This simulates a job that goes from 'processing' "
    "to 'partially completed' after one polling cycle."
))
story.append(sp())

story.append(section("7.5 &mdash; Verifying Mock Calls"))
story.append(body(
    "After running the code under test, you can verify how the mock was called:"
))
story.append(code(
    "# Was it called at all?\n"
    "mock_start.assert_called_once()\n"
    "\n"
    "# Was it NOT called?\n"
    "mock_sleep.assert_not_called()\n"
    "\n"
    "# What arguments was it called with?\n"
    "sleep_calls = [call.args[0] for call in mock_sleep.call_args_list]\n"
    "assert sleep_calls == [4, 8, 16, 32]  # exponential backoff"
))
story.append(sp())

story.append(tip(
    "MOCK VERIFICATION TIP: <b>assert_called_once()</b> verifies the mock was called "
    "exactly once. <b>call_args_list</b> gives you every call with its arguments. "
    "This lets you verify not just <i>that</i> a function was called, but <i>how</i>."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 8 — Bug-Hunting Tests
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 8: Bug-Hunting Tests"))
story.append(sp())

story.append(body(
    "One of the most valuable uses of tests is <b>documenting known bugs</b>. Our test "
    "suite includes seven test classes that each target a specific, documented bug in the "
    "codebase. These tests serve three purposes: (1) they prove the bug exists, (2) they "
    "document the expected behavior, and (3) they will automatically pass when the bug is fixed."
))
story.append(sp())

story.append(section("8.1 &mdash; BUG #1: No Polling Timeout (Infinite Loop)"))
story.append(body(
    "The <i>run_digitization</i> function polls Sarvam with a <i>while True</i> loop. "
    "If Sarvam never returns 'Completed', the thread polls <b>forever</b>."
))
story.append(filelabel("Source: digitize.py (the bug)"))
story.append(code(
    "# This loop has NO exit condition for timeouts:\n"
    "while True:                          # <-- INFINITE LOOP\n"
    "    status_resp = sarvam_job.get_status()\n"
    "    job_state = status_resp.job_state\n"
    "    if job_state in ('Completed', 'PartiallyCompleted'):\n"
    "        break\n"
    "    elif job_state == 'Failed':\n"
    "        raise Exception('...')\n"
    "    time.sleep(interval)             # <-- polls forever"
))
story.append(sp())

story.append(filelabel("Test: test_large_pdf_digitization.py"))
story.append(code(
    "class TestPollingTimeout:\n"
    '    """The while True loop has NO timeout.\n'
    "    If Sarvam never completes, the thread polls forever.\"\"\"\n"
    "\n"
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_polling_should_timeout_for_stuck_jobs(\n"
    "            self, mock_sarvam_class):\n"
    '        job_id = create_job("stuck.pdf", 10)\n'
    "        pdf_bytes = generate_pdf(num_pages=10)\n"
    "\n"
    "        # Mock Sarvam to ALWAYS return 'InProgress'\n"
    "        mock_client = MagicMock()\n"
    "        mock_sarvam_class.return_value = mock_client\n"
    "        mock_job = MagicMock()\n"
    "        mock_client.document_intelligence.create_job.return_value = mock_job\n"
    "        status_mock = MagicMock()\n"
    '        status_mock.job_state = "InProgress"\n'
    "        mock_job.get_status.return_value = status_mock\n"
    "\n"
    "        # Run in a thread with a timeout (prevents real infinite loop)\n"
    "        thread = threading.Thread(target=lambda:\n"
    "            run_digitization(job_id, pdf_bytes), daemon=True)\n"
    "        thread.start()\n"
    "        thread.join(timeout=15)  # Wait max 15 seconds\n"
    "\n"
    "        if thread.is_alive():\n"
    "            # Thread is STILL running = BUG CONFIRMED\n"
    '            job = get_job(job_id)\n'
    '            assert job["status"] != "failed"'
))
story.append(sp())
story.append(body(
    "The test spawns the digitization in a separate thread with a 15-second timeout. "
    "If the thread is still alive after 15 seconds, it means the <i>while True</i> loop "
    "is stuck &mdash; confirming the bug."
))
story.append(sp())

story.append(subsection("Source Code Inspection Test"))
story.append(code(
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_should_have_max_polling_duration(\n"
    "            self, mock_sarvam_class):\n"
    "        import inspect\n"
    "        source = inspect.getsource(run_digitization)\n"
    "\n"
    "        has_timeout = any(term in source.lower() for term in [\n"
    "            'max_poll', 'timeout', 'max_duration', 'max_wait',\n"
    "            'deadline', 'max_elapsed', 'time_limit',\n"
    "        ])\n"
    "\n"
    "        assert not has_timeout, \\\n"
    '            "Good news: a polling timeout was added!"'
))
story.append(sp())
story.append(body(
    "This is an unusual but effective pattern: using <b>inspect.getsource()</b> to read "
    "the actual source code and check whether it contains timeout-related keywords. "
    "The assertion is <i>inverted</i> &mdash; it asserts the bug <b>exists</b>. When someone "
    "fixes the bug, this test will fail with the message 'Good news: a polling timeout was added!', "
    "signaling that the test should be updated."
))
story.append(sp())

story.append(section("8.2 &mdash; BUG #2: No Server-Side File Size Limit"))
story.append(code(
    "class TestServerSideFileSizeLimit:\n"
    '    """Upload endpoint has NO server-side file size validation.\n'
    "    Only the client enforces 300MB.\"\"\"\n"
    "\n"
    "    @pytest.mark.asyncio\n"
    '    @patch("app.routers.upload.start_digitization")\n'
    "    async def test_no_server_side_size_limit_exists(\n"
    "            self, mock_start, client):\n"
    "        import inspect\n"
    "        from app.routers.upload import upload_pdf\n"
    "        source = inspect.getsource(upload_pdf)\n"
    "\n"
    "        has_size_check = any(term in source.lower() for term in [\n"
    "            'max_size', 'file_size', 'content_length',\n"
    "            'size_limit', 'too large',\n"
    "        ])\n"
    "\n"
    "        assert not has_size_check, \\\n"
    '            "Good news: a server-side size limit was added!"\n'
    "\n"
    "    @pytest.mark.asyncio\n"
    '    @patch("app.routers.upload.start_digitization")\n'
    "    async def test_server_accepts_arbitrarily_large_pdf(\n"
    "            self, mock_start, client):\n"
    "        large_pdf = generate_pdf(num_pages=200, large_content=True)\n"
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("huge.pdf", large_pdf, "application/pdf")},\n'
    "        )\n"
    "        # This SHOULD be rejected but currently is not\n"
    "        assert response.status_code == 200"
))
story.append(sp())
story.append(body(
    "The second test demonstrates the bug by uploading a 200-page PDF and verifying it is "
    "accepted (HTTP 200). The comment 'This SHOULD be rejected' documents the intent &mdash; "
    "a future fix would add a size limit, and this test would need to assert a 413 or 400 status."
))
story.append(sp())

story.append(section("8.3 &mdash; BUG #4: Temp File Cleanup on Failure"))
story.append(code(
    "class TestTempFileCleanup:\n"
    '    """Temp files are created but only cleaned up in the success path."""\n'
    "\n"
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_temp_file_leaks_on_sarvam_api_failure(\n"
    "            self, mock_sarvam_class):\n"
    '        job_id = create_job("test.pdf", 5)\n'
    "        pdf_bytes = generate_pdf(num_pages=5)\n"
    "\n"
    "        mock_client = MagicMock()\n"
    "        mock_sarvam_class.return_value = mock_client\n"
    "        mock_client.document_intelligence.create_job.side_effect = \\\n"
    '            Exception("API unavailable")\n'
    "\n"
    "        # Count temp PDF files BEFORE\n"
    "        temp_dir = tempfile.gettempdir()\n"
    "        pdf_temps_before = set(\n"
    "            f for f in os.listdir(temp_dir) if f.endswith('.pdf')\n"
    "        )\n"
    "\n"
    "        run_digitization(job_id, pdf_bytes)\n"
    "\n"
    "        # Count temp PDF files AFTER\n"
    "        pdf_temps_after = set(\n"
    "            f for f in os.listdir(temp_dir) if f.endswith('.pdf')\n"
    "        )\n"
    "        leaked = pdf_temps_after - pdf_temps_before\n"
    "\n"
    "        if leaked:\n"
    "            # Clean up ourselves\n"
    "            for f in leaked:\n"
    "                os.unlink(os.path.join(temp_dir, f))\n"
    "            print(f'BUG: {len(leaked)} temp file(s) leaked')"
))
story.append(sp())
story.append(body(
    "This test uses a creative approach: it counts the temp files <b>before</b> and <b>after</b> "
    "running the function, then checks if any new files appeared. The set difference "
    "(<i>pdf_temps_after - pdf_temps_before</i>) gives us the leaked files. "
    "The test even cleans up the leaked files to avoid polluting the test environment."
))
story.append(sp())

story.append(section("8.4 &mdash; BUG #5: Rate Limit Retry With Exponential Backoff"))
story.append(code(
    "class TestRateLimitHandling:\n"
    "    @patch('app.services.digitize.time.sleep')  # Don't really sleep\n"
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_rate_limit_retries_use_exponential_backoff(\n"
    "            self, mock_sarvam_class, mock_sleep):\n"
    '        job_id = create_job("test.pdf", 5)\n'
    "        pdf_bytes = generate_pdf(num_pages=5)\n"
    "\n"
    "        mock_client = MagicMock()\n"
    "        mock_sarvam_class.return_value = mock_client\n"
    "        mock_client.document_intelligence.create_job.side_effect = \\\n"
    '            Exception("429 rate limit")\n'
    "\n"
    "        run_digitization(job_id, pdf_bytes)\n"
    "\n"
    "        # Verify exponential backoff intervals\n"
    "        sleep_calls = [call.args[0]\n"
    "                       for call in mock_sleep.call_args_list]\n"
    "        assert len(sleep_calls) == 4    # 4 retries\n"
    "        assert sleep_calls == [4, 8, 16, 32]  # 2^(attempt+2)"
))
story.append(sp())
story.append(body(
    "This test verifies the <b>exact backoff intervals</b> by patching <i>time.sleep</i> "
    "and inspecting its call arguments. The mock records every call, so after the test, "
    "we can extract the sleep durations and assert they follow the 4-8-16-32 pattern."
))
story.append(sp())

story.append(subsection("Non-Rate-Limit Errors Fail Immediately"))
story.append(code(
    "    @patch('app.services.digitize.time.sleep')\n"
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_non_rate_limit_error_fails_immediately(\n"
    "            self, mock_sarvam_class, mock_sleep):\n"
    "        # ...\n"
    "        mock_client.document_intelligence.create_job.side_effect = \\\n"
    '            Exception("Invalid API key")\n'
    "\n"
    "        run_digitization(job_id, pdf_bytes)\n"
    "\n"
    "        job = get_job(job_id)\n"
    '        assert job["status"] == "failed"\n'
    "        mock_sleep.assert_not_called()  # No retries!"
))
story.append(sp())
story.append(body(
    "This is the counterpart: when the error is NOT a rate limit (no '429' or 'rate limit' "
    "in the message), the function should fail immediately without retrying. We verify this "
    "by asserting <i>mock_sleep.assert_not_called()</i>."
))
story.append(sp())

story.append(section("8.5 &mdash; BUG #7: Memory Handling"))
story.append(code(
    "class TestMemoryHandling:\n"
    "    def test_pdf_bytes_passed_by_reference_to_thread(self):\n"
    '        """PDF bytes stay in memory during entire processing."""\n'
    "        import inspect\n"
    "        from app.services.digitize import start_digitization\n"
    "        source = inspect.getsource(start_digitization)\n"
    '        assert "pdf_bytes" in source\n'
    "\n"
    "        run_source = inspect.getsource(run_digitization)\n"
    '        assert "tmp.write(pdf_bytes)" in run_source\n'
    "\n"
    "        # After writing to temp file, bytes should be freed\n"
    '        has_explicit_cleanup = "del pdf_bytes" in run_source\n'
    "        assert not has_explicit_cleanup, \\\n"
    '            "BUG: pdf_bytes not freed after writing to temp file"'
))
story.append(sp())
story.append(body(
    "This test uses source code inspection to verify that <i>pdf_bytes</i> is never "
    "explicitly freed with <i>del pdf_bytes</i> after being written to a temp file. "
    "For a 100MB PDF, this means 100MB stays in memory even though the data is already "
    "on disk &mdash; effectively doubling memory usage."
))
story.append(sp())

story.append(callout(
    "PATTERN: Bug-hunting tests can use <b>inverted assertions</b> (assert the bug "
    "exists) or <b>source inspection</b> (check the code for missing features). "
    "When the bug is fixed, the test fails with a descriptive message, prompting "
    "a developer to update the test."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 9 — End-to-End Flow Tests
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 9: End-to-End Flow Tests"))
story.append(sp())

story.append(body(
    "An <b>end-to-end (E2E) test</b> exercises the entire workflow from start to finish. "
    "In our case, this means: create a job, run the full digitization pipeline (with mocked "
    "Sarvam API), and verify the final output. E2E tests require coordinating multiple "
    "mocks to work together seamlessly."
))
story.append(sp())

story.append(section("9.1 &mdash; TestDigitizationFlow: Happy Path"))
story.append(filelabel("server/tests/test_large_pdf_digitization.py"))
story.append(code(
    "class TestDigitizationFlow:\n"
    "    @patch('app.services.digitize.time.sleep')\n"
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_successful_small_pdf_flow(\n"
    "            self, mock_sarvam_class, mock_sleep):\n"
    '        """Full happy path: upload -> process -> complete."""\n'
    '        job_id = create_job("test.pdf", 3)\n'
    "        pdf_bytes = generate_pdf(num_pages=3)\n"
    "\n"
    "        # ---- Mock Setup ----\n"
    "        mock_client = MagicMock()\n"
    "        mock_sarvam_class.return_value = mock_client\n"
    "        mock_job = MagicMock()\n"
    "        mock_client.document_intelligence.create_job\\\n"
    "            .return_value = mock_job\n"
    "\n"
    "        status_complete = MagicMock()\n"
    '        status_complete.job_state = "Completed"\n'
    "        mock_job.get_status.return_value = status_complete\n"
    "\n"
    "        # Create a valid ZIP with 3 HTML pages\n"
    "        import zipfile\n"
    "        zip_buf = io.BytesIO()\n"
    "        with zipfile.ZipFile(zip_buf, 'w') as zf:\n"
    '            zf.writestr("page_1.html",\n'
    '                "<html><body><p>Page 1 text</p></body></html>")\n'
    '            zf.writestr("page_2.html",\n'
    '                "<html><body><p>Page 2 text</p></body></html>")\n'
    '            zf.writestr("page_3.html",\n'
    '                "<html><body><p>Page 3 text</p></body></html>")\n'
    "        zip_bytes = zip_buf.getvalue()\n"
    "\n"
    "        def fake_download(path):\n"
    "            Path(path).write_bytes(zip_bytes)\n"
    "        mock_job.download_output.side_effect = fake_download\n"
    "\n"
    "        # ---- Execute ----\n"
    "        run_digitization(job_id, pdf_bytes)\n"
    "\n"
    "        # ---- Verify ----\n"
    "        job = get_job(job_id)\n"
    '        assert job["status"] == "completed"\n'
    '        assert job["html"] is not None\n'
    '        assert "Page 1 text" in job["html"]\n'
    '        assert "Page 2 text" in job["html"]\n'
    '        assert "Page 3 text" in job["html"]\n'
    '        assert job["error"] is None'
))
story.append(sp())

story.append(subsection("The Three Phases"))
story.append(body(
    "This test follows the <b>Arrange-Act-Assert (AAA)</b> pattern clearly:"
))
story.append(bullet("<b>Arrange (Mock Setup)</b> &mdash; Build the mock chain: SarvamAI class -> "
                     "mock client -> mock job -> status = Completed -> fake download. "
                     "We also create a real ZIP file with HTML pages."))
story.append(bullet("<b>Act (Execute)</b> &mdash; Call <i>run_digitization(job_id, pdf_bytes)</i>. "
                     "This runs the entire pipeline: write temp file, create Sarvam job, upload, "
                     "start, poll, download, extract HTML, update job."))
story.append(bullet("<b>Assert (Verify)</b> &mdash; Check the final job state. Status should be "
                     "'completed', HTML should contain all three pages, error should be None."))
story.append(sp())

story.append(section("9.2 &mdash; Job Status Transitions"))
story.append(code(
    "    @patch('app.services.digitize.time.sleep')\n"
    "    @patch('app.services.digitize.SarvamAI')\n"
    "    def test_job_status_transitions(\n"
    "            self, mock_sarvam_class, mock_sleep):\n"
    '        """Job should go through uploading -> processing -> completed."""\n'
    '        job_id = create_job("test.pdf", 3)\n'
    "        pdf_bytes = generate_pdf(num_pages=3)\n"
    "\n"
    "        # ... (same mock setup as above) ...\n"
    "\n"
    "        # Check initial status\n"
    '        assert get_job(job_id)["status"] == "uploading"\n'
    "\n"
    "        run_digitization(job_id, pdf_bytes)\n"
    "\n"
    "        # Final status should be completed\n"
    '        assert get_job(job_id)["status"] == "completed"'
))
story.append(sp())
story.append(body(
    "This test verifies the <b>state machine</b>: a job starts as 'uploading', transitions "
    "through 'processing' during digitization, and ends as 'completed'. By checking before "
    "and after <i>run_digitization</i>, we verify the full lifecycle."
))
story.append(sp())

story.append(section("9.3 &mdash; Anatomy of the Mock Coordination"))
story.append(body(
    "Let us trace exactly how the mocks interact with the real code:"
))
story.append(sp())

flow_data = [
    ["Step", "Real Code", "Mock Response"],
    ["1", "SarvamAI(api_subscription_key=...)", "Returns mock_client"],
    ["2", "client.document_intelligence\n.create_job(language, output_format)", "Returns mock_job"],
    ["3", "sarvam_job.upload_file(tmp_path)", "Does nothing (MagicMock)"],
    ["4", "sarvam_job.start()", "Does nothing (MagicMock)"],
    ["5", "sarvam_job.get_status()", 'Returns status with\njob_state="Completed"'],
    ["6", "sarvam_job.download_output(zip_path)", "Writes ZIP bytes to path\n(via side_effect)"],
]
ft = Table(flow_data, colWidths=[0.5*inch, 2.5*inch, 2.5*inch])
ft.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (1, 1), (2, -1), 'Courier'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(ft)
story.append(sp())

story.append(body(
    "Notice that steps 3 and 4 (<i>upload_file</i> and <i>start</i>) do not need any "
    "configuration &mdash; MagicMock automatically accepts any call and returns another MagicMock. "
    "Only the steps where we need specific behavior (return values, side effects) require setup."
))
story.append(sp())

story.append(tip(
    "E2E TEST DESIGN: Start by mocking the <b>boundaries</b> (external APIs, file I/O, "
    "time.sleep) and let the real code run for everything in between. This gives you "
    "maximum confidence with minimum mocking."
))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════════════
# CHAPTER 10 — Custom Markers & Running Subsets
# ═══════════════════════════════════════════════════════════════════
story.append(title("Chapter 10: Custom Markers &amp; Running Subsets"))
story.append(sp())

story.append(body(
    "As your test suite grows, you will want to run specific subsets of tests. "
    "pytest <b>markers</b> let you tag tests with labels and then filter by those labels "
    "on the command line. Our project defines two custom markers."
))
story.append(sp())

story.append(section("10.1 &mdash; Defining Custom Markers"))
story.append(body(
    "Markers are registered in <i>pytest.ini</i> to avoid warnings:"
))
story.append(filelabel("server/pytest.ini"))
story.append(code(
    "[pytest]\n"
    "markers =\n"
    '    slow: marks tests as slow (deselect with \'-m "not slow"\')\n'
    "    large_pdf: marks tests that generate large PDFs"
))
story.append(sp())
story.append(body(
    "Each marker has a name and a description. The description appears when you run "
    "<i>pytest --markers</i>."
))
story.append(sp())

story.append(section("10.2 &mdash; Applying Markers to Tests"))
story.append(body(
    "Markers are applied with the <i>@pytest.mark.&lt;name&gt;</i> decorator:"
))
story.append(filelabel("server/tests/test_upload.py"))
story.append(code(
    "class TestLargePdfUpload:\n"
    "    @pytest.mark.asyncio\n"
    "    @pytest.mark.large_pdf             # <-- custom marker\n"
    '    @patch("app.routers.upload.start_digitization")\n'
    "    async def test_100_page_pdf_upload(\n"
    "            self, mock_start, client, large_pdf):\n"
    '        """A 100-page PDF should be accepted."""\n'
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("large.pdf", large_pdf,\n'
    '                            "application/pdf")},\n'
    "        )\n"
    "        assert response.status_code == 200\n"
    '        assert response.json()["pages"] == 100\n'
    "\n"
    "    @pytest.mark.asyncio\n"
    "    @pytest.mark.large_pdf\n"
    '    @patch("app.routers.upload.start_digitization")\n'
    "    async def test_300_page_pdf_upload(\n"
    "            self, mock_start, client, very_large_pdf):\n"
    '        """A 300-page PDF should be accepted."""\n'
    "        response = await client.post(\n"
    '            "/api/upload",\n'
    '            files={"file": ("very_large.pdf", very_large_pdf,\n'
    '                            "application/pdf")},\n'
    "        )\n"
    "        assert response.status_code == 200\n"
    '        assert response.json()["pages"] == 300'
))
story.append(sp())
story.append(body(
    "These tests generate PDFs with 100 and 300 pages, which takes noticeable time. "
    "By marking them with <i>@pytest.mark.large_pdf</i>, we can skip them during rapid "
    "development and only run them in CI or before a release."
))
story.append(sp())

story.append(section("10.3 &mdash; Running Test Subsets"))
story.append(body("Here are the command-line options for filtering tests:"))
story.append(sp())

run_data = [
    ["Command", "What It Runs"],
    ["pytest", "All tests"],
    ["pytest -m large_pdf", "Only tests marked @large_pdf"],
    ["pytest -m slow", "Only tests marked @slow"],
    ['pytest -m "not large_pdf"', "All tests EXCEPT @large_pdf"],
    ['pytest -m "not slow and not large_pdf"', "Fast tests only"],
    ["pytest tests/test_upload.py", "Only tests in one file"],
    ["pytest -k 'thread'", "Tests with 'thread' in the name"],
    ["pytest -k 'TestCreateJob'", "Only the TestCreateJob class"],
    ["pytest -x", "Stop on first failure"],
    ["pytest -v", "Verbose output (show each test name)"],
    ["pytest --tb=short", "Shorter tracebacks on failure"],
]
rt = Table(run_data, colWidths=[3.0*inch, 3.0*inch])
rt.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (0, -1), 'Courier'),
    ('FONTSIZE', (0, 0), (-1, -1), 8.5),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(rt)
story.append(sp())

story.append(section("10.4 &mdash; Combining Multiple Decorators"))
story.append(body(
    "Notice that our tests often stack multiple decorators:"
))
story.append(code(
    "@pytest.mark.asyncio              # 1. async test\n"
    "@pytest.mark.large_pdf            # 2. custom marker\n"
    '@patch("app.routers.upload.start_digitization")  # 3. mock\n'
    "async def test_100_page_pdf_upload(\n"
    "        self, mock_start, client, large_pdf):\n"
    "    ..."
))
story.append(sp())
story.append(body(
    "Decorators are applied <b>bottom-up</b> (closest to the function first), but the "
    "order of <i>@pytest.mark</i> decorators does not matter. The <i>@patch</i> decorator "
    "should be closest to the function because it affects the parameter list."
))
story.append(sp())

story.append(section("10.5 &mdash; Stacking Markers on a Class"))
story.append(body(
    "You can also apply markers to an entire class. Every test in that class inherits the marker:"
))
story.append(code(
    "@pytest.mark.large_pdf\n"
    "class TestLargePdfUpload:\n"
    "    # All methods in this class are marked @large_pdf\n"
    "    async def test_100_page_pdf_upload(self, ...):\n"
    "        ...\n"
    "    async def test_300_page_pdf_upload(self, ...):\n"
    "        ..."
))
story.append(sp())

story.append(tip(
    "CI TIP: In your CI pipeline, run <b>pytest -m 'not slow'</b> on every push "
    "and <b>pytest</b> (all tests) on a nightly schedule. This gives fast feedback "
    "on pushes while still catching issues in slow tests."
))
story.append(sp())

# ── FINAL SUMMARY ──
story.append(PageBreak())
story.append(title("Summary: What We Covered"))
story.append(sp())

summary_data = [
    ["Chapter", "Concept", "Test File(s)"],
    ["1", "Project structure &amp; source code", "(overview)"],
    ["2", "pytest.ini, conftest.py, fixtures", "conftest.py"],
    ["3", "Unit tests, assertions, class groups", "test_digitize_service.py"],
    ["4", "Thread safety, concurrent testing", "test_digitize_service.py"],
    ["5", "Boundary values, data-driven tests", "test_digitize_service.py"],
    ["6", "Async tests, httpx, endpoint testing", "test_upload.py"],
    ["7", "@patch, MagicMock, side_effect", "test_large_pdf_digitization.py"],
    ["8", "Bug documentation, inspect, inverted asserts", "test_large_pdf_digitization.py"],
    ["9", "E2E flows, AAA pattern, mock coordination", "test_large_pdf_digitization.py"],
    ["10", "Custom markers, CLI filtering", "test_upload.py, pytest.ini"],
]
st_table = Table(summary_data, colWidths=[0.7*inch, 2.5*inch, 2.5*inch])
st_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(st_table)
story.append(sp(12))

story.append(body(
    "Every concept in this guide was taught through <b>real code from one repository</b>. "
    "The source files in <i>server/app/</i> and the test files in <i>server/tests/</i> are "
    "the living examples. Go read them, modify them, break them, and learn."
))
story.append(sp())
story.append(hr())
story.append(sp())
story.append(Paragraph("End of Guide", S['CoverSubtitle']))


# ═══════════════════════════════════════════════════════════════════
# BUILD PDF
# ═══════════════════════════════════════════════════════════════════
doc.build(story)
print(f"PDF generated: {OUTPUT}")
