"""
Integrationstests
für den Telegram-Service.
"""

import pytest

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)


@pytest.fixture
def service():

    return YasinTelegramService()


def test_send_message(service):

    result = service.send_message(
        "Testnachricht"
    )

    assert result is True


def test_send_signal(service):

    result = service.send_signal(
        market="GOLD",
        symbol="XAUUSD",
        direction="BUY",
        entry=2350.50,
        stop_loss=2345.00,
        take_profit=2365.00,
    )

    assert result is True


def test_send_statistics(service):

    result = service.send_statistics()

    assert result is True


def test_send_system_status(service):

    result = service.send_system_status()

    assert result is True


def test_send_error(service):

    result = service.send_error(
        "Testfehler"
    )

    assert result is True


def test_send_trade_closed(service):

    result = service.send_trade_closed(
        trade_id=1,
        profit=125.40,
    )

    assert result is True
