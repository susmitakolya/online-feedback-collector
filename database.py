import sqlite3

conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rating INTEGER,
    comment TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
