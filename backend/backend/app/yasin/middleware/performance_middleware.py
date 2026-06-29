"""
Performance Middleware
für Yasin AI.
"""

import time

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.yasin.utils import get_logger


logger = get_logger("performance")


class PerformanceMiddleware(
    BaseHTTPMiddleware
):
    """
    Misst die Laufzeit aller
    HTTP-Requests.
    """

    HEADER_NAME = "X-Response-Time"

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        start = time.perf_counter()

        response = await call_next(
            request
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        response.headers[
            self.HEADER_NAME
        ] = f"{elapsed:.2f} ms"

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"{elapsed:.2f} ms"
        )

        return response
