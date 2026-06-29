import pytest

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():

    response = client.get(
        "/api/v1/yasin/health"
    )

    assert response.status_code == 200


def test_dashboard():

    response = client.get(
        "/api/v1/yasin/dashboard"
    )

    assert response.status_code == 200


def test_statistics():

    response = client.get(
        "/api/v1/yasin/statistics"
    )

    assert response.status_code == 200


def test_open_signals():

    response = client.get(
        "/api/v1/yasin/signals/open"
    )

    assert response.status_code == 200


def test_all_signals():

    response = client.get(
        "/api/v1/yasin/signals"
    )

    assert response.status_code == 200


def test_create_signal():

    payload = {

        "symbol": "XAUUSD",

        "market": "GOLD",

        "direction": "BUY",

        "entry": 2500,

        "stop_loss": 2490,

        "take_profit_1": 2510,

        "take_profit_2": 2520,

        "take_profit_3": 2530,

    }

    response = client.post(
        "/api/v1/yasin/signals",
        json=payload,
    )

    assert response.status_code in (
        200,
        201,
    )


def test_not_found():

    response = client.get(
        "/api/v1/yasin/unknown"
    )

    assert response.status_code == 404


def test_invalid_request():

    response = client.post(
        "/api/v1/yasin/signals",
        json={},
    )

    assert response.status_code in (
        400,
        422,
    )
