"""
Request-ID Middleware
für Yasin AI.
"""

import uuid

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)


class RequestIDMiddleware(
    BaseHTTPMiddleware
):
    """
    Vergibt für jede Anfrage
    eine eindeutige Request-ID.
    """

    HEADER_NAME = "X-Request-ID"

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        request_id = request.headers.get(
            self.HEADER_NAME
        )

        if not request_id:

            request_id = str(
                uuid.uuid4()
            )

        request.state.request_id = (
            request_id
        )

        response = await call_next(
            request
        )

        response.headers[
            self.HEADER_NAME
        ] = request_id

        return response
