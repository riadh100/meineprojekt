"""
Datenbankfehler
für Yasin AI.
"""


class DatabaseException(Exception):
    """
    Wird ausgelöst, wenn während einer
    Datenbankoperation ein Fehler auftritt.
    """

    def __init__(
        self,
        message: str = "Datenbankfehler.",
        operation: str | None = None,
    ):

        self.operation = operation

        super().__init__(message)

    def __str__(self) -> str:

        if self.operation:

            return (
                f"Database Error "
                f"({self.operation}): "
                f"{self.args[0]}"
            )

        return (
            f"Database Error: "
            f"{self.args[0]}"
        )
