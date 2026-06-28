from typing import Any


class MarketDataProvider:
    """
    Adapter zwischen Yasin AI und den bestehenden
    Market-Data-Services aus AI Empire Pro V8.

    Diese Klasse implementiert bewusst keine eigene
    API-Anbindung. Sie verwendet ausschließlich die
    bereits vorhandenen Services der V8-Architektur.
    """

    def __init__(
        self,
        market_data_service: Any,
    ):
        self.market_data_service = market_data_service

    def get_latest_price(
        self,
        symbol: str,
    ) -> float:
        """
        Liefert den aktuellen Marktpreis.
        """
        return self.market_data_service.get_latest_price(symbol)

    def get_latest_candle(
        self,
        symbol: str,
        timeframe: str,
    ):
        """
        Liefert die letzte abgeschlossene Kerze.
        """
        return self.market_data_service.get_latest_candle(
            symbol=symbol,
            timeframe=timeframe,
        )

    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        limit: int = 500,
    ):
        """
        Liefert historische Candles.
        """
        return self.market_data_service.get_candles(
            symbol=symbol,
            timeframe=timeframe,
            limit=limit,
        )

    def get_orderbook(
        self,
        symbol: str,
    ):
        """
        Optional: Orderbuchdaten (falls in V8 vorhanden).
        """
        if hasattr(self.market_data_service, "get_orderbook"):
            return self.market_data_service.get_orderbook(symbol)

        return None

    def get_ticker(
        self,
        symbol: str,
    ):
        """
        Optional: Tick-/Tickerdaten.
        """
        if hasattr(self.market_data_service, "get_ticker"):
            return self.market_data_service.get_ticker(symbol)

        return None

    def get_market_snapshot(
        self,
        symbol: str,
        timeframe: str = "15m",
        candle_limit: int = 500,
    ) -> dict:
        """
        Einheitlicher Einstiegspunkt für alle
        Analysemodule von Yasin AI.
        """
        return {
            "symbol": symbol,
            "price": self.get_latest_price(symbol),
            "candles": self.get_candles(
                symbol=symbol,
                timeframe=timeframe,
                limit=candle_limit,
            ),
            "last_candle": self.get_latest_candle(
                symbol=symbol,
                timeframe=timeframe,
            ),
            "orderbook": self.get_orderbook(symbol),
            "ticker": self.get_ticker(symbol),
        }
