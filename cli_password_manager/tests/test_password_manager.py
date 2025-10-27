import tempfile
from pathlib import Path

import pytest

from cli_password_manager.core.manager import (
    EmptyInputError,
    PasswordManager,
    PasswordNotFoundError,
)


@pytest.fixture
def temp_storage():
    """Создаёт временный файл для хранения паролей"""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "passwords.json"
        yield path


def test_add_password(temp_storage):
    pm = PasswordManager(storage_path=temp_storage)
    pm.add_password("github.com", "user123", "qwerty123")
    data = pm.list_passwords()

    assert "github.com" in data
    assert data["github.com"]["username"] == "user123"

    assert data["github.com"]["password"] != "qwerty123"


def test_add_empty_fields_raises(temp_storage):
    pm = PasswordManager(storage_path=temp_storage)
    with pytest.raises(EmptyInputError):
        pm.add_password("", "user", "pass")
    with pytest.raises(EmptyInputError):
        pm.add_password("site", "", "pass")
    with pytest.raises(EmptyInputError):
        pm.add_password("site", "user", "")


def test_find_password(temp_storage):
    pm = PasswordManager(storage_path=temp_storage)
    pm.add_password("github.com", "user123", "qwerty123")
    site, username, password = pm.find_password("github.com")

    assert site == "github.com"
    assert username == "user123"
    assert password == "qwerty123"


def test_find_nonexistent_raises(temp_storage):
    pm = PasswordManager(storage_path=temp_storage)
    with pytest.raises(PasswordNotFoundError):
        pm.find_password("nonexistent.com")


def test_remove_password(temp_storage):
    pm = PasswordManager(storage_path=temp_storage)
    pm.add_password("github.com", "user123", "qwerty123")
    pm.remove_password("github.com")

    with pytest.raises(PasswordNotFoundError):
        pm.find_password("github.com")


def test_remove_nonexistent_raises(temp_storage):
    pm = PasswordManager(storage_path=temp_storage)
    with pytest.raises(PasswordNotFoundError):
        pm.remove_password("nonexistent.com")
