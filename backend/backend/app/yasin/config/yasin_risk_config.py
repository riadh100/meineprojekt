from dataclasses import dataclass


@dataclass(frozen=True)
class RiskConfig:
    """
    Zentrale Risiko-Konfiguration
    für Yasin AI.
    """

    # Risiko

    max_risk_per_trade: float

    max_daily_risk: float

    max_total_drawdown: float

    max_open_positions: int

    # Positionsgröße

    default_position_size: float

    minimum_position_size: float

    maximum_position_size: float

    # Risk / Reward

    minimum_rr: float

    preferred_rr: float

    # Sicherheit

    stop_trading_after_daily_loss: bool

    stop_trading_after_drawdown: bool

    require_ai_confirmation: bool

    # Qualitätsfilter

    minimum_signal_quality: float

    minimum_confirmations: int


RISK_CONFIG = RiskConfig(

    # Risiko

    max_risk_per_trade=1.0,
    max_daily_risk=5.0,
    max_total_drawdown=15.0,
    max_open_positions=3,

    # Positionsgröße

    default_position_size=1.0,
    minimum_position_size=0.01,
    maximum_position_size=10.0,

    # RR

    minimum_rr=2.0,
    preferred_rr=3.0,

    # Sicherheit

    stop_trading_after_daily_loss=True,
    stop_trading_after_drawdown=True,
    require_ai_confirmation=True,

    # Qualität

    minimum_signal_quality=85.0,
    minimum_confirmations=4,
)


def get_risk_config():

    return RISK_CONFIG


def trading_allowed(
    *,
    current_drawdown: float,
    daily_loss: float,
):

    if (
        RISK_CONFIG.stop_trading_after_drawdown
        and current_drawdown
        >= RISK_CONFIG.max_total_drawdown
    ):
        return False

    if (
        RISK_CONFIG.stop_trading_after_daily_loss
        and daily_loss
        >= RISK_CONFIG.max_daily_risk
    ):
        return False

    return True


def signal_allowed(
    *,
    quality: float,
    confirmations: int,
    rr: float,
):

    return (
        quality
        >= RISK_CONFIG.minimum_signal_quality
        and confirmations
        >= RISK_CONFIG.minimum_confirmations
        and rr
        >= RISK_CONFIG.minimum_rr
    )
