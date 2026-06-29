"""
Beispiel für die Verwendung der
Yasin-Konfiguration.
"""

from app.yasin.config.yasin_ai_config import (
    get_ai_config,
)

from app.yasin.config.yasin_risk_config import (
    get_risk_config,
)

from app.yasin.config.yasin_strategy_config import (
    get_strategy_config,
)

from app.yasin.config.yasin_indicator_config import (
    get_indicator_config,
)

from app.yasin.config.yasin_dashboard_config import (
    get_dashboard_config,
)

from app.yasin.config.yasin_telegram_config import (
    get_telegram_config,
)

from app.yasin.config.yasin_database_config import (
    get_database_config,
)

from app.yasin.config.yasin_scheduler_config import (
    get_scheduler_config,
)


def main():

    print("=" * 60)
    print("YASIN AI CONFIGURATION")
    print("=" * 60)

    print("\nAI CONFIG")
    print(get_ai_config())

    print("\nRISK CONFIG")
    print(get_risk_config())

    print("\nSTRATEGY CONFIG")
    print(get_strategy_config())

    print("\nINDICATOR CONFIG")
    print(get_indicator_config())

    print("\nDASHBOARD CONFIG")
    print(get_dashboard_config())

    print("\nTELEGRAM CONFIG")
    print(get_telegram_config())

    print("\nDATABASE CONFIG")
    print(get_database_config())

    print("\nSCHEDULER CONFIG")
    print(get_scheduler_config())

    print("\nKonfiguration erfolgreich geladen.")


if __name__ == "__main__":
    main()
