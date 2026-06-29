"""
Integrationstests
für die REST API.
"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():

    response = client.get(
        "/api/health"
    )

    assert response.status_code == 200


def test_analysis_endpoint():

    response = client.post(
        "/api/analysis/run",
        json={
            "market": "GOLD",
            "timeframe": "15m",
            "strategy": "ALL",
        },
    )

    assert response.status_code == 200


def test_backtesting_endpoint():

    response = client.post(
        "/api/backtesting/run",
        json={
            "market": "GOLD",
            "timeframe": "15m",
            "strategy": "Trend Following",
        },
    )

    assert response.status_code == 200


def test_statistics_endpoint():

    response = client.get(
        "/api/statistics"
    )

    assert response.status_code == 200


def test_scheduler_status():

    response = client.get(
        "/api/scheduler/status"
    )

    assert response.status_code == 200


def test_dashboard_endpoint():

    response = client.get(
        "/api/dashboard"
    )

    assert response.status_code == 200


def test_invalid_endpoint():

    response = client.get(
        "/api/does-not-exist"
    )

    assert response.status_code == 404
