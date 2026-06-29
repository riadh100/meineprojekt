"""
Zentrale Konstanten für Yasin AI.
"""

# ==========================================================
# Märkte
# ==========================================================

MARKET_GOLD = "GOLD"
MARKET_NAS100 = "NAS100"
MARKET_FOREX = "FOREX"
MARKET_CRYPTO = "CRYPTO"

MARKET_CUSTOM_1 = "CUSTOM_1"
MARKET_CUSTOM_2 = "CUSTOM_2"
MARKET_CUSTOM_3 = "CUSTOM_3"
MARKET_CUSTOM_4 = "CUSTOM_4"

SUPPORTED_MARKETS = [
    MARKET_GOLD,
    MARKET_NAS100,
    MARKET_FOREX,
    MARKET_CRYPTO,
    MARKET_CUSTOM_1,
    MARKET_CUSTOM_2,
    MARKET_CUSTOM_3,
    MARKET_CUSTOM_4,
]

# ==========================================================
# Signaltypen
# ==========================================================

BUY = "BUY"
SELL = "SELL"

SIGNAL_TYPES = [
    BUY,
    SELL,
]

# ==========================================================
# Signalstatus
# ==========================================================

STATUS_PENDING = "PENDING"

STATUS_APPROVED = "APPROVED"

STATUS_ACTIVE = "ACTIVE"

STATUS_TP1 = "TP1"

STATUS_TP2 = "TP2"

STATUS_TP3 = "TP3"

STATUS_STOP_LOSS = "STOP_LOSS"

STATUS_CLOSED = "CLOSED"

STATUS_REJECTED = "REJECTED"

# ==========================================================
# Timeframes
# ==========================================================

TIMEFRAME_M1 = "1m"
TIMEFRAME_M5 = "5m"
TIMEFRAME_M15 = "15m"
TIMEFRAME_M30 = "30m"

TIMEFRAME_H1 = "1h"
TIMEFRAME_H4 = "4h"

TIMEFRAME_D1 = "1d"

SUPPORTED_TIMEFRAMES = [
    TIMEFRAME_M1,
    TIMEFRAME_M5,
    TIMEFRAME_M15,
    TIMEFRAME_M30,
    TIMEFRAME_H1,
    TIMEFRAME_H4,
    TIMEFRAME_D1,
]

# ==========================================================
# WebSocket Events
# ==========================================================

EVENT_SIGNAL_CREATED = "SIGNAL_CREATED"

EVENT_TP1 = "TP1_REACHED"

EVENT_TP2 = "TP2_REACHED"

EVENT_TP3 = "TP3_REACHED"

EVENT_STOP_LOSS = "STOP_LOSS"

EVENT_TRADE_CLOSED = "TRADE_CLOSED"

EVENT_STATISTICS = "STATISTICS_UPDATED"

EVENT_SYSTEM = "SYSTEM_STATUS"

EVENT_NOTIFICATION = "NOTIFICATION"

EVENT_DASHBOARD = "DASHBOARD_UPDATE"

# ==========================================================
# Telegram
# ==========================================================

TG_SIGNAL = "SIGNAL"

TG_TP1 = "TP1"

TG_TP2 = "TP2"

TG_TP3 = "TP3"

TG_STOP_LOSS = "STOP_LOSS"

TG_STATISTICS = "STATISTICS"

TG_SYSTEM = "SYSTEM"

# ==========================================================
# Scheduler
# ==========================================================

JOB_ANALYSIS = "analysis"

JOB_MONITOR = "monitor"

JOB_STATISTICS = "statistics"

JOB_HEALTH = "health"

# ==========================================================
# Dashboard
# ==========================================================

WIDGET_SUMMARY = "summary"

WIDGET_SYSTEM = "system"

WIDGET_PERFORMANCE = "performance"

WIDGET_STATISTICS = "statistics"

WIDGET_MARKETS = "markets"

WIDGET_OPEN_TRADES = "open_trades"

WIDGET_LATEST_SIGNALS = "latest_signals"

WIDGET_NOTIFICATIONS = "notifications"

# ==========================================================
# AI
# ==========================================================

AI_APPROVED = "APPROVED"

AI_REJECTED = "REJECTED"

AI_REVIEW = "REVIEW"
