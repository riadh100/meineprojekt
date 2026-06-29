"""
Logging Middleware
für Yasin AI.
"""

import time

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.yasin.utils import get_logger


logger = get_logger("middleware")


class LoggingMiddleware(
    BaseHTTPMiddleware
):
    """
    Protokolliert alle HTTP-Requests
    und Responses.
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        start = time.perf_counter()

        logger.info(
            f"→ {request.method} "
            f"{request.url.path}"
        )

        response = await call_next(
            request
        )

        duration = (
            time.perf_counter() - start
        ) * 1000

        logger.info(
            f"← {response.status_code} "
            f"{request.method} "
            f"{request.url.path} "
            f"({duration:.2f} ms)"
        )

        return response
