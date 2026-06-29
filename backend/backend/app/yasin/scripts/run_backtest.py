"""
Startet einen Backtest
für Yasin AI.
"""

import argparse

from app.yasin.backtesting.yasin_backtesting_service import (
    YasinBacktestingService,
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Yasin AI Backtesting"
    )

    parser.add_argument(
        "--market",
        default="GOLD",
    )

    parser.add_argument(
        "--timeframe",
        default="15m",
    )

    parser.add_argument(
        "--balance",
        type=float,
        default=10000,
    )

    parser.add_argument(
        "--strategy",
        default="Trend Following",
    )

    return parser.parse_args()


def print_summary(result):

    print()
    print("=" * 60)
    print("BACKTEST ERGEBNIS")
    print("=" * 60)

    print(f"Markt           : {result.market}")
    print(f"Strategie       : {result.strategy}")

    print(f"Trades          : {result.total_trades}")
    print(f"Gewinne         : {result.winning_trades}")
    print(f"Verluste        : {result.losing_trades}")

    print(f"Winrate         : {result.win_rate}%")
    print(f"Profit Factor   : {result.profit_factor}")
    print(f"Drawdown        : {result.max_drawdown}%")

    print(f"Net Profit      : {result.net_profit}")

    print(f"Endkapital      : {result.final_balance}")


def main():

    args = parse_arguments()

    service = YasinBacktestingService()

    print("=" * 60)
    print("YASIN AI BACKTEST")
    print("=" * 60)

    result = service.run(
        market=args.market,
        timeframe=args.timeframe,
        initial_balance=args.balance,
        strategy=args.strategy,
    )

    print_summary(result)

    print()

    print("Exportiere Ergebnisse...")

    service.export_json()

    service.export_csv()

    service.export_excel()

    print("Backtest erfolgreich abgeschlossen.")


if __name__ == "__main__":

    main()
