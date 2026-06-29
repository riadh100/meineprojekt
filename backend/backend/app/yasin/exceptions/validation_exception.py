"""
Validierungsfehler
für Yasin AI.
"""


class ValidationException(Exception):
    """
    Wird ausgelöst, wenn Eingabedaten,
    Konfigurationen oder Geschäftsregeln
    ungültig sind.
    """

    def __init__(
        self,
        message: str,
        field: str | None = None,
    ):

        self.field = field

        super().__init__(message)

    def __str__(self) -> str:

        if self.field:

            return (
                f"Validation Error "
                f"[{self.field}]: "
                f"{self.args[0]}"
            )

        return (
            f"Validation Error: "
            f"{self.args[0]}"
        )
