from pathlib import Path
from typing import Dict, Tuple

from core.constants import PASSWORDS_FILE
from core.encrypter import hash_password
from core.exception import EmptyInputError, PasswordNotFoundError
from utils.logger import get_logger
from utils.storage import load_data, save_data

logger = get_logger(__name__)


class PasswordManager:
    """
    Менеджер паролей для добавления, поиска и удаления учетных данных.

    :param storage_path: Путь к файлу хранения паролей, по умолчанию PASSWORDS_FILE
    :type storage_path: Path
    """

    def __init__(self, storage_path: Path = PASSWORDS_FILE):
        self.storage_path = storage_path
        self.data = load_data(storage_path)
        logger.info("Менеджер паролей инициализирован, файл: %s", storage_path)

    def add_password(self, site: str, username: str, password: str) -> None:
        """
        Добавляет новый пароль для сайта.

        :param site: Название сайта
        :type site: str
        :param username: Имя пользователя
        :type username: str
        :param password: Пароль пользователя
        :type password: str
        :raises EmptyInputError: Если любое из полей пустое
        """
        if not all([site, username, password]):
            logger.warning("Попытка добавить пароль с пустыми полями")
            raise EmptyInputError("Все поля должны быть заполнены")

        self.data[site] = {"username": username, "password": hash_password(password)}
        save_data(self.storage_path, self.data)

    def list_passwords(self) -> Dict[str, Dict[str, str]]:
        """
        Возвращает словарь всех сохранённых паролей.

        :return: Словарь вида {site: {"username": username, "password": password}}
        """
        logger.info("Вывод всех сохранённых паролей")
        return self.data

    def find_password(self, site: str) -> Tuple[str, str, str]:
        """
        Находит пароль для заданного сайта.

        :param site: Название сайта
        :type site: str
        :return: Кортеж из (site, username, password)
        :rtype: Tuple[str, str, str]
        :raises PasswordNotFoundError: Если сайт не найден в базе
        """
        try:
            record = self.data[site]
        except KeyError:
            logger.warning("Попытка поиска пароля для несуществующего сайта '%s'", site)
            raise PasswordNotFoundError(f"Сайт {site} не найден.")
        logger.info("Пароль для сайта '%s' успешно найден", site)
        return site, record["username"], record["password"]

    def remove_password(self, site: str) -> None:
        """
        Удаляет пароль для заданного сайта.

        :param site: Название сайта
        :type site: str
        :raises PasswordNotFoundError: Если сайт не найден в базе
        """
        try:
            self.data.pop(site)
        except KeyError:
            logger.warning("Попытка удаления несуществующего сайта '%s'", site)
            raise PasswordNotFoundError(f"Сайт {site} не найден.")
        save_data(self.storage_path, self.data)
        logger.info("Пароль для сайта '%s' удалён", site)
