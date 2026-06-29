"""
Integrationstests
für das Dashboard.
"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_dashboard_page():

    response = client.get(
        "/api/dashboard"
    )

    assert response.status_code == 200


def test_dashboard_statistics():

    response = client.get(
        "/api/dashboard/statistics"
    )

    assert response.status_code == 200

    data = response.json()

    assert "total_trades" in data
    assert "win_rate" in data
    assert "profit_factor" in data


def test_dashboard_open_trades():

    response = client.get(
        "/api/dashboard/open-trades"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list,
    )


def test_dashboard_signals():

    response = client.get(
        "/api/dashboard/signals"
    )

    assert response.status_code == 200


def test_dashboard_system_status():

    response = client.get(
        "/api/dashboard/system"
    )

    assert response.status_code == 200

    data = response.json()

    assert "status" in data
    assert "uptime" in data


def test_dashboard_chart_data():

    response = client.get(
        "/api/dashboard/chart"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list,
    )
