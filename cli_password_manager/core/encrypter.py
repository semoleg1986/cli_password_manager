import os
from pathlib import Path

from cryptography.fernet import Fernet
from dotenv import load_dotenv

from cli_password_manager.core.constants import KEY_FILE as KEY_FILE_PATH

load_dotenv()

key_file_path = Path(KEY_FILE_PATH)
env_key = os.getenv("PASSWORD_MANAGER_KEY")

if env_key:
    KEY = env_key.encode()
elif key_file_path.exists():
    KEY = key_file_path.read_bytes()
else:
    KEY = Fernet.generate_key()
    key_file_path.write_bytes(KEY)

f = Fernet(KEY)


def encrypt_password(password: str) -> str:
    """
    Шифрует пароль с использованием Fernet.

    :param password: Пароль для шифрования.
    :type password: str
    :return: Зашифрованный пароль в виде строки.
    :rtype: str
    """
    return f.encrypt(password.encode("utf-8")).decode("utf-8")


def decrypt_password(encrypted_password: str) -> str:
    """
    Расшифровывает пароль, зашифрованный с помощью Fernet.

    :param encrypted_password: Зашифрованный пароль.
    :type encrypted_password: str
    :return: Исходный пароль в виде строки.
    :rtype: str
    """
    return f.decrypt(encrypted_password.encode("utf-8")).decode("utf-8")
