"""
Unit-Tests für die
projektspezifischen Exceptions.
"""

import pytest

from app.yasin.exceptions import (
    ValidationException,
    AuthenticationException,
    AuthorizationException,
    DatabaseException,
    ApiException,
    TradingException,
    BacktestingException,
    SchedulerException,
    WebSocketException,
    SystemException,
)


def test_validation_exception():

    with pytest.raises(
        ValidationException
    ):

        raise ValidationException(
            "Ungültiger Markt."
        )


def test_authentication_exception():

    with pytest.raises(
        AuthenticationException
    ):

        raise AuthenticationException(
            "Login fehlgeschlagen."
        )


def test_authorization_exception():

    with pytest.raises(
        AuthorizationException
    ):

        raise AuthorizationException(
            "Kein Zugriff."
        )


def test_database_exception():

    with pytest.raises(
        DatabaseException
    ):

        raise DatabaseException(
            "DB nicht erreichbar."
        )


def test_api_exception():

    with pytest.raises(
        ApiException
    ):

        raise ApiException(
            "API-Fehler.",
            status_code=500,
        )


def test_trading_exception():

    with pytest.raises(
        TradingException
    ):

        raise TradingException(
            "Order konnte nicht ausgeführt werden."
        )


def test_backtesting_exception():

    with pytest.raises(
        BacktestingException
    ):

        raise BacktestingException(
            "Keine historischen Daten."
        )


def test_scheduler_exception():

    with pytest.raises(
        SchedulerException
    ):

        raise SchedulerException(
            "Scheduler gestoppt."
        )


def test_websocket_exception():

    with pytest.raises(
        WebSocketException
    ):

        raise WebSocketException(
            "Verbindung getrennt."
        )


def test_system_exception():

    with pytest.raises(
        SystemException
    ):

        raise SystemException(
            "Systemfehler."
        )
