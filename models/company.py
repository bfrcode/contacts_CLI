import sqlite3

from dataclasses import dataclass

from .speciality import Speciality
from .speciality import get_or_create_speciality

@dataclass
class Company:
    id: int | None
    name: str | None
    address: str | None
    phone: str | None
    mail: str | None
    speciality: str | None
    note: str | None

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Company":
        return cls(
            id=row["company_id"],
            name=row["company_name"],
            address=row["company_address"],
            phone=row["company_phone"],
            mail=row["company_mail"],
            speciality=row["fk_speciality"],
            note=row["company_note"],
        )

def add_company(conn: sqlite3.Connection, company: Company, speciality_name: str) -> Company:
    """Ajoute une société dans la base de donnée"""
    with conn:
        cursor = conn.cursor()
        speciality = Speciality(id=None, name=speciality_name)
        speciality = get_or_create_speciality(conn, speciality)
        cursor.execute("INSERT OR IGNORE INTO company (company_name, company_address, company_phone, company_mail, fk_speciality, company_note) VALUES (?, ?, ?, ?, ?, ?)", (company.name, company.address, company.phone, company.mail, speciality.id, company.note))
        return company