from cli.menu import App


def main() -> None:
    """
    Точка входа для командного интерфейса (CLI) Password Manager.

    Эта функция создаёт экземпляр приложения `App` и запускает его метод `run`,
    который отвечает за интерактивное взаимодействие с пользователем.

    :return: None
    """
    app = App()
    app.run()


if __name__ == "__main__":
    main()
