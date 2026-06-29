"""
API-Fehler
für Yasin AI.
"""


class ApiException(Exception):
    """
    Wird ausgelöst, wenn während einer
    REST-API- oder WebSocket-Kommunikation
    ein Fehler auftritt.
    """

    def __init__(
        self,
        message: str = "API-Fehler.",
        status_code: int = 500,
    ):

        self.status_code = status_code

        super().__init__(message)

    def __str__(self) -> str:

        return (
            f"API Error "
            f"[HTTP {self.status_code}]: "
            f"{self.args[0]}"
        )
