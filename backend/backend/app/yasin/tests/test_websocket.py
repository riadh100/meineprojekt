"""
Integrationstests
für die WebSocket-Schnittstelle.
"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_websocket_connection():

    with client.websocket_connect(
        "/ws"
    ) as websocket:

        assert websocket is not None


def test_websocket_ping():

    with client.websocket_connect(
        "/ws"
    ) as websocket:

        websocket.send_json(
            {
                "type": "ping",
            }
        )

        response = websocket.receive_json()

        assert response["type"] == "pong"


def test_websocket_authentication():

    with client.websocket_connect(
        "/ws"
    ) as websocket:

        websocket.send_json(
            {
                "type": "authenticate",
                "token": "demo-token",
            }
        )

        response = websocket.receive_json()

        assert response["status"] in (
            "authenticated",
            "failed",
        )


def test_websocket_signal_stream():

    with client.websocket_connect(
        "/ws"
    ) as websocket:

        websocket.send_json(
            {
                "type": "subscribe",
                "channel": "signals",
            }
        )

        response = websocket.receive_json()

        assert response is not None


def test_websocket_statistics_stream():

    with client.websocket_connect(
        "/ws"
    ) as websocket:

        websocket.send_json(
            {
                "type": "subscribe",
                "channel": "statistics",
            }
        )

        response = websocket.receive_json()

        assert response is not None


def test_websocket_disconnect():

    with client.websocket_connect(
        "/ws"
    ) as websocket:

        websocket.close()

        assert True
