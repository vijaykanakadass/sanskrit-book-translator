from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import upload, jobs

app = FastAPI(title="Sanskrit Book Translator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload.router)
app.include_router(jobs.router)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
