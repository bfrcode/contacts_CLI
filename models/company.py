import sqlite3

from dataclasses import dataclass

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
            company_speciality=row["company_speciality"],
            company_note=row["company_note"],
        )

def add_company(conn: sqlite3.Connection, values: tuple[str | int, ...]) -> None:
    """Ajoute une société dans la base de donnée"""
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO company (company_name, company_address, company_phone, company_mail, company_speciality, company_note) VALUES (?, ?, ?, ?, ?, ?)", values)