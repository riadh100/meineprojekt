from dataclasses import dataclass
from typing import Iterable


@dataclass
class DrawdownResult:
    max_drawdown: float
    current_drawdown: float
    peak_equity: float
    lowest_equity: float


class DrawdownCalculator:
    """
    Berechnet Drawdown-Kennzahlen auf Basis einer Equity-Kurve.

    Erwartet eine chronologisch sortierte Liste von Kontoständen
    (Equity nach jedem abgeschlossenen Trade).
    """

    @staticmethod
    def calculate(equity_curve: Iterable[float]) -> DrawdownResult:
        equity = list(equity_curve)

        if not equity:
            return DrawdownResult(
                max_drawdown=0.0,
                current_drawdown=0.0,
                peak_equity=0.0,
                lowest_equity=0.0,
            )

        peak = equity[0]
        lowest = equity[0]

        max_drawdown = 0.0
        current_drawdown = 0.0

        for value in equity:

            if value > peak:
                peak = value

            if value < lowest:
                lowest = value

            if peak > 0:
                drawdown = ((peak - value) / peak) * 100
            else:
                drawdown = 0.0

            current_drawdown = drawdown

            if drawdown > max_drawdown:
                max_drawdown = drawdown

        return DrawdownResult(
            max_drawdown=round(max_drawdown, 2),
            current_drawdown=round(current_drawdown, 2),
            peak_equity=round(peak, 2),
            lowest_equity=round(lowest, 2),
        )
