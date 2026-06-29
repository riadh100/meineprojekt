"""
Authentication Middleware
für Yasin AI.
"""

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.yasin.exceptions import (
    AuthenticationException,
)


class AuthenticationMiddleware(
    BaseHTTPMiddleware
):
    """
    Prüft alle eingehenden Requests
    auf gültige Authentifizierungsdaten.
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        token = request.headers.get(
            "Authorization"
        )

        api_key = request.headers.get(
            "X-API-Key"
        )

        if not token and not api_key:

            raise AuthenticationException(
                "Authentifizierung erforderlich.",
                reason="MISSING_CREDENTIALS",
            )

        # Platzhalter für JWT-/API-Key-Prüfung
        request.state.authenticated = True

        response = await call_next(
            request
        )

        return response
