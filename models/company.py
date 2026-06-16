import sqlite3

from dataclasses import dataclass

from .speciality import get_or_create_speciality

@dataclass
class Company:
    company_id: int
    company_name: str
    company_address: str
    company_phone: str
    company_mail: str
    company_speciality: str
    company_note: str

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Company":
        return cls(
            company_id=row["company_id"],
            company_name=row["company_name"],
            company_address=row["company_address"],
            company_phone=row["company_phone"],
            company_mail=row["company_mail"],
            company_speciality=row["fk_speciality"],
            company_note=row["company_note"],
        )

def add_company(conn: sqlite3.Connection, name: str, address: str, phone: str, mail: str, speciality: str, note: str) -> None:
    """Ajoute une société dans la base de donnée"""
    with conn:
        cursor = conn.cursor()
        speciality_id = get_or_create_speciality(conn, speciality)
        cursor.execute("INSERT OR IGNORE INTO company (company_name, company_address, company_phone, company_mail, fk_speciality, company_note) VALUES (?, ?, ?, ?, ?, ?)", (name, address, phone, mail, speciality_id, note))