"""
Beispiel für das Backtesting-System
von Yasin AI.
"""

from app.yasin.backtesting.yasin_backtesting_service import (
    YasinBacktestingService,
)


def main():

    backtest = YasinBacktestingService()

    print("=" * 60)
    print("YASIN AI BACKTEST")
    print("=" * 60)

    print("\nBacktest wird gestartet...")

    result = backtest.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
    )

    print("\nErgebnisse")

    print("-" * 60)

    print(f"Trades        : {result.total_trades}")
    print(f"Gewinne       : {result.winning_trades}")
    print(f"Verluste      : {result.losing_trades}")

    print(f"Winrate       : {result.win_rate}%")
    print(f"Profit Factor : {result.profit_factor}")

    print(f"Drawdown      : {result.max_drawdown}%")

    print(f"Net Profit    : {result.net_profit}")

    print(f"End Balance   : {result.final_balance}")

    print()

    print("Exportiere Ergebnisse...")

    backtest.export_json()

    backtest.export_csv()

    print("Backtest abgeschlossen.")


if __name__ == "__main__":
    main()
