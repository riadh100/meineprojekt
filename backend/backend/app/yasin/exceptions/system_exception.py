"""
Systemfehler
für Yasin AI.
"""


class SystemException(Exception):
    """
    Wird ausgelöst, wenn ein allgemeiner
    Systemfehler auftritt, der keiner
    spezifischen Fehlerklasse zugeordnet
    werden kann.
    """

    def __init__(
        self,
        message: str = "Systemfehler.",
        component: str | None = None,
    ):

        self.component = component

        super().__init__(message)

    def __str__(self) -> str:

        if self.component:

            return (
                f"System Error "
                f"[{self.component}]: "
                f"{self.args[0]}"
            )

        return (
            f"System Error: "
            f"{self.args[0]}"
        )
