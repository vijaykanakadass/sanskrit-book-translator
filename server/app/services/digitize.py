import io
import re
import time
import uuid
import zipfile
import threading
import tempfile
from pathlib import Path
from sarvamai import SarvamAI
from app.config import settings

# In-memory job store
jobs = {}
jobs_lock = threading.Lock()


def get_job(job_id):
    with jobs_lock:
        return jobs.get(job_id, {}).copy()


def update_job(job_id, **kwargs):
    with jobs_lock:
        if job_id in jobs:
            jobs[job_id].update(kwargs)


def create_job(filename, pages):
    job_id = str(uuid.uuid4())
    with jobs_lock:
        jobs[job_id] = {
            "job_id": job_id,
            "filename": filename,
            "pages": pages,
            "status": "uploading",
            "detail": "Submitting to Sarvam...",
            "html": None,
            "error": None,
        }
    return job_id


def adaptive_poll_interval(elapsed, total_pages):
    if total_pages < 10:
        return 5.0
    if elapsed < 30:
        return 5.0
    elif elapsed < 300:
        return 10.0
    else:
        return 15.0


def extract_html_from_zip(zip_bytes):
    """Extract and merge per-page HTML files from a ZIP archive."""
    pages = []
    with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zf:
        html_files = sorted([
            name for name in zf.namelist()
            if name.lower().endswith(".html")
        ])
        for i, filename in enumerate(html_files):
            content = zf.read(filename).decode("utf-8", errors="replace")
            # Strip HTML/HEAD/BODY wrappers from individual pages
            content = re.sub(r"<!DOCTYPE[^>]*>", "", content, flags=re.IGNORECASE)
            content = re.sub(r"</?html[^>]*>", "", content, flags=re.IGNORECASE)
            content = re.sub(r"<head>.*?</head>", "", content, flags=re.IGNORECASE | re.DOTALL)
            content = re.sub(r"</?body[^>]*>", "", content, flags=re.IGNORECASE)
            pages.append((i + 1, content.strip()))

    # Build merged HTML
    parts = []
    for page_num, content in pages:
        parts.append(
            f'<div class="page" id="page-{page_num}">'
            f'<div class="page-header">Page {page_num}</div>'
            f'{content}'
            f'</div>'
        )

    return "\n".join(parts)


def run_digitization(job_id, pdf_bytes):
    """Background task: submit PDF to Sarvam Document Intelligence, poll, download result."""
    try:
        client = SarvamAI(api_subscription_key=settings.SARVAM_API_KEY)

        # Save PDF to temp file
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(pdf_bytes)
            tmp_path = tmp.name

        # Create job with retry + exponential backoff
        sarvam_job = None
        max_retries = 5
        for attempt in range(max_retries):
            try:
                sarvam_job = client.document_intelligence.create_job(
                    language="sa-IN",
                    output_format="html",
                )
                sarvam_job.upload_file(tmp_path)
                sarvam_job.start()
                break
            except Exception as api_err:
                err_str = str(api_err).lower()
                is_rate_limit = "rate limit" in err_str or "429" in err_str
                if is_rate_limit and attempt < max_retries - 1:
                    backoff = min(2 ** (attempt + 2), 60)  # 4s, 8s, 16s, 32s, 60s
                    update_job(job_id, detail=f"Rate limited, retrying in {backoff}s...")
                    time.sleep(backoff)
                else:
                    raise

        update_job(job_id, status="processing", detail="Digitizing pages...")

        # Poll until complete
        job_info = get_job(job_id)
        total_pages = job_info.get("pages", 0)
        start_time = time.time()

        while True:
            status_resp = sarvam_job.get_status()
            job_state = status_resp.job_state

            if job_state in ("Completed", "PartiallyCompleted"):
                break
            elif job_state == "Failed":
                raise Exception("Sarvam digitization job failed")

            elapsed = time.time() - start_time
            interval = adaptive_poll_interval(elapsed, total_pages)
            update_job(job_id, detail=f"Digitizing... ({int(elapsed)}s elapsed)")
            time.sleep(interval)

        # Download output
        update_job(job_id, detail="Downloading results...")
        with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp_zip:
            zip_path = tmp_zip.name

        sarvam_job.download_output(zip_path)
        zip_bytes = Path(zip_path).read_bytes()

        # Extract and merge HTML
        html = extract_html_from_zip(zip_bytes)

        # Clean up temp files
        Path(tmp_path).unlink(missing_ok=True)
        Path(zip_path).unlink(missing_ok=True)

        update_job(job_id, status="completed", detail="Done", html=html)
        print(f"[digitize] Job {job_id} completed successfully")

    except Exception as e:
        update_job(job_id, status="failed", detail=str(e), error=str(e))
        print(f"[digitize] Job {job_id} failed: {e}")


def start_digitization(job_id, pdf_bytes):
    """Launch digitization in a background thread."""
    thread = threading.Thread(
        target=run_digitization,
        args=(job_id, pdf_bytes),
        daemon=True,
    )
    thread.start()
