"""
Initialisiert die Datenbank
für Yasin AI.
"""

from sqlalchemy import text

from app.database.session import (
    engine,
)

from app.database.base import (
    Base,
)

from app.database.seed import (
    seed_database,
)


def create_tables():

    print("Erstelle Tabellen...")

    Base.metadata.create_all(
        bind=engine
    )


def create_indexes():

    print("Erstelle Indizes...")

    with engine.begin() as connection:

        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS
                idx_signal_market
                ON signals (market);
                """
            )
        )

        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS
                idx_signal_status
                ON signals (status);
                """
            )
        )

        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS
                idx_statistics_market
                ON statistics (market);
                """
            )
        )


def check_connection():

    with engine.connect() as connection:

        connection.execute(
            text("SELECT 1")
        )

    print("Datenbankverbindung erfolgreich.")


def initialize():

    print("=" * 60)
    print("YASIN AI DATABASE INIT")
    print("=" * 60)

    check_connection()

    create_tables()

    create_indexes()

    seed_database()

    print()

    print("Datenbank erfolgreich initialisiert.")


if __name__ == "__main__":

    initialize()
