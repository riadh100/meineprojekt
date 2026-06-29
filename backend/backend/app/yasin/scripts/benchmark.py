"""
Benchmark-Skript für Yasin AI.
Misst die Performance der wichtigsten
Systemkomponenten.
"""

import time
import tracemalloc

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)


def benchmark(name, func):

    tracemalloc.start()

    start = time.perf_counter()

    func()

    duration = time.perf_counter() - start

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "name": name,
        "time": duration,
        "memory": peak / 1024 / 1024,
    }


def print_result(result):

    print("-" * 60)

    print(f"Test       : {result['name']}")
    print(f"Laufzeit   : {result['time']:.4f}s")
    print(f"RAM Peak   : {result['memory']:.2f} MB")


def main():

    print("=" * 60)
    print("YASIN AI BENCHMARK")
    print("=" * 60)

    service = YasinAIService()

    benchmarks = [

        benchmark(
            "Analyse",
            service.run_analysis,
        ),

        benchmark(
            "Signal Engine",
            service.generate_signals,
        ),

        benchmark(
            "Monitoring",
            service.monitor_trades,
        ),

        benchmark(
            "Dashboard",
            service.update_dashboard,
        ),

        benchmark(
            "Statistik",
            service.update_statistics,
        ),

        benchmark(
            "Backtesting",
            service.run_backtest,
        ),

    ]

    print()

    print("Ergebnisse")

    for result in benchmarks:

        print_result(result)

    print()

    print("Benchmark abgeschlossen.")


if __name__ == "__main__":

    main()
