"""
Exportiert Statistiken und Backtesting-Ergebnisse
von Yasin AI.
"""

import csv
import json
from pathlib import Path

from openpyxl import Workbook

from app.database.session import SessionLocal
from app.models.statistics import Statistics


EXPORT_DIR = Path("exports")


def load_statistics():

    db = SessionLocal()

    try:

        return db.query(
            Statistics
        ).all()

    finally:

        db.close()


def export_json(data):

    EXPORT_DIR.mkdir(
        exist_ok=True
    )

    file = EXPORT_DIR / "statistics.json"

    with open(
        file,
        "w",
        encoding="utf-8",
    ) as fp:

        json.dump(
            [
                item.to_dict()
                for item in data
            ],
            fp,
            indent=4,
            ensure_ascii=False,
        )

    print(f"JSON exportiert: {file}")


def export_csv(data):

    EXPORT_DIR.mkdir(
        exist_ok=True
    )

    file = EXPORT_DIR / "statistics.csv"

    with open(
        file,
        "w",
        newline="",
        encoding="utf-8",
    ) as fp:

        writer = csv.writer(fp)

        writer.writerow(
            [
                "Market",
                "Trades",
                "Winrate",
                "Profit Factor",
                "Net Profit",
            ]
        )

        for item in data:

            writer.writerow(
                [
                    item.market,
                    item.total_trades,
                    item.win_rate,
                    item.profit_factor,
                    item.net_profit,
                ]
            )

    print(f"CSV exportiert: {file}")


def export_excel(data):

    EXPORT_DIR.mkdir(
        exist_ok=True
    )

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Statistics"

    sheet.append(
        [
            "Market",
            "Trades",
            "Winrate",
            "Profit Factor",
            "Net Profit",
        ]
    )

    for item in data:

        sheet.append(
            [
                item.market,
                item.total_trades,
                item.win_rate,
                item.profit_factor,
                item.net_profit,
            ]
        )

    file = EXPORT_DIR / "statistics.xlsx"

    workbook.save(file)

    print(f"Excel exportiert: {file}")


def main():

    print("=" * 60)
    print("YASIN AI EXPORT")
    print("=" * 60)

    statistics = load_statistics()

    export_json(statistics)

    export_csv(statistics)

    export_excel(statistics)

    print()

    print("Export erfolgreich abgeschlossen.")


if __name__ == "__main__":

    main()
