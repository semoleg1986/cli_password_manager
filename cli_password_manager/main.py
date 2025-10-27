from cli_password_manager.cli.menu import App
from cli_password_manager.core.auth import AuthManager


def main() -> None:
    """
    Точка входа для командного интерфейса (CLI) Password Manager.

    Эта функция создаёт экземпляр приложения `App` и запускает его метод `run`,
    который отвечает за интерактивное взаимодействие с пользователем.

    :return: None
    """
    auth = AuthManager()
    if not auth.authenticate():
        print("Доступ запрещён. Завершение работы.")
        return
    app = App()
    app.run()


if __name__ == "__main__":
    main()
