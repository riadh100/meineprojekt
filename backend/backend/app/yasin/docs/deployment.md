# Yasin AI – Deployment Guide

## Übersicht

Diese Dokumentation beschreibt die Bereitstellung von Yasin AI
für Entwicklungs-, Test- und Produktionsumgebungen.

---

# Voraussetzungen

- Python 3.12+
- PostgreSQL 16+
- Redis 7+
- Docker
- Docker Compose
- Git
- Nginx

---

# Repository klonen

```bash
git clone https://github.com/company/yasin-ai.git

cd yasin-ai
```

---

# Umgebungsvariablen

.env

```env
DATABASE_URL=postgresql://user:password@postgres/yasin

REDIS_URL=redis://redis:6379

SECRET_KEY=CHANGE_ME

JWT_SECRET=CHANGE_ME

TELEGRAM_TOKEN=YOUR_TOKEN

TELEGRAM_CHAT_ID=YOUR_CHAT
```

---

# Docker

Docker Image erstellen

```bash
docker build -t yasin-ai .
```

Container starten

```bash
docker run -d \
-p 8000:8000 \
--env-file .env \
yasin-ai
```

---

# Docker Compose

```bash
docker compose up -d
```

Services

- FastAPI
- PostgreSQL
- Redis
- Nginx

---

# Datenbank

Migrationen

```bash
alembic upgrade head
```

---

# Redis

Start

```bash
redis-server
```

---

# Produktionsstart

```bash
uvicorn app.main:app \
--host 0.0.0.0 \
--port 8000 \
--workers 4
```

---

# Nginx

Reverse Proxy

```
Client

↓

Nginx

↓

FastAPI

↓

PostgreSQL
```

---

# SSL

Let's Encrypt

HTTPS

HTTP Redirect

---

# Backups

PostgreSQL

```bash
pg_dump
```

---

# Wiederherstellung

```bash
psql
```

---

# Logs

```bash
docker compose logs
```

---

# Updates

```bash
git pull

docker compose build

docker compose up -d
```

---

# Monitoring

- Health Endpoint
- Scheduler
- Dashboard
- Telegram
