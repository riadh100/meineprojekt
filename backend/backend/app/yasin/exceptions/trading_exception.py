"""
Trading-Fehler
für Yasin AI.
"""


class TradingException(Exception):
    """
    Wird ausgelöst, wenn während
    eines Trading-Vorgangs ein
    Fehler auftritt.
    """

    def __init__(
        self,
        message: str = "Trading-Fehler.",
        error_code: str | None = None,
    ):

        self.error_code = error_code

        super().__init__(message)

    def __str__(self) -> str:

        if self.error_code:

            return (
                f"Trading Error "
                f"[{self.error_code}]: "
                f"{self.args[0]}"
            )

        return (
            f"Trading Error: "
            f"{self.args[0]}"
        )
