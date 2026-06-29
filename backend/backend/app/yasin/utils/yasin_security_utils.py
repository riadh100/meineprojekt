"""
Sicherheitsfunktionen
für Yasin AI.
"""

import hashlib
import hmac
import secrets
from base64 import urlsafe_b64encode


def sha256(value: str) -> str:
    """SHA-256 Hash erzeugen."""
    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()


def verify_sha256(
    value: str,
    expected_hash: str,
) -> bool:
    """SHA-256 Hash überprüfen."""
    return hmac.compare_digest(
        sha256(value),
        expected_hash,
    )


def generate_token(
    length: int = 32,
) -> str:
    """Kryptografisch sicheren Token erzeugen."""
    return secrets.token_urlsafe(length)


def generate_secret_key(
    length: int = 64,
) -> str:
    """Secret-Key erzeugen."""
    return urlsafe_b64encode(
        secrets.token_bytes(length)
    ).decode("utf-8")


def sign_data(
    data: str,
    secret: str,
) -> str:
    """Daten signieren."""

    return hmac.new(
        secret.encode("utf-8"),
        data.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def verify_signature(
    data: str,
    signature: str,
    secret: str,
) -> bool:
    """Signatur prüfen."""

    expected = sign_data(
        data,
        secret,
    )

    return hmac.compare_digest(
        expected,
        signature,
    )


def generate_api_key() -> str:
    """API-Key erzeugen."""
    return secrets.token_hex(32)


def generate_password(
    length: int = 20,
) -> str:
    """Sicheres Passwort erzeugen."""

    alphabet = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*()_-+=<>?"
    )

    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )


def secure_compare(
    left: str,
    right: str,
) -> bool:
    """Timing-sicheren Vergleich durchführen."""
    return hmac.compare_digest(
        left,
        right,
    )
