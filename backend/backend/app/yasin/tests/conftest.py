"""
Gemeinsame pytest-Konfiguration
für Yasin AI.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database.session import (
    SessionLocal,
)
from app.yasin.models.trade import Trade
from app.yasin.models.signal import Signal
from app.yasin.models.user import User


@pytest.fixture(scope="session")
def client():
    """
    Gemeinsamer FastAPI-Testclient.
    """
    return TestClient(app)


@pytest.fixture()
def db():
    """
    Gemeinsame Test-Datenbank-Session.
    """
    session = SessionLocal()

    yield session

    session.rollback()
    session.close()


@pytest.fixture()
def sample_trade():
    """
    Beispiel-Trade.
    """
    return Trade(
        market="GOLD",
        symbol="XAUUSD",
        direction="BUY",
        entry=2350.50,
    )


@pytest.fixture()
def sample_signal():
    """
    Beispiel-Signal.
    """
    return Signal(
        market="GOLD",
        symbol="XAUUSD",
        direction="BUY",
        confidence=92.5,
    )


@pytest.fixture()
def sample_user():
    """
    Beispiel-Benutzer.
    """
    return User(
        username="admin",
        email="admin@yasin.ai",
    )
