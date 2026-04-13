import sqlite3

conn = def get_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return sqlite3.connect(os.path.join(BASE_DIR, "database.db"))


conn.execute("""
CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT,
role TEXT,
branch TEXT,
year TEXT,
semester TEXT,
roll TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
