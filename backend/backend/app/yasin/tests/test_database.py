"""
Integrationstests
für die Datenbankschicht.
"""

import pytest

from app.database.session import SessionLocal
from app.yasin.models.trade import Trade


@pytest.fixture
def db():

    session = SessionLocal()

    yield session

    session.rollback()
    session.close()


def test_database_connection(db):

    assert db is not None


def test_create_trade(db):

    trade = Trade(
        market="GOLD",
        symbol="XAUUSD",
        direction="BUY",
        entry=2350.00,
    )

    db.add(trade)
    db.commit()

    assert trade.id is not None


def test_read_trade(db):

    trade = db.query(
        Trade
    ).first()

    assert trade is not None


def test_update_trade(db):

    trade = db.query(
        Trade
    ).first()

    trade.entry = 2360.00

    db.commit()

    assert trade.entry == 2360.00


def test_delete_trade(db):

    trade = db.query(
        Trade
    ).first()

    db.delete(trade)
    db.commit()

    assert (
        db.query(Trade)
        .filter(
            Trade.id == trade.id
        )
        .first()
        is None
    )


def test_transaction(db):

    try:

        db.begin()

        trade = Trade(
            market="BTC",
            symbol="BTCUSD",
            direction="SELL",
            entry=65000,
        )

        db.add(trade)

        db.commit()

    except Exception:

        db.rollback()

        pytest.fail(
            "Transaktion fehlgeschlagen."
        )
