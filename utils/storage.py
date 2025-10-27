import json
from pathlib import Path
from typing import Any, Dict


def save_data(path: Path, data: Dict[str, Any]) -> None:
    """
    Сохраняет данные в JSON-файл.

    :param path: путь к файлу для сохранения
    :param data: данные для записи в формате словаря
    :raises ValueError: если данные не могут быть сериализованы в JSON
    :raises OSError: если возникла ошибка при записи в файл
    """
    try:
        json_text = json.dumps(data, indent=4, ensure_ascii=False)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Ошибка сериализации данных в JSON: {e}") from e

    try:
        path.write_text(json_text, encoding="utf-8")
    except (OSError, PermissionError, FileNotFoundError) as e:
        raise OSError(f"Ошибка записи файла '{path}': {e}") from e


def load_data(path: Path) -> Dict[str, Any]:
    """
    Загружает данные из JSON-файла.

    Если файл не существует, создаётся пустой JSON-файл.
    Возвращает словарь, считанный из файла.

    :param path: Путь к JSON-файлу для чтения.
    :type path: Path
    :return: Словарь с данными из файла.
    :rtype: Dict[str, Any]
    :raises json.JSONDecodeError: Если файл содержит некорректный JSON.
    :raises OSError: Если произошла ошибка чтения или создания файла.
    """
    if not path.exists():
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("{}", encoding="utf-8")
        except OSError as e:
            raise OSError(f"Ошибка создания файла '{path}': {e}") from e

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Ошибка разбора JSON в файле '{path}': {e.msg}", e.doc, e.pos
        )
    except OSError as e:
        raise OSError(f"Ошибка чтения файла '{path}': {e}") from e
