# AI Empire Pro V8

AI Empire Pro V8 ist eine modulare KI-, Trading-, Video- und Automatisierungsplattform mit modernem Dashboard, REST-API und WebSocket-Unterstützung.

---

# Funktionen

- KI-Assistent (OpenAI)
- Trading Dashboard
- Portfolio Verwaltung
- Binance Integration
- CoinGecko Integration
- Telegram Bot
- Video Studio
- Gameification
- Aufgabenverwaltung
- Job Scheduler
- Backup System
- Benutzerverwaltung
- JWT Login
- REST API
- WebSocket Live Updates
- Responsive Dashboard

---

# Voraussetzungen

- Node.js >= 20
- MongoDB >= 7
- npm

---

# Installation

Repository klonen

```bash
git clone <repository>
cd ai-empire-pro-v8
```

Pakete installieren

```bash
npm install
```

Environment erstellen

```bash
cp .env.example .env
```

MongoDB starten

```bash
mongod
```

Projekt starten

```bash
npm run dev
```

oder

```bash
npm start
```

---

# Docker

Projekt starten

```bash
docker compose up --build
```

Projekt stoppen

```bash
docker compose down
```

---

# Projektstruktur

```
assets/
config/
server/
├── controllers/
├── middleware/
├── models/
├── routes/
├── services/
├── utils/
uploads/
storage/
logs/
backups/
```

---

# API

```
POST /api/auth/login
POST /api/auth/register

GET /api/dashboard

POST /api/assistant/chat

GET /api/trading

GET /api/video

GET /api/game

GET /api/tools

GET /api/setup
```

---

# Sicherheit

- JWT Authentication
- Helmet
- Rate Limiter
- CORS
- Passwort Hashing
- Request Logger
- Error Handler

---

# Version

AI Empire Pro V8

Version 8.0.0

---

# Lizenz

MIT License
