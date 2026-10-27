from pathlib import Path

APP_NAME = "SecureVault"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "passwords.db"
BACKUP_DIR = DATA_DIR / "backups"
KDF_ITERATIONS = 3
KDF_MEMORY_KIB = 65536
KDF_PARALLELISM = 2
CLIPBOARD_CLEAR_SECONDS = 30
