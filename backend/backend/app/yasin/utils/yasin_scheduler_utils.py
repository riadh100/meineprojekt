from datetime import datetime, timedelta


class SchedulerJob:
    """
    Repräsentiert einen Scheduler-Job.
    """

    def __init__(
        self,
        name: str,
        interval_seconds: int,
        priority: int = 5,
    ):
        self.name = name
        self.interval = timedelta(
            seconds=interval_seconds
        )
        self.priority = priority

        self.last_run = None
        self.next_run = datetime.utcnow()

        self.running = False

    def should_run(self):

        return (
            datetime.utcnow()
            >= self.next_run
        )

    def started(self):

        self.running = True

        self.last_run = datetime.utcnow()

    def finished(self):

        self.running = False

        self.next_run = (
            datetime.utcnow()
            + self.interval
        )

    def timeout(
        self,
        seconds: int,
    ) -> bool:

        if self.last_run is None:
            return False

        return (
            datetime.utcnow()
            - self.last_run
        ) > timedelta(seconds=seconds)


class SchedulerUtils:
    """
    Allgemeine Scheduler-Hilfsfunktionen.
    """

    @staticmethod
    def sort_jobs(
        jobs,
    ):

        return sorted(
            jobs,
            key=lambda job: (
                job.priority,
                job.next_run,
            ),
        )

    @staticmethod
    def running_jobs(
        jobs,
    ):

        return [
            job
            for job in jobs
            if job.running
        ]

    @staticmethod
    def waiting_jobs(
        jobs,
    ):

        return [
            job
            for job in jobs
            if not job.running
        ]

    @staticmethod
    def due_jobs(
        jobs,
    ):

        return [
            job
            for job in jobs
            if job.should_run()
        ]

    @staticmethod
    def scheduler_status(
        jobs,
    ):

        return {

            "total_jobs":
                len(jobs),

            "running":
                len(
                    SchedulerUtils.running_jobs(
                        jobs
                    )
                ),

            "waiting":
                len(
                    SchedulerUtils.waiting_jobs(
                        jobs
                    )
                ),

            "due":
                len(
                    SchedulerUtils.due_jobs(
                        jobs
                    )
                ),
        }
