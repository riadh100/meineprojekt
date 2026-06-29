"""
Beispiel für den vollständigen Signal-Workflow
von Yasin AI.
"""

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)


def main():

    ai = YasinAIService()

    print("=" * 60)
    print("YASIN AI SIGNAL WORKFLOW")
    print("=" * 60)

    # Analyse starten
    print("\n[1] Marktanalyse...")
    analysis = ai.run_analysis()

    # Signale erzeugen
    print("[2] Signalgenerierung...")
    signals = ai.generate_signals()

    if not signals:
        print("Keine Signale gefunden.")
        return

    for signal in signals:

        print()

        print(f"Markt      : {signal.market}")
        print(f"Symbol     : {signal.symbol}")
        print(f"Richtung   : {signal.direction}")

        print(f"Entry      : {signal.entry}")
        print(f"Stop Loss  : {signal.stop_loss}")

        print(f"TP1        : {signal.take_profit_1}")
        print(f"TP2        : {signal.take_profit_2}")
        print(f"TP3        : {signal.take_profit_3}")

        print(f"Quality    : {signal.quality_score}%")
        print(f"Confidence : {signal.confidence}%")
        print(f"RR         : {signal.risk_reward_ratio}")

        # Dashboard aktualisieren
        ai.update_dashboard()

        # WebSocket Broadcast
        ai.broadcast_dashboard()

        # Telegram Nachricht
        ai.send_signal(signal)

    print()

    print("Workflow erfolgreich beendet.")


if __name__ == "__main__":
    main()
