import hashlib
import hmac
import secrets


def generate_api_key(
    length: int = 32,
) -> str:
    """
    Erzeugt einen sicheren API-Key.
    """

    return secrets.token_hex(length)


def generate_token(
    length: int = 32,
) -> str:
    """
    Erzeugt ein sicheres Token.
    """

    return secrets.token_urlsafe(length)


def sha256(
    value: str,
) -> str:

    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()


def verify_hash(
    value: str,
    hashed: str,
) -> bool:

    return hmac.compare_digest(
        sha256(value),
        hashed,
    )


def sign_message(
    message: str,
    secret: str,
) -> str:

    return hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256,
    ).hexdigest()


def verify_signature(
    message: str,
    signature: str,
    secret: str,
) -> bool:

    expected = sign_message(
        message,
        secret,
    )

    return hmac.compare_digest(
        expected,
        signature,
    )


def secure_compare(
    value1: str,
    value2: str,
) -> bool:

    return hmac.compare_digest(
        value1,
        value2,
    )


def validate_api_key(
    api_key: str,
    expected: str,
) -> bool:

    return secure_compare(
        api_key,
        expected,
    )


def random_secret(
    length: int = 64,
) -> str:

    return secrets.token_hex(length)
