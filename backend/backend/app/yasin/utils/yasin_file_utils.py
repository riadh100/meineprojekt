import csv
import json
from pathlib import Path
from datetime import datetime


def ensure_directory(
    directory: str,
):
    """
    Erstellt ein Verzeichnis,
    falls es nicht existiert.
    """

    Path(directory).mkdir(
        parents=True,
        exist_ok=True,
    )


def write_json(
    file_path: str,
    data,
):

    ensure_directory(
        Path(file_path).parent
    )

    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def read_json(
    file_path: str,
):

    with open(
        file_path,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def write_csv(
    file_path: str,
    rows: list[dict],
):

    if not rows:
        return

    ensure_directory(
        Path(file_path).parent
    )

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys(),
        )

        writer.writeheader()

        writer.writerows(rows)


def read_csv(
    file_path: str,
):

    with open(
        file_path,
        newline="",
        encoding="utf-8",
    ) as file:

        return list(
            csv.DictReader(file)
        )


def write_text(
    file_path: str,
    content: str,
):

    ensure_directory(
        Path(file_path).parent
    )

    Path(file_path).write_text(
        content,
        encoding="utf-8",
    )


def read_text(
    file_path: str,
):

    return Path(file_path).read_text(
        encoding="utf-8",
    )


def backup_name(
    filename: str,
):

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S"
    )

    path = Path(filename)

    return (
        f"{path.stem}_{timestamp}"
        f"{path.suffix}"
    )
