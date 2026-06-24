import sqlite3

conn = sqlite3.connect("study_planner.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    status TEXT
)
""")

conn.commit()

print("Table Created")

conn.close()