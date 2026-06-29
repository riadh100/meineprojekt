"""
Datei- und Verzeichnisfunktionen
für Yasin AI.
"""

import json
import shutil
from pathlib import Path


def ensure_directory(
    path: str | Path,
) -> Path:
    """Verzeichnis erstellen, falls es nicht existiert."""
    directory = Path(path)
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    return directory


def file_exists(
    path: str | Path,
) -> bool:
    """Prüfen, ob eine Datei existiert."""
    return Path(path).exists()


def read_text(
    path: str | Path,
    encoding: str = "utf-8",
) -> str:
    """Textdatei lesen."""
    return Path(path).read_text(
        encoding=encoding
    )


def write_text(
    path: str | Path,
    content: str,
    encoding: str = "utf-8",
) -> None:
    """Textdatei schreiben."""
    Path(path).write_text(
        content,
        encoding=encoding,
    )


def read_json(
    path: str | Path,
):
    """JSON-Datei lesen."""
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def write_json(
    path: str | Path,
    data,
) -> None:
    """JSON-Datei schreiben."""
    with open(
        path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def copy_file(
    source: str | Path,
    destination: str | Path,
) -> None:
    """Datei kopieren."""
    shutil.copy2(
        source,
        destination,
    )


def move_file(
    source: str | Path,
    destination: str | Path,
) -> None:
    """Datei verschieben."""
    shutil.move(
        source,
        destination,
    )


def delete_file(
    path: str | Path,
) -> None:
    """Datei löschen."""

    file = Path(path)

    if file.exists():

        file.unlink()


def delete_directory(
    path: str | Path,
) -> None:
    """Verzeichnis löschen."""

    directory = Path(path)

    if directory.exists():

        shutil.rmtree(directory)
