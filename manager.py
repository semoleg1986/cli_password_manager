import hashlib
from pathlib import Path
from typing import Tuple

from constants import PASSWORDS_FILE
from utils.storage import load_data, save_data


class EmptyInputError(Exception):
    """Пустой ввод"""


class PasswordNotFoundError(Exception):
    """Пароль для указанного сайта не найден."""


def hash_password(password: str) -> str:
    """
    Хеширование пароля метод SHA256
    :param password: Исходный пароль
    :type password: str
    :return: Хеш пароля
    :rtype: str
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


class PasswordManager:
    def __init__(self, storage_path: Path = PASSWORDS_FILE):
        self.storage_path = storage_path
        self.data = load_data(storage_path)

    def add_password(self, site: str, username: str, password: str) -> None:
        if not all([site, username, password]):
            raise EmptyInputError("Все поля должны быть заполнены")

        self.data[site] = {"username": username, "password": hash_password(password)}
        save_data(self.storage_path, self.data)

    def find_password(self, site: str) -> Tuple[str, str, str]:
        try:
            record = self.data[site]
        except KeyError:
            raise PasswordNotFoundError(f"Сайт {site} не найден.")
        return site, record["username"], record["password"]

    def remove_password(self, site: str) -> None:
        try:
            self.data.pop(site)
        except KeyError:
            raise PasswordNotFoundError(f"Сайт {site} не найден.")
        save_data(self.storage_path, self.data)
