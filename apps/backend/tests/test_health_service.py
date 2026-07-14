"""Health readiness service unit tests."""

from app.services import health_service


def test_build_health_response_includes_readiness_fields(monkeypatch) -> None:
    monkeypatch.setattr(health_service, "check_database", lambda: True)
    payload = health_service.build_health_response()
    assert payload.status == "ok"
    assert payload.db_ok is True
    assert payload.public_api_url == "http://localhost:8000"
    assert payload.session_timeout_seconds == 3600
