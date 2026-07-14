"""Appeon/LICENSE secret presence gate for FastAPI hosting ops."""

from __future__ import annotations

from typing import Protocol


class LicenseSettings(Protocol):
    license_required: bool
    appeon_license_key: str | None
    license_key: str | None


class LicenseGateError(RuntimeError):
    """Raised when a required license/secret env var is missing or too short."""


def _candidate_secrets(settings: LicenseSettings) -> list[str]:
    values: list[str] = []
    if settings.appeon_license_key:
        values.append(settings.appeon_license_key.strip())
    if settings.license_key:
        values.append(settings.license_key.strip())
    return [value for value in values if value]


def license_is_configured(settings: LicenseSettings) -> bool:
    return any(len(value) >= 8 for value in _candidate_secrets(settings))


def assert_license_ready(settings: LicenseSettings) -> None:
    if not settings.license_required:
        return
    if license_is_configured(settings):
        return
    raise LicenseGateError(
        "LICENSE_REQUIRED is enabled but neither APPEON_LICENSE_KEY nor "
        "LICENSE_KEY is set to a non-empty secret (min length 8). "
        "Never embed license blobs in source; supply via env/secrets."
    )
