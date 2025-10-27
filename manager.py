import hashlib


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


class PasswordManager:
    def __init__(self):
        self.data = {}

    def add_password(self, site: str, username: str, password: str) -> None:
        if not all([site, username, password]):
            raise EmptyInputError("Все поля должны быть заполнены")

        self.data[site] = {"username": username, "password": hash_password(password)}
        print(f"{self.data.get(site)}")
