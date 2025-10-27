from core.manager import EmptyInputError, PasswordManager, PasswordNotFoundError


class App:
    """
    CLI-приложение
    """

    COMMANDS = {
        "add": "Добавить пароль",
        "find": "Найти пароль",
        "delete": "Удалить пароль",
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
                    case "find":
                        self._find()
                    case "delete":
                        self._remove()
                    case _:
                        print(f'"{command}" такой команды нет')

            except Exception as e:
                print("Неожиданная ошибка:", e)

    def _add(self) -> None:
        try:
            site = input("Введите сайт: ").strip()
            username = input("Введите логин: ").strip()
            password = input("Введите пароль: ").strip()
            self.manager.add_password(site, username, password)
        except EmptyInputError as e:
            print(f"{e}")

    def _find(self) -> None:
        site = input("Введите сайт: ").strip()
        try:
            print(self.manager.find_password(site))
        except PasswordNotFoundError as e:
            print(f"{e}")

    def _remove(self) -> None:
        site = input("Введите сайт: ").strip()
        try:
            self.manager.remove_password(site)
        except PasswordNotFoundError as e:
            print(f"{e}")

    def help(self) -> None:
        """Вывод списка команд"""
        print("\nДоступные команды:")
        for cmd, desc in self.COMMANDS.items():
            print(f"  {cmd:<6} - {desc}")
        print()

    def exit(self) -> None:
        """
        Завершение программы
        """
        print("Программа завершена")
        self.running = False
