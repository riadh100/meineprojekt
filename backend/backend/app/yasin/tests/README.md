# Yasin AI – Test Suite

Die Test-Suite von **Yasin AI** stellt sicher, dass alle Komponenten des Systems zuverlässig funktionieren. Sie umfasst Unit-, Integrations- und End-to-End-Tests und unterstützt automatisierte Testläufe in lokalen Entwicklungsumgebungen sowie in CI/CD-Pipelines.

---

# Teststruktur

```
tests/
│
├── test_analysis_service.py
├── test_backtesting_service.py
├── test_monitor_service.py
├── test_scheduler_service.py
├── test_api.py
├── test_websocket.py
├── test_dashboard.py
├── test_telegram.py
├── test_database.py
├── test_models.py
├── test_utils.py
├── test_exceptions.py
├── test_middleware.py
├── conftest.py
└── run_tests.py
```

---

# Testkategorien

## Unit-Tests

Prüfen einzelne Module isoliert.

- Analysis Service
- Backtesting
- Monitor
- Scheduler
- Modelle
- Utilities
- Exceptions

Starten:

```bash
python run_tests.py --unit
```

---

## Integrationstests

Prüfen das Zusammenspiel mehrerer Komponenten.

- REST API
- WebSocket
- Dashboard
- Telegram
- Datenbank
- Middleware

Starten:

```bash
python run_tests.py --integration
```

---

## End-to-End-Tests

Prüfen komplette Workflows.

Beispiele:

- Signalanalyse
- Trade-Ausführung
- Dashboard
- Scheduler
- Telegram-Benachrichtigung

Starten:

```bash
python run_tests.py --e2e
```

---

# Gesamte Test-Suite

```bash
python run_tests.py
```

---

# Coverage-Bericht

Coverage inklusive HTML-Report erzeugen:

```bash
python run_tests.py --coverage
```

Der HTML-Bericht wird anschließend im Verzeichnis:

```
htmlcov/
```

erstellt.

---

# Best Practices

- Neue Funktionen immer mit Tests ergänzen.
- Fehler zunächst reproduzierbar machen.
- Kleine, unabhängige Testfälle bevorzugen.
- Fixtures aus `conftest.py` wiederverwenden.
- Testdaten konsistent halten.
- CI/CD vor jedem Merge ausführen.

---

# CI/CD

Die Test-Suite ist für automatisierte Ausführung geeignet.

Empfohlener Ablauf:

1. Unit-Tests
2. Integrationstests
3. End-to-End-Tests
4. Coverage
5. Deployment

---

# Ziel

Die Test-Suite gewährleistet die Stabilität, Qualität und Wartbarkeit von **Yasin AI** und bildet die Grundlage für eine sichere Weiterentwicklung des Systems.
