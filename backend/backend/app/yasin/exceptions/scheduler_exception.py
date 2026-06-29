"""
Scheduler-Fehler
für Yasin AI.
"""


class SchedulerException(Exception):
    """
    Wird ausgelöst, wenn während
    der Initialisierung oder Ausführung
    des Schedulers ein Fehler auftritt.
    """

    def __init__(
        self,
        message: str = "Scheduler-Fehler.",
        job_name: str | None = None,
    ):

        self.job_name = job_name

        super().__init__(message)

    def __str__(self) -> str:

        if self.job_name:

            return (
                f"Scheduler Error "
                f"[{self.job_name}]: "
                f"{self.args[0]}"
            )

        return (
            f"Scheduler Error: "
            f"{self.args[0]}"
        )
