import pytest

from unittest.mock import Mock

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)


@pytest.fixture
def bot():

    return Mock()


@pytest.fixture
def formatter():

    return Mock()


@pytest.fixture
def service(
    bot,
    formatter,
):

    return YasinTelegramService(
        telegram_bot=bot,
        formatter=formatter,
    )


def test_send_signal(
    service,
    bot,
):

    signal = Mock()

    service.send_signal(signal)

    bot.send_message.assert_called_once()


def test_send_take_profit(
    service,
    bot,
):

    signal = Mock()

    service.send_tp(
        signal,
        "TP1",
    )

    bot.send_message.assert_called_once()


def test_send_stop_loss(
    service,
    bot,
):

    signal = Mock()

    service.send_stop_loss(
        signal,
    )

    bot.send_message.assert_called_once()


def test_send_statistics(
    service,
    bot,
):

    service.send_statistics(
        Mock()
    )

    bot.send_message.assert_called_once()


def test_send_system_message(
    service,
    bot,
):

    service.send_system_message(
        "System gestartet"
    )

    bot.send_message.assert_called_once()


def test_send_health_report(
    service,
    bot,
):

    service.send_health_report(
        Mock()
    )

    bot.send_message.assert_called_once()


def test_service_status(
    service,
):

    result = service.status()

    assert result is not None
