from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import re
import time
import csv
from datetime import date
from core.insta_scraper import extract_routes_from_instagram


def get_coordinates_selenium(route_name):
    search_term = route_name.replace(" ", "+")
    search_url = f"https://www.thecrag.com/en/search?S={search_term}"

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")

    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print(f"🔍 Öffne Suchseite: {search_url}")
        driver.get(search_url)
        time.sleep(2)

        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/route/']"))
        )

        print(f"🔗 Gefundene Routen-Links auf der Suchseite:")
        for i, link in enumerate(links):
            print(f"  {i + 1}. {link.get_attribute('href')}")

        if not links:
            print(f"⚠️ Keine Routen-Links gefunden für {route_name}")
            return None

        route_url = links[0].get_attribute("href")
        if not route_url.startswith("http"):
            route_url = f"https://www.thecrag.com{route_url}"

        print(f"➡️ Folge dem ersten Routentreffer: {route_url}")
        driver.get(route_url)
        time.sleep(4)

        try:
            location_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Lat/Lon')]"))
            )
            location_text = location_element.text
            print(f"🔎 Gefundener Text: {location_text}")
            match = re.search(r'Lat/Lon:\s*([0-9\.-]+),\s*([0-9\.-]+)', location_text)
            if match:
                lat, lon = match.groups()
                print(f"✅ Gefunden: {lat}, {lon}")
                return float(lat), float(lon)
        except Exception as e:
            print(f"⚠️ Kein Lat/Lon gefunden: {e}")

        print(f"⚠️ Keine Koordinaten auf der Seite gefunden")
        return None

    except Exception as e:
        print(f"❌ Fehler: {e}")
        return None

    finally:
        driver.quit()


if __name__ == "__main__":
    today = date.today().isoformat()
    output_file = f"thecrag_coordinates_{today}.csv"
    csv_headers = ["Route Name", "Latitude", "Longitude", "Type"]

    instagram_routes = extract_routes_from_instagram()
    routes = [(r[0], r[1]) for r in instagram_routes if r[0] is not None]

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

        for route, typ in routes:
            print(f"\n📌 Suche Koordinaten für: {route} ({typ})")
            result = get_coordinates_selenium(route)
            if result:
                lat, lon = result
                writer.writerow([route, lat, lon, typ])
