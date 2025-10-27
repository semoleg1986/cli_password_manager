from core.manager import EmptyInputError, PasswordManager, PasswordNotFoundError
from utils.logger import get_logger

logger = get_logger(__name__)


class App:
    """
    CLI-приложение
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
        self.running = True
        self.manager = PasswordManager()

    def run(self) -> None:
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
                        self._add()
                    case "list":
                        self._list()
                    case "find":
                        self._find()
                    case "delete":
                        self._remove()
                    case _:
                        print(f'"{command}" такой команды нет')
                        logger.warning("Неизвестная команда: %s", command)

            except Exception as e:
                print("Неожиданная ошибка:", e)
                logger.exception("Неожиданная ошибка в run: %s", e)

    def _add(self) -> None:
        try:
            site = input("Введите сайт: ").strip()
            username = input("Введите логин: ").strip()
            password = input("Введите пароль: ").strip()
            self.manager.add_password(site, username, password)
        except EmptyInputError as e:
            print(f"{e}")
            logger.warning("Ошибка при добавлении пароля: %s", e)

    def _list(self) -> None:
        print(self.manager.list_passwords())

    def _find(self) -> None:
        site = input("Введите сайт: ").strip()
        try:
            print(self.manager.find_password(site))
        except PasswordNotFoundError as e:
            print(f"{e}")
            logger.warning("Ошибка поиска пароля: %s", e)

    def _remove(self) -> None:
        site = input("Введите сайт: ").strip()
        try:
            self.manager.remove_password(site)
        except PasswordNotFoundError as e:
            print(f"{e}")
            logger.warning("Ошибка удаления пароля: %s", e)

    def help(self) -> None:
        """Вывод списка команд"""
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
