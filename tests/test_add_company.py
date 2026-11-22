import sqlite3

from database.db import get_connection
from models.company import add_company

conn = get_connection()
name = "MA SOCIETE"
address = "Adresse test"
phone = "0442809070"
mail = "mail@test.fr"
speciality = "Gros Oeuvre"
note = "Test Cédric"

add_company(conn, name, address, phone, mail, speciality, note)

cursor = conn.cursor()
rows = cursor.execute("SELECT * FROM company")
for row in rows:
    print(dict(row))