"""
Autorisierungsfehler
für Yasin AI.
"""


class AuthorizationException(Exception):
    """
    Wird ausgelöst, wenn ein Benutzer
    nicht über ausreichende Berechtigungen
    verfügt.
    """

    def __init__(
        self,
        message: str = "Zugriff verweigert.",
        required_role: str | None = None,
    ):

        self.required_role = required_role

        super().__init__(message)

    def __str__(self) -> str:

        if self.required_role:

            return (
                f"Authorization Error "
                f"(Benötigte Rolle: "
                f"{self.required_role}): "
                f"{self.args[0]}"
            )

        return (
            f"Authorization Error: "
            f"{self.args[0]}"
        )
