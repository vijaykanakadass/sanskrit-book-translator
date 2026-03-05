import io
from fastapi import APIRouter, UploadFile, HTTPException
import pdfplumber
from app.services.digitize import create_job, start_digitization

router = APIRouter()


@router.post("/api/upload")
async def upload_pdf(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    contents = await file.read()
    size = len(contents)

    try:
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            pages = len(pdf.pages)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read PDF. The file may be corrupted.")

    print(f"\n{'='*50}")
    print(f"PDF RECEIVED — starting digitization")
    print(f"  Filename: {file.filename}")
    print(f"  Size:     {size / 1024:.1f} KB")
    print(f"  Pages:    {pages}")
    print(f"{'='*50}\n")

    # Create job and start background digitization
    job_id = create_job(file.filename, pages)
    start_digitization(job_id, contents)

    return {
        "job_id": job_id,
        "filename": file.filename,
        "size": size,
        "pages": pages,
        "status": "processing",
    }
