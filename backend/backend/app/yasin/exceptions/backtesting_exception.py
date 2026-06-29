"""
Backtesting-Fehler
für Yasin AI.
"""


class BacktestingException(Exception):
    """
    Wird ausgelöst, wenn während
    eines Backtests ein Fehler
    auftritt.
    """

    def __init__(
        self,
        message: str = "Backtesting-Fehler.",
        dataset: str | None = None,
    ):

        self.dataset = dataset

        super().__init__(message)

    def __str__(self) -> str:

        if self.dataset:

            return (
                f"Backtesting Error "
                f"[{self.dataset}]: "
                f"{self.args[0]}"
            )

        return (
            f"Backtesting Error: "
            f"{self.args[0]}"
        )
