"""
WebSocket-Fehler
für Yasin AI.
"""


class WebSocketException(Exception):
    """
    Wird ausgelöst, wenn während der
    WebSocket-Kommunikation ein Fehler
    auftritt.
    """

    def __init__(
        self,
        message: str = "WebSocket-Fehler.",
        connection_id: str | None = None,
    ):

        self.connection_id = connection_id

        super().__init__(message)

    def __str__(self) -> str:

        if self.connection_id:

            return (
                f"WebSocket Error "
                f"[{self.connection_id}]: "
                f"{self.args[0]}"
            )

        return (
            f"WebSocket Error: "
            f"{self.args[0]}"
        )
