from app.yasin.signals.signal_schema import YasinSignal


class YasinTelegramFormatter:
    """
    Erstellt einheitliche Telegram-Nachrichten
    für neue Signale und Trade-Updates.
    """

    @staticmethod
    def format_new_signal(signal: YasinSignal) -> str:
        return (
            "🧠 YASIN AI SIGNAL\n\n"
            f"📈 Markt: {signal.market.value}\n"
            f"💱 Symbol: {signal.symbol}\n"
            f"📊 Richtung: {signal.direction.value}\n\n"
            f"🎯 Entry: {signal.entry}\n"
            f"🛑 Stop Loss: {signal.stop_loss}\n\n"
            f"✅ TP1: {signal.take_profit_1}\n"
            f"✅ TP2: {signal.take_profit_2}\n"
            f"✅ TP3: {signal.take_profit_3}\n\n"
            f"⚖ Risk/Reward: {signal.risk_reward_ratio}:1\n"
            f"⭐ Qualität: {signal.quality_score:.1f}%\n\n"
            f"🤖 Analyse:\n"
            f"{signal.yasin_analysis}\n\n"
            f"🕒 {signal.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

    @staticmethod
    def format_tp1(signal: YasinSignal) -> str:
        return (
            "🎯 TP1 ERREICHT\n\n"
            f"{signal.symbol}\n"
            f"{signal.direction.value}\n\n"
            "Erstes Gewinnziel wurde erfolgreich erreicht."
        )

    @staticmethod
    def format_tp2(signal: YasinSignal) -> str:
        return (
            "🎯 TP2 ERREICHT\n\n"
            f"{signal.symbol}\n"
            f"{signal.direction.value}\n\n"
            "Zweites Gewinnziel wurde erfolgreich erreicht."
        )

    @staticmethod
    def format_tp3(signal: YasinSignal) -> str:
        return (
            "🏆 TP3 ERREICHT\n\n"
            f"{signal.symbol}\n"
            f"{signal.direction.value}\n\n"
            "Trade vollständig abgeschlossen."
        )

    @staticmethod
    def format_stop_loss(signal: YasinSignal) -> str:
        return (
            "🛑 STOP LOSS\n\n"
            f"{signal.symbol}\n"
            f"{signal.direction.value}\n\n"
            "Trade wurde mit Stop Loss beendet."
        )

    @staticmethod
    def format_trade_closed(signal: YasinSignal) -> str:
        return (
            "📌 TRADE BEENDET\n\n"
            f"Symbol: {signal.symbol}\n"
            f"Status: {signal.status}"
        )
