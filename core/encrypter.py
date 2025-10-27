import hashlib


def hash_password(password: str) -> str:
    """
    Хеширование пароля метод SHA256
    :param password: Исходный пароль
    :type password: str
    :return: Хеш пароля
    :rtype: str
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()
