# Yasin AI – Systemarchitektur

## Übersicht

Yasin AI besteht aus mehreren unabhängigen Modulen, die gemeinsam
ein vollständiges Trading-System bilden.

---

## Architektur

```
                     FastAPI
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
 REST API          WebSocket         Dashboard
      │                 │                 │
      └──────────────┬──┴─────────────────┘
                     ▼
               Yasin AI Service
                     │
 ┌───────────────────┼────────────────────┐
 ▼                   ▼                    ▼
Analysis       Signal Service       Monitor
 ▼                   ▼                    ▼
Indicators      Risk Management    Statistics
 ▼                   ▼                    ▼
Strategies      Trade Engine      Backtesting
                     │
                     ▼
               PostgreSQL
                     │
                     ▼
               Telegram Bot
```

---

## Hauptmodule

### Analysis

- Marktanalyse
- Trendbestimmung
- Indikatoren
- KI-Auswertung

### Signal Service

- Signalerstellung
- Speicherung
- Freigabe
- Verwaltung

### Monitor

- TP/SL Überwachung
- Statusänderungen
- Trade Closing

### Statistics

- Winrate
- Profit Factor
- Drawdown
- Performance

### Dashboard

- Live Daten
- WebSocket
- Widgets
- Statistiken

### Telegram

- Signale
- Statistiken
- Health Reports
- Systemmeldungen

### Scheduler

- Analyse
- Monitoring
- Statistik
- Telegram

---

## Datenfluss

```
Marktdaten
      │
      ▼
Analyse
      │
      ▼
Strategien
      │
      ▼
KI Bewertung
      │
      ▼
Signal
      │
      ▼
Monitoring
      │
      ▼
Dashboard
      │
      ▼
Telegram
```

---

## Technologien

- FastAPI
- PostgreSQL
- SQLAlchemy
- APScheduler
- WebSocket
- Pydantic
- Pytest

---

## Ziel

Yasin AI soll modular, erweiterbar, testbar und wartbar sein.
