import pytest

from unittest.mock import Mock

from app.yasin.websocket.yasin_websocket_service import (
    YasinWebSocketService,
)


@pytest.fixture
def connection_manager():

    return Mock()


@pytest.fixture
def dashboard_service():

    return Mock()


@pytest.fixture
def service(
    connection_manager,
    dashboard_service,
):

    return YasinWebSocketService(
        connection_manager=connection_manager,
        dashboard_service=dashboard_service,
    )


def test_connect(
    service,
    connection_manager,
):

    websocket = Mock()

    service.connect(websocket)

    connection_manager.connect.assert_called_once_with(
        websocket
    )


def test_disconnect(
    service,
    connection_manager,
):

    websocket = Mock()

    service.disconnect(websocket)

    connection_manager.disconnect.assert_called_once_with(
        websocket
    )


def test_broadcast_signal(
    service,
    connection_manager,
):

    signal = Mock()

    service.broadcast_signal(signal)

    connection_manager.broadcast_signal.assert_called_once()


def test_broadcast_dashboard(
    service,
    connection_manager,
):

    dashboard = Mock()

    service.broadcast_dashboard(
        dashboard
    )

    connection_manager.broadcast_dashboard.assert_called_once()


def test_refresh_dashboard(
    service,
    dashboard_service,
):

    service.refresh_dashboard()

    dashboard_service.refresh.assert_called_once()


def test_connection_count(
    service,
    connection_manager,
):

    connection_manager.count.return_value = 5

    assert service.connection_count() == 5


def test_service_status(
    service,
):

    result = service.status()

    assert result is not None
