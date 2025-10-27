import hashlib
from getpass import getpass
from pathlib import Path

from cli_password_manager.core.constants import MASTER_KEY

MASTER_FILE = Path(MASTER_KEY)


class AuthManager:
    """
    Управляет аутентификацией через мастер-пароль.
    """

    def __init__(self) -> None:
        MASTER_FILE.parent.mkdir(exist_ok=True)

    def _hash(self, password: str) -> str:
        """Возвращает SHA-256 хэш пароля"""
        return hashlib.sha256(password.encode()).hexdigest()

    def setup(self) -> None:
        """Создаёт мастер-пароль при первом запуске"""
        if not MASTER_FILE.exists():
            print("Установка мастер-пароля.")
            while True:
                p1 = getpass("Введите новый пароль: ")
                p2 = getpass("Повторите пароль: ")
                if p1 != p2:
                    print("Пароли не совпадают.")
                elif not p1.strip():
                    print("Пароль не может быть пустым.")
                else:
                    MASTER_FILE.write_text(self._hash(p1))
                    print("Мастер-пароль сохранён.")
                    break

    def authenticate(self) -> bool:
        """
        Проверяет мастер-пароль перед запуском приложения

        :return: Возвращает булевое значение
        :rtype: bool
        """
        self.setup()
        stored_hash = MASTER_FILE.read_text().strip()
        password = getpass("Введите мастер-пароль: ")
        if self._hash(password) == stored_hash:
            print("Доступ разрешён.")
            return True
        print("Неверный пароль.")
        return False
