# import_crags.py
import requests
import django
import os
import sys

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvMap.settings")
django.setup()

from core.models import CragLocation

# TheCrag search endpoint
SEARCH_ENDPOINT = "https://www.thecrag.com/api/topo-area-search"

# Keywords to search for
keywords = ["fontainebleau", "hampi", "magic wood", "siurana", "kalymnos", "albarracin"]

for keyword in keywords:
    print(f"🔍 Searching for: {keyword}")
    response = requests.get(SEARCH_ENDPOINT, params={"q": keyword})

    if response.status_code != 200:
        print(f"❌ Error searching '{keyword}': {response.status_code}")
        continue

    results = response.json()

    for item in results:
        node_id = item.get("nodeId")
        name = item.get("name")
        lat = item.get("latitude")
        lng = item.get("longitude")
        country = item.get("country")

        if not (node_id and lat and lng):
            continue  # Skip incomplete data

        crag, created = CragLocation.objects.get_or_create(
            node_id=node_id,
            defaults={
                "name": name,
                "lat": lat,
                "lng": lng,
                "country": country or "",
                "aliases": keyword.lower(),
            }
        )

        if created:
            print(f"✅ Added: {name} ({country}) → {lat}, {lng}")
        else:
            print(f"↺ Skipped (already exists): {name}")
