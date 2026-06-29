"""
Beispiel für die Verwendung der
Yasin AI REST API.
"""

import requests


BASE_URL = "http://localhost:8000/api/v1/yasin"

TOKEN = "YOUR_API_TOKEN"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}


def health():

    response = requests.get(
        f"{BASE_URL}/health",
        headers=HEADERS,
    )

    print("Health")
    print(response.json())


def dashboard():

    response = requests.get(
        f"{BASE_URL}/dashboard",
        headers=HEADERS,
    )

    print("\nDashboard")
    print(response.json())


def statistics():

    response = requests.get(
        f"{BASE_URL}/statistics",
        headers=HEADERS,
    )

    print("\nStatistics")
    print(response.json())


def open_signals():

    response = requests.get(
        f"{BASE_URL}/signals/open",
        headers=HEADERS,
    )

    print("\nOpen Signals")
    print(response.json())


def create_signal():

    payload = {

        "symbol": "XAUUSD",

        "market": "GOLD",

        "direction": "BUY",

        "entry": 2500,

        "stop_loss": 2490,

        "take_profit_1": 2510,

        "take_profit_2": 2520,

        "take_profit_3": 2530,

    }

    response = requests.post(
        f"{BASE_URL}/signals",
        headers=HEADERS,
        json=payload,
    )

    print("\nCreate Signal")
    print(response.json())


def run_backtest():

    payload = {

        "market": "GOLD",

        "timeframe": "15m",

        "balance": 10000,

    }

    response = requests.post(
        f"{BASE_URL}/backtesting/run",
        headers=HEADERS,
        json=payload,
    )

    print("\nBacktesting")
    print(response.json())


def main():

    print("=" * 60)
    print("YASIN AI REST API EXAMPLE")
    print("=" * 60)

    health()

    dashboard()

    statistics()

    open_signals()

    create_signal()

    run_backtest()


if __name__ == "__main__":
    main()
