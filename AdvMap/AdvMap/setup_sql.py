import sqlite3

conn = sqlite3.connect("insta_routes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS insta_routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_name TEXT,
    route_type TEXT,
    shortcode TEXT,
    post_url TEXT,
    image_url TEXT,
    caption TEXT,
    lat REAL,
    lon REAL
)
""")

conn.commit()
conn.close()

print("✅ Tabelle erstellt")
