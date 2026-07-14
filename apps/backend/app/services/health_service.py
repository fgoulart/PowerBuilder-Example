"""Readiness aggregation for GET /api/v1/health."""

from __future__ import annotations

from sqlalchemy import text

from app.core.config import settings
from app.core.database import engine
from app.core.license_gate import license_is_configured
from app.schemas.health import HealthResponse


def check_database() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


def build_health_response() -> HealthResponse:
    db_ok = check_database()
    status = "ok" if db_ok else "degraded"
    return HealthResponse(
        status=status,
        environment=settings.environment,
        db_ok=db_ok,
        public_api_url=settings.public_api_url,
        https_enabled=settings.https_enabled,
        session_timeout_seconds=settings.session_timeout_seconds,
        request_timeout_seconds=settings.request_timeout_seconds,
        transaction_timeout_seconds=settings.transaction_timeout_seconds,
        license_configured=license_is_configured(settings),
    )
