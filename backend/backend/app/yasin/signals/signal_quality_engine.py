from typing import Dict, List


class SignalQualityEngine:
    """
    Bewertet Trading-Signale anhand mehrerer Bestätigungen.
    Gibt nur hochwertige Signale für Yasin frei.
    """

    MINIMUM_QUALITY_SCORE = 75.0

    def calculate_quality_score(
        self,
        confirmations: Dict[str, bool],
        risk_reward_ratio: float,
        trend_strength: float,
        volatility_score: float,
    ) -> float:
        score = 0.0

        confirmation_weight = 50.0
        rr_weight = 20.0
        trend_weight = 20.0
        volatility_weight = 10.0

        active_confirmations = sum(1 for value in confirmations.values() if value)
        total_confirmations = max(len(confirmations), 1)

        score += (active_confirmations / total_confirmations) * confirmation_weight
        score += min(risk_reward_ratio / 3.0, 1.0) * rr_weight
        score += min(max(trend_strength, 0.0), 1.0) * trend_weight
        score += min(max(volatility_score, 0.0), 1.0) * volatility_weight

        return round(score, 2)

    def is_signal_approved(self, quality_score: float) -> bool:
        return quality_score >= self.MINIMUM_QUALITY_SCORE

    def get_failed_confirmations(
        self,
        confirmations: Dict[str, bool],
    ) -> List[str]:
        return [
            name for name, passed in confirmations.items()
            if not passed
        ]

    def build_quality_report(
        self,
        confirmations: Dict[str, bool],
        risk_reward_ratio: float,
        trend_strength: float,
        volatility_score: float,
    ) -> Dict:
        quality_score = self.calculate_quality_score(
            confirmations=confirmations,
            risk_reward_ratio=risk_reward_ratio,
            trend_strength=trend_strength,
            volatility_score=volatility_score,
        )

        return {
            "quality_score": quality_score,
            "approved": self.is_signal_approved(quality_score),
            "failed_confirmations": self.get_failed_confirmations(confirmations),
            "risk_reward_ratio": risk_reward_ratio,
            "trend_strength": trend_strength,
            "volatility_score": volatility_score,
        }
