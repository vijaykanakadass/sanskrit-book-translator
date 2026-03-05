import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


class Settings:
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    PORT: int = int(os.getenv("PORT", "3001"))
    SARVAM_API_KEY: str = os.getenv("SARVAM_API_KEY", "")


settings = Settings()
