
from thecrag_selenium import get_coordinates_selenium
import sqlite3
import time

DB_PATH = "insta_routes.db"

def update_coordinates():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, route_name FROM insta_routes WHERE lat IS NULL OR lon IS NULL")
    rows = cursor.fetchall()

    for row in rows:
        route_id, route_name = row
        print(f"📌 Suche Koordinaten für: {route_name}")
        coords = get_coordinates_selenium(route_name)

        if coords:
            lat, lon = coords
            try:
                cursor.execute(
                    "UPDATE insta_routes SET lat = ?, lon = ? WHERE id = ?",
                    (lat, lon, route_id)
                )
                conn.commit()
                print(f"✅ Aktualisiert: {route_name} → {lat}, {lon}")
            except Exception as e:
                print(f"❌ Fehler beim Speichern für {route_name}: {e}")
        else:
            print(f"⚠️ Keine Koordinaten für {route_name}")

        time.sleep(1.5)  # vermeidet Blockierung

    conn.close()

if __name__ == "__main__":
    update_coordinates()
