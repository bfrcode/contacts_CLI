import sqlite3

from database.db import get_connection
from models.company import add_company

conn = get_connection()
test = ("MA SOCIETE", "Adresse test", "0442809070", "mail@test.fr","Gros Oeuvre","Test Cédric")

add_company(conn, test)

cursor = conn.cursor()
cursor.execute("SELECT * FROM company")
print(cursor.fetchall())