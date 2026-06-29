"""
CORS Middleware
für Yasin AI.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware,
)


DEFAULT_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


def setup_cors(
    app: FastAPI,
    origins: list[str] | None = None,
) -> None:
    """
    Konfiguriert Cross-Origin
    Resource Sharing.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins or DEFAULT_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=[
            "X-Request-ID",
        ],
    )
