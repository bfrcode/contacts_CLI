from pathlib import Path
import sqlite3

from utils import show_error

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SCHEMA_PATH = BASE_DIR / "contacts-CLI" / "database" / "schema.sql"
DB_FOLDER = BASE_DIR / "data"
DB_PATH = BASE_DIR / "data" / "database.db"

def get_connection() -> sqlite3.Connection:
    """lance la connexion à la base de donnée"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # accès aux colonnes par nom : row["email"]
    conn.execute("PRAGMA foreign_keys = ON") # active les foreign keys, désactivée par défaut
    return conn

def init_db() -> None:
    """initialise la base donnée (la crée si non existante)"""
    try:
         DB_FOLDER.mkdir()
    except FileExistsError as e:
        show_error(e)

    with get_connection() as conn:
        with open(SCHEMA_PATH, "r") as f:
            conn.executescript(f.read())