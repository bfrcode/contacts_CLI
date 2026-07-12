import sqlite3

from dataclasses import dataclass, fields

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
        """Construit une instance Company à partir d'un objet sqlite3.Row"""
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
    if not company.name:
        raise ValueError("Le nom de la société ne peut pas être vide")
    
    with conn:
        speciality = Speciality(id=None, name=speciality_name)
        speciality = get_or_create_speciality(conn, speciality)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO company (company_name, company_address, company_phone, company_mail, fk_speciality, company_note) VALUES (?, ?, ?, ?, ?, ?)", (company.name, company.address, company.phone, company.mail, speciality.id, company.note))
        if cursor.rowcount == 0:
            raise ValueError(f"Une société nommée '{company.name}' existe déjà")
        company.id = cursor.lastrowid
        return company
    
def show_company(conn: sqlite3.Connection, name: str) -> Company:
    """Affiche une société en particulier"""
    if not name:
        raise ValueError("Le nom de la société ne peut pas être vide")
    
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT company WHERE name = ?", (name,))
        result = cursor.fetchone()
        company = Company.from_row(result)
        return company




