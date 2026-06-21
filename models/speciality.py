import sqlite3

from dataclasses import dataclass

from utils.string import normalize_speciality

@dataclass
class Speciality:
    id: int | None
    name: str | None

    @classmethod
    def from_row (cls, row: sqlite3.Row) -> "Speciality":
        return cls(
            id=row["speciality_id"],
            name=row["speciality_type"],
        )
def get_or_create_speciality(conn: sqlite3.Connection, speciality: Speciality) -> Speciality:
    """Retourne l'id d'une spécialité ou la crée si elle n'existe pas"""
    speciality_name = normalize_speciality(speciality.name)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO speciality(speciality_type) VALUES (?)", (speciality_name,))
    cursor.execute("SELECT speciality_id FROM speciality WHERE speciality_type = ?", (speciality_name,))
    result = cursor.fetchone()
    speciality.id = result["speciality_id"]
    return speciality