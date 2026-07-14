"""License/secret presence gate unit tests."""

import pytest

from app.core.config import Settings
from app.core.license_gate import LicenseGateError, assert_license_ready, license_is_configured


def test_license_gate_optional_when_not_required() -> None:
    cfg = Settings(license_required=False)
    assert_license_ready(cfg)
    assert license_is_configured(cfg) is False


def test_license_gate_requires_secret_when_enabled() -> None:
    cfg = Settings(license_required=True, appeon_license_key=None, license_key=None)
    with pytest.raises(LicenseGateError):
        assert_license_ready(cfg)

    cfg_ok = Settings(license_required=True, appeon_license_key="appeon-demo-secret-value")
    assert_license_ready(cfg_ok)
    assert license_is_configured(cfg_ok) is True
