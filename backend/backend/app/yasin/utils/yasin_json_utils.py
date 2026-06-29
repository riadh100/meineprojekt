import json
from pathlib import Path
from typing import Any, Dict, Optional


def load_json_file(file_path: str | Path, default: Optional[Any] = None) -> Any:
    """
    Lädt eine JSON-Datei sicher.
    Gibt default zurück, wenn Datei fehlt oder ungültig ist.
    """
    path = Path(file_path)

    if not path.exists():
        return default

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return default


def save_json_file(file_path: str | Path, data: Any, indent: int = 4) -> bool:
    """
    Speichert Daten sicher als JSON-Datei.
    Erstellt fehlende Ordner automatisch.
    """
    path = Path(file_path)

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=indent)

        return True
    except OSError:
        return False


def json_to_string(data: Any, indent: int = 4) -> str:
    """
    Wandelt Python-Daten in einen JSON-String um.
    """
    try:
        return json.dumps(data, ensure_ascii=False, indent=indent)
    except (TypeError, ValueError):
        return "{}"


def string_to_json(json_string: str, default: Optional[Any] = None) -> Any:
    """
    Wandelt einen JSON-String sicher in Python-Daten um.
    """
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, TypeError):
        return default


def merge_json_dicts(base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Führt zwei JSON-Dictionaries rekursiv zusammen.
    updates überschreibt base.
    """
    result = base.copy()

    for key, value in updates.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = merge_json_dicts(result[key], value)
        else:
            result[key] = value

    return result


def is_valid_json(json_string: str) -> bool:
    """
    Prüft, ob ein String gültiges JSON ist.
    """
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False
