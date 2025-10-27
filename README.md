# CLI Password Manager

Консольное приложение для хранения и управления паролями.

---

## Описание

Приложение позволяет:

- Сохранять пароли для сайтов в `passwords.json`.
- Шифровать пароли с помощью Fernet (cryptography).
- Добавлять, удалять и искать пароли.
- Удобно работать через CLI.

---

## Функциональность

- Хранение данных в `passwords.json`.
- Шифрование паролей с помощью `cryptography.fernet`.
- Логирование действий (`logs/app.log`).
- Проверка мастер-пароля при запуске.
- Добавление, удаление, поиск и вывод всех паролей.

---

## Команды CLI

| Команда | Описание                |
|---------|-------------------------|
| `add`   | Добавить пароль         |
| `find`  | Найти пароль по сайту   |
| `delete`| Удалить пароль по сайту |
| `list`  | Вывести все пароли      |
| `help`  | Показать список команд  |
| `exit`  | Выйти из программы      |

---

## Технологии
	•	Python 3.11+
	•	pytest
    •	tabulate
	•	mypy
    •	cryptography
    •	python-dotenv

## Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/semoleg1986/cli_password_manager.git
cd cli_password_manager
```

2. Создаём и активируем виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Устанавливаем зависимости:
```bash
pip install -r requirements.txt
```

4. Устанавливаем CLI в editable режиме:
```bash
pip install -e .
```

5. Запускаем
```bash
password-manager
```

