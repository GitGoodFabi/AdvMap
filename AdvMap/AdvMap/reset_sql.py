import sqlite3

conn = sqlite3.connect("insta_routes.db")
cursor = conn.cursor()

# Alte Tabelle löschen, falls vorhanden
cursor.execute("DROP TABLE IF EXISTS insta_routes")

# Neue Tabelle mit allen Feldern anlegen
cursor.execute("""
    CREATE TABLE insta_routes (
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

print("✅ Tabelle insta_routes erfolgreich neu erstellt.")
