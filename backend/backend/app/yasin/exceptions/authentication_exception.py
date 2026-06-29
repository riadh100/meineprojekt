"""
Authentifizierungsfehler
für Yasin AI.
"""


class AuthenticationException(Exception):
    """
    Wird ausgelöst, wenn die
    Authentifizierung fehlschlägt.
    """

    def __init__(
        self,
        message: str = "Authentifizierung fehlgeschlagen.",
        reason: str | None = None,
    ):

        self.reason = reason

        super().__init__(message)

    def __str__(self) -> str:

        if self.reason:

            return (
                f"Authentication Error "
                f"({self.reason}): "
                f"{self.args[0]}"
            )

        return (
            f"Authentication Error: "
            f"{self.args[0]}"
        )
