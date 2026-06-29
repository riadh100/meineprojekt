"""
Security Headers Middleware
für Yasin AI.
"""

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)


class SecurityHeadersMiddleware(
    BaseHTTPMiddleware
):
    """
    Fügt allen HTTP-Responses
    sicherheitsrelevante Header hinzu.
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        response = await call_next(
            request
        )

        response.headers[
            "X-Content-Type-Options"
        ] = "nosniff"

        response.headers[
            "X-Frame-Options"
        ] = "DENY"

        response.headers[
            "Referrer-Policy"
        ] = "strict-origin-when-cross-origin"

        response.headers[
            "Permissions-Policy"
        ] = "geolocation=(), camera=(), microphone=()"

        response.headers[
            "Content-Security-Policy"
        ] = (
            "default-src 'self'; "
            "img-src 'self' data:; "
            "style-src 'self' 'unsafe-inline'; "
            "script-src 'self'; "
            "connect-src 'self' ws: wss:;"
        )

        response.headers[
            "Strict-Transport-Security"
        ] = (
            "max-age=31536000; "
            "includeSubDomains"
        )

        return response
