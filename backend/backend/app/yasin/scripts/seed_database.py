"""
Seed-Daten für Yasin AI.
"""

from app.database.session import (
    SessionLocal,
)

from app.models.market import Market
from app.models.strategy import Strategy
from app.models.statistics import Statistics
from app.models.system_config import SystemConfig


def seed_markets(db):

    markets = [
        ("GOLD", "XAUUSD"),
        ("FOREX", "EURUSD"),
        ("NASDAQ", "NAS100"),
        ("SP500", "US500"),
        ("BTC", "BTCUSDT"),
    ]

    for market, symbol in markets:

        exists = (
            db.query(Market)
            .filter(
                Market.market == market
            )
            .first()
        )

        if not exists:

            db.add(
                Market(
                    market=market,
                    symbol=symbol,
                )
            )


def seed_strategies(db):

    strategies = [

        "Trend Following",

        "Breakout",

        "Scalping",

        "Swing Trading",

        "Reversal",

    ]

    for name in strategies:

        exists = (
            db.query(Strategy)
            .filter(
                Strategy.name == name
            )
            .first()
        )

        if not exists:

            db.add(
                Strategy(
                    name=name,
                    enabled=True,
                )
            )


def seed_statistics(db):

    exists = db.query(
        Statistics
    ).first()

    if exists:

        return

    db.add(
        Statistics(
            market="GLOBAL",
            total_trades=0,
            winning_trades=0,
            losing_trades=0,
            gross_profit=0,
            gross_loss=0,
        )
    )


def seed_configuration(db):

    exists = db.query(
        SystemConfig
    ).first()

    if exists:

        return

    db.add(
        SystemConfig(
            ai_enabled=True,
            telegram_enabled=True,
            dashboard_enabled=True,
            websocket_enabled=True,
            scheduler_enabled=True,
        )
    )


def seed_database():

    db = SessionLocal()

    try:

        seed_markets(db)

        seed_strategies(db)

        seed_statistics(db)

        seed_configuration(db)

        db.commit()

        print(
            "Seed erfolgreich abgeschlossen."
        )

    finally:

        db.close()


if __name__ == "__main__":

    seed_database()
