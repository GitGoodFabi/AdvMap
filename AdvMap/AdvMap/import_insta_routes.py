import sqlite3
import os
import django

# Django-Setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvMap.settings")
django.setup()

from core.models import InstaRoute

# Pfad zur externen SQLite-Datenbank
DB_PATH = "insta_routes.db"

def import_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT route_name, route_type, shortcode, image_url, caption, lat, lon FROM insta_routes")
    rows = cursor.fetchall()

    count = 0
    for row in rows:
        route_name, route_type, shortcode, image_url, caption, lat, lon = row

        # Duplikate verhindern (z. B. durch shortcode)
        if not InstaRoute.objects.filter(shortcode=shortcode).exists():
            InstaRoute.objects.create(
                route_name=route_name,
                route_type=route_type,
                shortcode=shortcode,
                post_url=f"https://www.instagram.com/p/{shortcode}/",
                image_url=image_url,
                caption=caption,
                lat=lat,
                lon=lon
            )
            count += 1

    print(f"✅ {count} Routen importiert.")
    conn.close()
