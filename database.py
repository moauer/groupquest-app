import sqlite3

conn = sqlite3.connect("data/groupquest.db")
cursor = conn.cursor()

# USER TABELLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# CHALLENGE TABELLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
""")

conn.commit()
conn.close()

print("Datenbank erstellt!")

