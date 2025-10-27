from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

PASSWORDS_FILE = DATA_DIR / "passwords.json"
LOG_FILE = LOGS_DIR / "app.log"
