"""
Integrationstests
für die Middleware.
"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_request_id_header():

    response = client.get(
        "/api/health"
    )

    assert (
        "X-Request-ID"
        in response.headers
    )


def test_response_time_header():

    response = client.get(
        "/api/health"
    )

    assert (
        "X-Response-Time"
        in response.headers
    )


def test_security_headers():

    response = client.get(
        "/api/health"
    )

    assert (
        response.headers[
            "X-Frame-Options"
        ]
        == "DENY"
    )

    assert (
        response.headers[
            "X-Content-Type-Options"
        ]
        == "nosniff"
    )


def test_cors_headers():

    response = client.options(
        "/api/health"
    )

    assert response.status_code in (
        200,
        204,
    )


def test_authentication_required():

    response = client.get(
        "/api/protected"
    )

    assert response.status_code in (
        401,
        403,
    )


def test_error_handler():

    response = client.get(
        "/api/test/error"
    )

    assert response.status_code in (
        500,
        422,
    )
