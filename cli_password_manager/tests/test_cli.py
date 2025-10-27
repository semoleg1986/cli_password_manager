import pytest

from cli_password_manager.cli.menu import App


def test_print_help(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Проверяет, что метод help() выводит доступные команды.
    """
    app = App()
    app.help()
    captured = capsys.readouterr()
    assert "Доступные команды" in captured.out
    assert "add" in captured.out
    assert "exit" in captured.out


def test_exit_sets_running_false(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Проверяет, что после вызова exit() флаг running становится False
    и выводится сообщение о завершении программы.
    """
    app = App()
    app.exit()
    assert app.running is False
    captured = capsys.readouterr()
    assert "Программа завершена" in captured.out
