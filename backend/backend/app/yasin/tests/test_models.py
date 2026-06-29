"""
Unit-Tests für die
ORM-Datenmodelle.
"""

import pytest

from app.yasin.models.trade import Trade
from app.yasin.models.signal import Signal
from app.yasin.models.user import User


def test_trade_model():

    trade = Trade(
        market="GOLD",
        symbol="XAUUSD",
        direction="BUY",
        entry=2350.50,
    )

    assert trade.market == "GOLD"
    assert trade.symbol == "XAUUSD"
    assert trade.direction == "BUY"
    assert trade.entry == 2350.50


def test_signal_model():

    signal = Signal(
        market="BTC",
        symbol="BTCUSD",
        direction="SELL",
        confidence=91.5,
    )

    assert signal.market == "BTC"
    assert signal.symbol == "BTCUSD"
    assert signal.direction == "SELL"
    assert signal.confidence == 91.5


def test_user_model():

    user = User(
        username="admin",
        email="admin@yasin.ai",
    )

    assert user.username == "admin"
    assert user.email == "admin@yasin.ai"


def test_trade_defaults():

    trade = Trade()

    assert trade.status == "OPEN"


def test_signal_defaults():

    signal = Signal()

    assert signal.active is True


def test_user_defaults():

    user = User()

    assert user.is_active is True
