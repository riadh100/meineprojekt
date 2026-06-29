# Yasin AI – Datenbankschema

## Übersicht

Die Datenbank basiert auf PostgreSQL und SQLAlchemy. Alle Kernmodule
verwenden ein gemeinsames relationales Datenmodell.

---

# Entity-Relationship-Diagramm

```
               Signals
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
 Trade History        Statistics
        │                   │
        └─────────┬─────────┘
                  ▼
             Dashboard Cache
                  │
                  ▼
             Backtesting
```

---

# Tabelle: signals

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| id | BIGINT | Primärschlüssel |
| symbol | VARCHAR(20) | Handelssymbol |
| market | VARCHAR(20) | Markt |
| direction | VARCHAR(10) | BUY / SELL |
| entry | NUMERIC | Einstieg |
| stop_loss | NUMERIC | Stop Loss |
| take_profit_1 | NUMERIC | TP1 |
| take_profit_2 | NUMERIC | TP2 |
| take_profit_3 | NUMERIC | TP3 |
| quality_score | FLOAT | Qualitätsbewertung |
| risk_reward_ratio | FLOAT | Chance/Risiko |
| status | VARCHAR(20) | Aktueller Status |
| created_at | TIMESTAMP | Erstellungszeit |

---

# Tabelle: statistics

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| id | BIGINT | Primärschlüssel |
| market | VARCHAR(20) | Markt |
| total_trades | INTEGER | Anzahl Trades |
| winning_trades | INTEGER | Gewinne |
| losing_trades | INTEGER | Verluste |
| gross_profit | NUMERIC | Bruttogewinn |
| gross_loss | NUMERIC | Bruttoverlust |
| profit_factor | FLOAT | Profit Factor |
| drawdown | FLOAT | Max. Drawdown |
| updated_at | TIMESTAMP | Letzte Aktualisierung |

---

# Tabelle: backtesting

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| id | BIGINT | Primärschlüssel |
| market | VARCHAR(20) | Markt |
| timeframe | VARCHAR(10) | Timeframe |
| initial_balance | NUMERIC | Startkapital |
| final_balance | NUMERIC | Endkapital |
| profit | NUMERIC | Gewinn |
| win_rate | FLOAT | Gewinnquote |
| created_at | TIMESTAMP | Erstellungszeit |

---

# Beziehungen

- Signals → Statistics
- Signals → Backtesting
- Statistics → Dashboard
- Dashboard → WebSocket

---

# Indizes

- IDX_SIGNALS_SYMBOL
- IDX_SIGNALS_MARKET
- IDX_SIGNALS_STATUS
- IDX_STATISTICS_MARKET
- IDX_BACKTESTING_MARKET

---

# Constraints

- Primärschlüssel
- Fremdschlüssel
- NOT NULL
- UNIQUE
- CHECK Constraints

---

# ORM

Alle Tabellen werden mit SQLAlchemy ORM verwaltet.
