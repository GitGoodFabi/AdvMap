import sqlite3
from core.insta_scraper import extract_routes_from_instagram
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "insta_routes.db")

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS insta_routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            route_name TEXT,
            route_type TEXT,
            post_url TEXT,
            image_url TEXT,
            caption TEXT
        )
    ''')

    # Index auf route_name (unique)
    cursor.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_route_name
        ON insta_routes(route_name)
    ''')

    conn.commit()
    conn.close()

def insert_routes(routes):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    for route in routes:
        route_name = route["route_name"]

        # Prüfen, ob diese Route bereits existiert
        cursor.execute("SELECT 1 FROM insta_routes WHERE route_name = ?", (route_name,))
        exists = cursor.fetchone()

        if exists:
            print(f"⚠️ Übersprungen (bereits vorhanden): {route_name}")
            continue

        try:
            cursor.execute('''
                INSERT INTO insta_routes 
                (route_name, route_type, post_url, image_url, caption)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                route_name,
                route["route_type"],
                route["post_url"],
                route["image_url"],
                route["caption"]
            ))
            print(f"✅ Eingefügt: {route_name}")
        except Exception as e:
            print(f"❌ Fehler beim Einfügen von {route_name}: {e}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("🔍 Starte Instagram-Scraper...")
    routes = extract_routes_from_instagram()

    filtered = [
        r for r in routes
        if r.get("route_name") is not None and r.get("route_type") is not None
    ]

    print(f"📥 {len(filtered)} gültige Routen werden in die Datenbank geschrieben.")
    create_table()
    insert_routes(filtered)
    print("✅ Datenbank erfolgreich aktualisiert.")
