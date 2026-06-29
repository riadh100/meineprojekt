"""
Importiert historische Marktdaten
für Yasin AI.
"""

import csv
import json
from pathlib import Path

from app.database.session import SessionLocal
from app.models.market_data import MarketData


SUPPORTED_EXTENSIONS = {
    ".csv",
    ".json",
}


def import_csv(db, file_path):

    with open(
        file_path,
        newline="",
        encoding="utf-8",
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            db.add(
                MarketData(
                    market=row["market"],
                    symbol=row["symbol"],
                    timeframe=row["timeframe"],
                    timestamp=row["timestamp"],
                    open=row["open"],
                    high=row["high"],
                    low=row["low"],
                    close=row["close"],
                    volume=row["volume"],
                )
            )


def import_json(db, file_path):

    with open(
        file_path,
        encoding="utf-8",
    ) as file:

        data = json.load(file)

    for row in data:

        db.add(
            MarketData(
                market=row["market"],
                symbol=row["symbol"],
                timeframe=row["timeframe"],
                timestamp=row["timestamp"],
                open=row["open"],
                high=row["high"],
                low=row["low"],
                close=row["close"],
                volume=row["volume"],
            )
        )


def validate_file(file_path):

    suffix = Path(file_path).suffix.lower()

    if suffix not in SUPPORTED_EXTENSIONS:

        raise ValueError(
            "Dateiformat wird nicht unterstützt."
        )


def import_market_data(file_path):

    validate_file(file_path)

    db = SessionLocal()

    try:

        suffix = Path(file_path).suffix.lower()

        if suffix == ".csv":

            import_csv(
                db,
                file_path,
            )

        elif suffix == ".json":

            import_json(
                db,
                file_path,
            )

        db.commit()

        print(
            "Marktdaten erfolgreich importiert."
        )

    finally:

        db.close()


if __name__ == "__main__":

    file_name = input(
        "Dateipfad: "
    )

    import_market_data(file_name)
