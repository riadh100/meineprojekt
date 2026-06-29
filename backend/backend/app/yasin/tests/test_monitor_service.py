import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_monitor_service import (
    YasinMonitorService,
)


@pytest.fixture
def signal_repository():

    return Mock()


@pytest.fixture
def telegram():

    return Mock()


@pytest.fixture
def websocket():

    return Mock()


@pytest.fixture
def statistics():

    return Mock()


@pytest.fixture
def service(
    signal_repository,
    telegram,
    websocket,
    statistics,
):

    return YasinMonitorService(
        signal_repository=signal_repository,
        telegram_service=telegram,
        websocket_manager=websocket,
        statistics_service=statistics,
    )


def test_monitor_open_trades(
    service,
    signal_repository,
):

    signal_repository.get_open_signals.return_value = [
        Mock(),
    ]

    service.monitor()

    signal_repository.get_open_signals.assert_called_once()


def test_take_profit_notification(
    service,
    telegram,
):

    signal = Mock()

    service.take_profit_hit(
        signal,
        "TP1",
    )

    telegram.send_tp.assert_called_once()


def test_stop_loss_notification(
    service,
    telegram,
):

    signal = Mock()

    service.stop_loss_hit(
        signal,
    )

    telegram.send_stop_loss.assert_called_once()


def test_websocket_update(
    service,
    websocket,
):

    signal = Mock()

    service.broadcast(signal)

    websocket.broadcast_signal.assert_called_once()


def test_statistics_refresh(
    service,
    statistics,
):

    service.update_statistics()

    statistics.rebuild_all.assert_called_once()


def test_monitor_status(
    service,
):

    result = service.status()

    assert result is not None
