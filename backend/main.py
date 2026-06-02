from __future__ import annotations

import os
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"
FRONTEND_INDEX = FRONTEND_DIR / "index.html"


# Make sure imports like `backend.database.db` work whether uvicorn is launched
# from the repo root or from inside `backend/`.
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from backend.database.db import Base, engine  # noqa: E402
from backend.routes.returns import router as returns_router
from backend.routes.analytics import router as analytics_router  # noqa: E402


app = FastAPI(title="Returns Optimizer", version="1.0.0")


try:
    Base.metadata.create_all(bind=engine)
    print("Database tables ready")
except Exception as exc:
    print(f"Database setup skipped: {exc}")


app.include_router(returns_router, prefix="/api/returns", tags=["returns"])
app.include_router(analytics_router)

if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api")
def api_info() -> dict[str, object]:
    return {
        "app": "E-commerce Returns Optimizer",
        "version": "1.0.0",
        "endpoints": [
            "POST /api/returns/submit",
            "GET /api/returns/all",
            "GET /api/returns/analytics",
            "GET /api/analytics/summary",
        ],
    }


@app.get("/api/meta")
def api_meta() -> dict[str, object]:
    database_url = os.getenv("DATABASE_URL", "")
    return {
        "app_name": os.getenv("APP_NAME", "Returns Optimizer"),
        "app_env": os.getenv("APP_ENV", "development"),
        "debug": os.getenv("DEBUG", "True"),
        "database": {
            "configured": bool(database_url),
            "provider": "sqlite" if database_url.startswith("sqlite") else "postgresql" if database_url else "unknown",
        },
        "integrations": {
            "groq": bool(os.getenv("GROQ_API_KEY")),
            "shopify": bool(os.getenv("SHOPIFY_ACCESS_TOKEN") or os.getenv("SHOPIFY_API_KEY")),
            "stripe": bool(os.getenv("STRIPE_SECRET_KEY")),
            "resend": bool(os.getenv("RESEND_API_KEY")),
            "twilio": bool(os.getenv("TWILIO_ACCOUNT_SID") and os.getenv("TWILIO_AUTH_TOKEN")),
        },
    }


@app.get("/")
def root():
    if FRONTEND_INDEX.exists():
        return FileResponse(FRONTEND_INDEX)
    raise HTTPException(status_code=404, detail="Frontend index.html not found")


@app.get("/ui", response_class=HTMLResponse)
def ui() -> HTMLResponse:
    if not FRONTEND_INDEX.exists():
        raise HTTPException(status_code=404, detail="Frontend index.html not found")
    return HTMLResponse(FRONTEND_INDEX.read_text(encoding="utf-8"))
