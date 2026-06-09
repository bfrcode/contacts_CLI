from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR / "schema.sql"
DB_PATH = BASE_DIR / "database.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # accès aux colonnes par nom : row["email"]
    conn.execute("PRAGMA foreign_keys = ON") # active les foreign keys, désactivée par défaut
    return conn


def init_db() -> None:
    with get_connection() as conn:
        with open(SCHEMA_PATH, "r") as f:
            conn.executescript(f.read())