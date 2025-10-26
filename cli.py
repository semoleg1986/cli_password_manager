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
                    case _:
                        print(f'"{command}" такой команды нет')

            except Exception as e:
                print("Неожиданная ошибка:", e)

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
