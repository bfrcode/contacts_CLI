import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")

    with open("schema.sql", "r") as f:

        sql_script = f.read()

        conn.executescript(sql_script)
        conn.commit()

        conn.close()
