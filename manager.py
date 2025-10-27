import hashlib
import json
from pathlib import Path
from typing import Any, Dict

from constants import PASSWORDS_FILE


class EmptyInputError(Exception):
    """Пустой ввод"""


def hash_password(password: str) -> str:
    """
    Хеширование пароля метод SHA256
    :param password: Исходный пароль
    :type password: str
    :return: Хеш пароля
    :rtype: str
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def save_data(path: Path, data: Dict[str, Any]) -> None:
    """
    Сохраняет данные в JSON-файл.
    """
    json_text = json.dumps(data, indent=4, ensure_ascii=False)
    path.write_text(json_text, encoding="utf-8")


def load_data(path: Path) -> Dict[str, Any]:
    """
    Загружает данные из JSON-файла.
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


class PasswordManager:
    def __init__(self, storage_path: Path = PASSWORDS_FILE):
        self.storage_path = storage_path
        self.data = load_data(storage_path)

    def add_password(self, site: str, username: str, password: str) -> None:
        if not all([site, username, password]):
            raise EmptyInputError("Все поля должны быть заполнены")

        self.data[site] = {"username": username, "password": hash_password(password)}
        save_data(self.storage_path, self.data)
