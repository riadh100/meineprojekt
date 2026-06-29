import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_signal_service import (
    YasinSignalService,
)


@pytest.fixture
def repository():

    return Mock()


@pytest.fixture
def telegram():

    return Mock()


@pytest.fixture
def events():

    return Mock()


@pytest.fixture
def service(
    repository,
    telegram,
    events,
):

    return YasinSignalService(
        repository=repository,
        telegram=telegram,
        events=events,
    )


def test_create_signal(
    service,
    repository,
):

    signal = Mock()

    repository.create.return_value = signal

    result = service.create(signal)

    repository.create.assert_called_once()

    assert result == signal


def test_get_all_signals(
    service,
    repository,
):

    repository.get_all.return_value = [
        Mock(),
        Mock(),
    ]

    result = service.get_all()

    assert len(result) == 2


def test_get_open_signals(
    service,
    repository,
):

    repository.get_open_signals.return_value = [
        Mock(),
    ]

    result = service.get_open_signals()

    assert len(result) == 1


def test_publish_signal(
    service,
    telegram,
):

    signal = Mock()

    signal.is_approved = True

    service.publish(signal)

    telegram.send_signal.assert_called_once()


def test_close_trade(
    service,
    repository,
):

    service.close_trade(
        signal_id=1,
        close_price=2500,
        status="TP3",
        realized_profit=300,
        realized_profit_percent=3,
    )

    repository.close_trade.assert_called_once()


def test_delete_signal(
    service,
    repository,
):

    service.delete(1)

    repository.delete.assert_called_once_with(
        1
    )
