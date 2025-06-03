import sqlite3

conn = sqlite3.connect("insta_routes.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM insta_routes")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()