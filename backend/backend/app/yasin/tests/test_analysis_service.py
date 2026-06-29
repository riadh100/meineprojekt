"""
Unit-Tests für den
YasinAnalysisService.
"""

import pytest

from app.yasin.services.yasin_analysis_service import (
    YasinAnalysisService,
)


@pytest.fixture
def service():

    return YasinAnalysisService()


def test_analysis_returns_list(service):

    result = service.run(
        market="GOLD",
        timeframe="15m",
        strategy="ALL",
    )

    assert isinstance(result, list)


def test_analysis_contains_signals(service):

    signals = service.run(
        market="GOLD",
        timeframe="15m",
        strategy="ALL",
    )

    for signal in signals:

        assert signal.market
        assert signal.symbol
        assert signal.direction


def test_quality_score(service):

    signals = service.run(
        market="GOLD",
        timeframe="15m",
        strategy="ALL",
    )

    for signal in signals:

        assert (
            0
            <= signal.quality_score
            <= 100
        )


def test_confidence(service):

    signals = service.run(
        market="GOLD",
        timeframe="15m",
        strategy="ALL",
    )

    for signal in signals:

        assert (
            0
            <= signal.confidence
            <= 100
        )


def test_entry_price(service):

    signals = service.run(
        market="GOLD",
        timeframe="15m",
        strategy="ALL",
    )

    for signal in signals:

        assert signal.entry > 0
