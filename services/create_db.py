import sqlite3

conn = sqlite3.connect("virtual_classroom.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")