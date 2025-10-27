from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

PASSWORDS_FILE = DATA_DIR / "passwords.json"
LOG_FILE = LOGS_DIR / "app.log"
KEY_FILE = DATA_DIR / "key.key"
MASTER_KEY = DATA_DIR / "master.key"
