from tabulate import tabulate

from cli_password_manager.core.manager import (
    EmptyInputError,
    PasswordManager,
    PasswordNotFoundError,
)
from cli_password_manager.utils.logger import get_logger

logger = get_logger(__name__)


class App:
    """
    CLI-приложение для управления паролями.
    """

    COMMANDS = {
        "add": "добавить пароль",
        "find": "найти пароль",
        "delete": "удалить пароль",
        "list": "вывод всех паролей",
        "help": "показать список команд",
        "exit": "выйти из программы",
    }

    def __init__(self) -> None:
        """
        Инициализирует CLI-приложение.

        :ivar columns: Заголовки таблицы для отображения данных.
        :vartype columns: tuple[str, str, str]
        :ivar running: Флаг работы приложения.
        :vartype running: bool
        :ivar manager: Менеджер паролей.
        :vartype manager: PasswordManager
        """
        self.columns = ("Site", "Username", "Password")
        self.running = True
        self.manager = PasswordManager()

    def run(self) -> None:
        """
        Запускает главный цикл CLI.

        :raises Exception: При возникновении непредвиденной ошибки во время выполнения.
        """
        print("Введите 'help' для списка команд.")
        while self.running:
            try:
                cmd: list[str] = input("> ").strip().lower().split()
                if not cmd:
                    print("Пустая команда")
                    continue
                command = cmd[0]
                match command:
                    case "help":
                        self.help()
                    case "exit":
                        self.exit()
                    case "add":
                        self._add(cmd)
                    case "list":
                        self._list()
                    case "find":
                        self._find(cmd)
                    case "delete":
                        self._remove(cmd)
                    case _:
                        print(f'"{command}" такой команды нет')
                        logger.warning("Неизвестная команда: %s", command)

            except Exception as e:
                print("Неожиданная ошибка:", e)
                logger.exception("Неожиданная ошибка в run: %s", e)

    def _add(self, cmd: list[str] | None = None) -> None:
        """
        Добавляет новый пароль.

        Может вызываться двумя способами:
            - С аргументами: ``add <site> <username> <password>``
            - Через интерактивный ввод (input)

        :param cmd: Аргументы команды (опционально)
        :type cmd: list[str] | None
        :raises EmptyInputError: Если одно из полей пустое.
        """
        try:
            if cmd and len(cmd) == 4:
                _, site, username, password = cmd
            else:
                site = input("Введите сайт: ").strip()
                username = input("Введите логин: ").strip()
                password = input("Введите пароль: ").strip()

            self.manager.add_password(site, username, password)
            print(f"Пароль для {site} добавлен")
        except EmptyInputError as e:
            print(f"{e}")
            logger.warning("Ошибка при добавлении пароля: %s", e)

    def _list(self) -> None:
        """
        Выводит все сохранённые пароли в виде таблицы.

        Если паролей нет, выводит сообщение об отсутствии данных.
        """
        data = self.manager.list_passwords()  # словарь {site: {username, password}}

        if not data:
            print("Паролей пока нет.")
            return
        table = [
            (site, info["username"], info["password"]) for site, info in data.items()
        ]
        print(tabulate(table, headers=self.columns, tablefmt="grid"))

    def _find(self, cmd: list[str] | None = None) -> None:
        """
        Ищет пароль по названию сайта.

        Может вызываться двумя способами:
            - С аргументом: ``find <site>``
            - Через интерактивный ввод

        :param cmd: Аргументы команды (опционально)
        :type cmd: list[str] | None
        :raises PasswordNotFoundError: Если сайт не найден.
        """
        if cmd and len(cmd) == 2:
            _, site = cmd
        else:
            site = input("Введите сайт: ").strip()

        try:
            record = self.manager.find_password(site)
            table = [record]
            print(tabulate(table, headers=self.columns, tablefmt="grid"))
        except PasswordNotFoundError as e:
            print(f"{e}")
            logger.warning("Ошибка поиска пароля: %s", e)

    def _remove(self, cmd: list[str] | None = None) -> None:
        """
        Удаляет сохранённый пароль по названию сайта.

        Может вызываться двумя способами:
            - С аргументом: ``delete <site>``
            - Через интерактивный ввод

        :param cmd: Аргументы команды (опционально)
        :type cmd: list[str] | None
        :raises PasswordNotFoundError: Если сайт не найден.
        """
        if cmd and len(cmd) == 2:
            _, site = cmd
        else:
            site = input("Введите сайт: ").strip()

        try:
            self.manager.remove_password(site)
        except PasswordNotFoundError as e:
            print(f"{e}")
            logger.warning("Ошибка удаления пароля: %s", e)

    def help(self) -> None:
        """
        Выводит список доступных команд CLI.
        """
        print("\nДоступные команды:")
        for cmd, desc in self.COMMANDS.items():
            print(f"  {cmd:<6} - {desc}")
        print()
        logger.info("Выведена справка по командам")

    def exit(self) -> None:
        """
        Завершение программы
        """
        print("Программа завершена")
        logger.info("CLI-приложение завершено")
        self.running = False
