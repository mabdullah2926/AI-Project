from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
LOCAL_DB_PATH = BASE_DIR / "returns.db"

load_dotenv(dotenv_path=ENV_PATH)


def _create_engine(database_url: str):
    """
    Create database engine for SQLite or PostgreSQL.
    """

    if database_url.startswith("sqlite"):
        return create_engine(
            database_url,
            connect_args={"check_same_thread": False},
            echo=False,
        )

    return create_engine(
        database_url,
        pool_pre_ping=True,
        pool_recycle=300,
        pool_size=5,
        max_overflow=10,
        echo=False,
    )


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = f"sqlite:///{LOCAL_DB_PATH}"
    print("DATABASE_URL missing, using local SQLite database")

try:
    engine = _create_engine(DATABASE_URL)

    # Test connection
    with engine.connect() as connection:
        print("Database connection ready")

except Exception as exc:
    print(f"Database connection failed: {exc}")

    fallback_url = f"sqlite:///{LOCAL_DB_PATH}"

    engine = create_engine(
        fallback_url,
        connect_args={"check_same_thread": False},
    )

    print("Using SQLite fallback database")


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()