"""
Error Handler Middleware
für Yasin AI.
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.yasin.exceptions import (
    ValidationException,
    AuthenticationException,
    AuthorizationException,
    ApiException,
)

from app.yasin.utils import get_logger


logger = get_logger("error_handler")


class ErrorHandlerMiddleware(
    BaseHTTPMiddleware
):
    """
    Behandelt alle unbehandelten
    Ausnahmen zentral.
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        try:

            return await call_next(
                request
            )

        except ValidationException as exc:

            logger.warning(str(exc))

            return JSONResponse(
                status_code=422,
                content={
                    "error": str(exc),
                },
            )

        except AuthenticationException as exc:

            logger.warning(str(exc))

            return JSONResponse(
                status_code=401,
                content={
                    "error": str(exc),
                },
            )

        except AuthorizationException as exc:

            logger.warning(str(exc))

            return JSONResponse(
                status_code=403,
                content={
                    "error": str(exc),
                },
            )

        except ApiException as exc:

            logger.error(str(exc))

            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "error": str(exc),
                },
            )

        except Exception as exc:

            logger.exception(exc)

            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                },
            )
