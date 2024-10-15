import sqlite3

conn = sqlite3.connect("dati.db")

def tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        Create table cilveki(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL
        )
        """
    )
    conn.commit()

tabulas_izveide()