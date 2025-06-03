import requests
from bs4 import BeautifulSoup
import re
import time
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Fetch coordinates for climbing routes from theCrag"

    def handle(self, *args, **kwargs):
        routes = [
            "Cosmic Crimp",
            "Il Richiamo del Mare",
            "Geierwandführe",
            "White Russian"
        ]

        for route in routes:
            self.stdout.write(f"\n📌 Searching coordinates for: {route}")
            coords = self.get_coordinates(route)
            if coords:
                lat, lon = coords
                self.stdout.write(f"✅ Found: {lat}, {lon}")
            else:
                self.stdout.write(f"⚠️ No coordinates found for: {route}")

    def get_coordinates(self, route_name):
        search_term = route_name.replace(" ", "+")
        search_url = f"https://www.thecrag.com/search?S={search_term}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(search_url, headers=headers)
            print(f"📡 Status code: {response.status_code}")
            if response.status_code != 200:
                print(f"❌ Fehler bei Suche für {route_name}")
                return None

            soup = BeautifulSoup(response.text, "lxml")

            # Suche nach Links, die auf eine Route oder einen Sektor deuten
            route_links = [
                link for link in soup.find_all("a", href=True)
                if re.search(r"/climbing/|/route/", link["href"])
            ]

            if not route_links:
                print(f"⚠️ Keine passenden Routelinks für {route_name}")
                return None

            route_url = "https://www.thecrag.com" + route_links[0]["href"]
            print(f"🔗 Folge Link: {route_url}")

            time.sleep(1)  # Respectful delay
            route_response = requests.get(route_url, headers=headers)

            # Koordinaten aus JavaScript-Daten extrahieren
            match = re.search(r'"lat":([0-9\.-]+),"lon":([0-9\.-]+)', route_response.text)
            if match:
                lat, lon = match.groups()
                return float(lat), float(lon)

            print(f"⚠️ Keine Koordinaten gefunden auf {route_url}")
            return None

        except Exception as e:
            print(f"❌ Exception: {e}")
            return None
