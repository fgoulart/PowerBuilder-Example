"""Hosting Settings defaults for PowerServer → FastAPI parity."""

from app.core.config import Settings


def test_hosting_settings_defaults_replace_powerserver_5088() -> None:
    cfg = Settings()
    assert cfg.public_api_url == "http://localhost:8000"
    assert cfg.bind_host == "0.0.0.0"
    assert cfg.bind_port == 8000
    assert cfg.https_enabled is False
    assert cfg.session_timeout_seconds == 3600
    assert cfg.request_timeout_seconds == 3600
    assert cfg.transaction_timeout_seconds == 120
    assert cfg.license_required is False
    assert cfg.psr_fixtures_root is None
