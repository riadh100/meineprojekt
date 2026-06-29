"""
Startet eine vollständige Marktanalyse
für Yasin AI.
"""

import argparse

from app.yasin.services.yasin_analysis_service import (
    YasinAnalysisService,
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Yasin AI Market Analysis"
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
        "--strategy",
        default="ALL",
    )

    return parser.parse_args()


def print_signal(signal):

    print("-" * 60)

    print(f"Markt          : {signal.market}")
    print(f"Symbol         : {signal.symbol}")
    print(f"Richtung       : {signal.direction}")

    print(f"Entry          : {signal.entry}")
    print(f"Stop Loss      : {signal.stop_loss}")

    print(f"Take Profit 1  : {signal.take_profit_1}")
    print(f"Take Profit 2  : {signal.take_profit_2}")
    print(f"Take Profit 3  : {signal.take_profit_3}")

    print(f"Risk/Reward    : {signal.risk_reward_ratio}")

    print(f"Qualität       : {signal.quality_score}%")
    print(f"Confidence     : {signal.confidence}%")

    print(f"Empfehlung     : {signal.recommendation}")


def main():

    args = parse_arguments()

    analysis = YasinAnalysisService()

    print("=" * 60)
    print("YASIN AI MARKET ANALYSIS")
    print("=" * 60)

    signals = analysis.run(
        market=args.market,
        timeframe=args.timeframe,
        strategy=args.strategy,
    )

    print()

    print(
        f"{len(signals)} Signale gefunden."
    )

    print()

    for signal in signals:

        print_signal(signal)

    print()

    print(
        "Analyse erfolgreich abgeschlossen."
    )


if __name__ == "__main__":

    main()
