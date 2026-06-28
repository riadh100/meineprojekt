from dataclasses import dataclass


@dataclass
class RiskCalculation:
    account_balance: float
    risk_percent: float
    risk_amount: float
    entry_price: float
    stop_loss: float
    stop_distance: float
    position_size: float
    risk_reward_ratio: float
    max_open_positions: int
    approved: bool


class YasinRiskManagementService:
    """
    Zentrales Risk Management von Yasin AI.

    Verantwortlich für:
    - Positionsgröße
    - maximales Risiko
    - Risk/Reward
    - Trade-Freigabe
    """

    DEFAULT_MAX_OPEN_POSITIONS = 3
    MINIMUM_RISK_REWARD = 2.0

    def calculate(
        self,
        *,
        account_balance: float,
        risk_percent: float,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
        open_positions: int,
        max_open_positions: int | None = None,
    ) -> RiskCalculation:

        max_positions = (
            max_open_positions
            or self.DEFAULT_MAX_OPEN_POSITIONS
        )

        risk_amount = (
            account_balance * risk_percent / 100
        )

        stop_distance = abs(
            entry_price - stop_loss
        )

        if stop_distance <= 0:
            position_size = 0.0
        else:
            position_size = (
                risk_amount / stop_distance
            )

        reward = abs(
            take_profit - entry_price
        )

        rr = (
            reward / stop_distance
            if stop_distance > 0
            else 0.0
        )

        approved = (
            open_positions < max_positions
            and rr >= self.MINIMUM_RISK_REWARD
            and position_size > 0
        )

        return RiskCalculation(
            account_balance=account_balance,
            risk_percent=risk_percent,
            risk_amount=round(risk_amount, 2),
            entry_price=entry_price,
            stop_loss=stop_loss,
            stop_distance=round(stop_distance, 5),
            position_size=round(position_size, 4),
            risk_reward_ratio=round(rr, 2),
            max_open_positions=max_positions,
            approved=approved,
        )

    def validate(
        self,
        calculation: RiskCalculation,
    ) -> bool:
        return calculation.approved

    def can_open_trade(
        self,
        open_positions: int,
        max_open_positions: int,
    ) -> bool:

        return open_positions < max_open_positions

    def calculate_risk_amount(
        self,
        balance: float,
        risk_percent: float,
    ) -> float:

        return round(
            balance * risk_percent / 100,
            2,
        )

    def calculate_position_size(
        self,
        risk_amount: float,
        stop_distance: float,
    ) -> float:

        if stop_distance <= 0:
            return 0.0

        return round(
            risk_amount / stop_distance,
            4,
        )
