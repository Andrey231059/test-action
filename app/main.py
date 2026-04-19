import os
from datetime import datetime, timezone

from fastapi import FastAPI

APP_NAME = os.getenv("APP_NAME", "FastAPI Template")
APP_ENV = os.getenv("APP_ENV", "dev")
APP_VERSION = os.getenv("APP_VERSION", "dev")

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Template FastAPI service for containerized deployments.",
)


@app.get("/")
def read_root():
    return {
        "service": APP_NAME,
        "env": APP_ENV,
        "version": APP_VERSION,
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": APP_NAME,
        "env": APP_ENV,
        "version": APP_VERSION,
        "time_utc": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/date")
def current_date():
    now = datetime.now(timezone.utc)
    return {"date_utc": now.date().isoformat(), "timezone": "UTC"}


@app.get("/datetime")
def current_datetime():
    now = datetime.now(timezone.utc)
    return {
        "datetime_utc": now.isoformat(),
        "date_utc": now.date().isoformat(),
        "timezone": "UTC",
    }
