from datetime import datetime


class YasinTelegramMessageBuilder:
    """
    Erstellt alle Telegram-Nachrichten
    von Yasin AI.
    """

    @staticmethod
    def new_signal(signal) -> str:

        return f"""
🤖 <b>YASIN AI SIGNAL</b>

📊 Symbol: <b>{signal.symbol}</b>
📈 Richtung: <b>{signal.direction}</b>

🎯 Entry: <b>{signal.entry}</b>

🛑 Stop Loss:
{signal.stop_loss}

🎯 TP1:
{signal.take_profit_1}

🎯 TP2:
{signal.take_profit_2}

🎯 TP3:
{signal.take_profit_3}

⚖️ RR:
{signal.risk_reward_ratio:.2f}

⭐ Qualität:
{signal.quality_score:.1f} %

🧠 Analyse:

{signal.yasin_analysis}

🕒
{datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}
"""

    @staticmethod
    def tp1(signal):

        return f"""
🎯 TP1 ERREICHT

{signal.symbol}

Gewinn wurde bestätigt.

Trade läuft weiter.
"""

    @staticmethod
    def tp2(signal):

        return f"""
🎯 TP2 ERREICHT

{signal.symbol}

Starker Trade.

Trailing Stop empfohlen.
"""

    @staticmethod
    def tp3(signal):

        return f"""
🏆 TP3 ERREICHT

{signal.symbol}

Trade vollständig abgeschlossen.

Glückwunsch!
"""

    @staticmethod
    def stop_loss(signal):

        return f"""
🛑 STOP LOSS

{signal.symbol}

Trade beendet.

Risikomanagement eingehalten.
"""

    @staticmethod
    def trade_closed(signal):

        return f"""
✅ TRADE GESCHLOSSEN

{signal.symbol}

Status:

{signal.status}

Profit:

{signal.realized_profit}

Performance:

{signal.realized_profit_percent:.2f} %
"""

    @staticmethod
    def system(message: str):

        return f"""
🤖 YASIN AI

{message}
"""

    @staticmethod
    def statistics(statistics):

        return f"""
📊 YASIN PERFORMANCE

Trades:

{statistics.total_trades}

Winrate:

{statistics.win_rate:.2f} %

Profit Factor:

{statistics.profit_factor:.2f}

Net Profit:

{statistics.net_profit}
"""
