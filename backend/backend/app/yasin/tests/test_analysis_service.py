import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_analysis_service import (
    YasinAnalysisService,
)


@pytest.fixture
def market_data():

    return Mock()


@pytest.fixture
def indicator_service():

    return Mock()


@pytest.fixture
def strategy_service():

    return Mock()


@pytest.fixture
def ai_service():

    return Mock()


@pytest.fixture
def service(
    market_data,
    indicator_service,
    strategy_service,
    ai_service,
):

    return YasinAnalysisService(
        market_data_service=market_data,
        indicator_service=indicator_service,
        strategy_service=strategy_service,
        ai_service=ai_service,
    )


def test_analyze_market(
    service,
    market_data,
):

    market_data.load.return_value = Mock()

    result = service.analyze(
        "GOLD"
    )

    assert result is not None


def test_indicator_analysis(
    service,
    indicator_service,
):

    indicator_service.calculate.return_value = {}

    result = service.calculate_indicators(
        "GOLD"
    )

    assert isinstance(
        result,
        dict,
    )


def test_strategy_execution(
    service,
    strategy_service,
):

    strategy_service.execute.return_value = []

    result = service.execute_strategy(
        "GOLD"
    )

    assert isinstance(
        result,
        list,
    )


def test_ai_confirmation(
    service,
    ai_service,
):

    ai_service.confirm.return_value = True

    assert (
        service.ai_confirmation(
            Mock()
        )
        is True
    )


def test_market_trend(
    service,
):

    result = service.market_trend(
        "GOLD"
    )

    assert result is not None


def test_analysis_status(
    service,
):

    result = service.status()

    assert result is not None
