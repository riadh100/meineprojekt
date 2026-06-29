# Yasin AI – Benutzerhandbuch

## Willkommen

Willkommen bei **Yasin AI**.

Dieses Handbuch erklärt die Bedienung des gesamten Systems – vom Dashboard
über Trading-Signale bis hin zu Backtesting und Administration.

---

# Dashboard

Nach dem Login erscheint das Dashboard.

Es zeigt:

- Live Trading Signale
- Performance
- Winrate
- Profit Factor
- Offene Trades
- Geschlossene Trades
- Marktstatus
- AI Status
- Systemstatus

---

# Trading Signale

Jedes Signal enthält:

- Symbol
- Markt
- BUY oder SELL
- Einstieg (Entry)
- Stop Loss
- Take Profit 1
- Take Profit 2
- Take Profit 3
- Risk/Reward
- Qualität
- Confidence

---

# Dashboard Widgets

Verfügbare Widgets:

- Performance
- Statistik
- Offene Positionen
- Letzte Signale
- Marktübersicht
- AI Entscheidungen
- Systemstatus

---

# REST API

Die REST API ist erreichbar unter:

```
/api/v1/yasin
```

Verfügbare Bereiche:

- Dashboard
- Signals
- Statistics
- Backtesting
- Health

---

# WebSocket

Live Updates:

```
/ws/dashboard
```

```
/ws/signals
```

---

# Telegram

Telegram informiert automatisch über:

- Neue Signale
- TP1
- TP2
- TP3
- Stop Loss
- Tagesstatistik
- Wochenstatistik
- Systemmeldungen

---

# Backtesting

Backtests ermöglichen:

- Strategie testen
- Historische Trades
- Winrate
- Profit Factor
- Drawdown
- Equity Curve

---

# Einstellungen

Konfigurierbar sind:

- Märkte
- Timeframes
- Strategien
- Risiko
- Telegram
- Dashboard
- Scheduler
- AI

---

# Benutzerrollen

Administrator

- Vollzugriff

Trader

- Dashboard
- Signale
- Backtesting

Viewer

- Nur Lesen

---

# Fehlerbehebung

Bei Problemen:

- Logs prüfen
- Health Endpoint aufrufen
- Dashboard kontrollieren
- Scheduler prüfen
- Datenbank prüfen
- Telegram testen

---

# Support

System:

Yasin AI V9

Support:

Administrator
