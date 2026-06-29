"""
Beispiel für den Telegram-Service
von Yasin AI.
"""

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)


def main():

    telegram = YasinTelegramService()

    print("=" * 60)
    print("YASIN AI TELEGRAM")
    print("=" * 60)

    print("\nTelegram-Demo wird gestartet...")

    # Beispiel-Signal
    signal = {
        "market": "GOLD",
        "symbol": "XAUUSD",
        "direction": "BUY",
        "entry": 2500.00,
        "stop_loss": 2490.00,
        "take_profit_1": 2510.00,
        "take_profit_2": 2520.00,
        "take_profit_3": 2530.00,
        "quality": 96.5,
        "confidence": 94.2,
    }

    print("\nSignal senden...")
    telegram.send_signal(signal)

    print("TP1 senden...")
    telegram.send_tp(signal, "TP1")

    print("TP2 senden...")
    telegram.send_tp(signal, "TP2")

    print("TP3 senden...")
    telegram.send_tp(signal, "TP3")

    print("Stop Loss senden...")
    telegram.send_stop_loss(signal)

    print("Tagesstatistik senden...")
    telegram.send_statistics("daily")

    print("Wochenstatistik senden...")
    telegram.send_statistics("weekly")

    print("Health Report senden...")
    telegram.send_health_report()

    print("Systemmeldung senden...")
    telegram.send_system_message(
        "Yasin AI läuft erfolgreich."
    )

    print("\nTelegram-Demo abgeschlossen.")


if __name__ == "__main__":
    main()
