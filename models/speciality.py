import sqlite3

from dataclasses import dataclass

from utils.string import normalize_speciality

@dataclass
class Speciality:
    speciality_id: int
    speciality_name: str

    @classmethod
    def from_row (cls, row: sqlite3.Row) -> "Speciality":
        return cls(
            speciality_id=row["speciality_id"],
            speciality_name=row["speciality_type"],
        )
def get_or_create_speciality(conn: sqlite3.Connection, name: str) -> int:
    """Retourne l'id d'une spécialité ou la crée si elle n'existe pas"""
    speciality_name = normalize_speciality(name)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO speciality(speciality_type) VALUES (?)", (speciality_name,))
    cursor.execute("SELECT speciality_id FROM speciality WHERE speciality_type = ?", (speciality_name,))
    result = cursor.fetchone()
    return result["speciality_id"]