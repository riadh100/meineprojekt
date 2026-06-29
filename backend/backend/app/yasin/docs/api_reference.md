# Yasin AI REST API Referenz

## Basis-URL

```
/api/v1/yasin
```

---

# Health

## GET /health

Prüft den Status des Systems.

### Response

```json
{
  "status": "online",
  "version": "9.0",
  "uptime": 52340
}
```

---

# Dashboard

## GET /dashboard

Liefert sämtliche Dashboard-Daten.

### Response

```json
{
  "performance": {},
  "statistics": {},
  "signals": [],
  "system": {}
}
```

---

# Signale

## GET /signals

Alle Signale abrufen.

## GET /signals/open

Nur offene Signale.

## GET /signals/{id}

Signal anhand der ID.

## POST /signals

Neues Signal erzeugen.

### Request

```json
{
  "symbol":"XAUUSD",
  "market":"GOLD",
  "direction":"BUY",
  "entry":2500,
  "stop_loss":2490,
  "take_profit_1":2510,
  "take_profit_2":2520,
  "take_profit_3":2530
}
```

---

## DELETE /signals/{id}

Signal löschen.

---

# Statistik

## GET /statistics

Alle Statistiken.

## GET /statistics/{market}

Marktstatistik.

---

# Backtesting

## POST /backtesting/run

Backtest starten.

### Request

```json
{
   "market":"GOLD",
   "timeframe":"15m",
   "balance":10000
}
```

---

# WebSocket

```
/ws/dashboard
```

Live Dashboard

```
/ws/signals
```

Live Trading Signale

---

# Fehlercodes

| Code | Bedeutung |
|------|-----------|
|200|OK|
|201|Erstellt|
|400|Ungültige Anfrage|
|401|Nicht autorisiert|
|403|Verboten|
|404|Nicht gefunden|
|422|Validierungsfehler|
|500|Interner Fehler|

---

# Authentifizierung

```
Authorization:

Bearer <TOKEN>
```

---

# Version

```
Yasin AI REST API V9
```
