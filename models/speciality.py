import sqlite3

from utils.string import normalize_speciality

def get_or_create_speciality(conn: sqlite3.Connection, name: str) -> int:
    """Retourne l'id d'une spécialité ou la crée si elle n'existe pas"""
    speciality_name = normalize_speciality(name)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO speciality(speciality_type) VALUES (?)", (speciality_name,))
    cursor.execute("SELECT speciality_id FROM speciality WHERE speciality_type = ?", (speciality_name,))
    result = cursor.fetchone()
    return result["speciality_id"]