import requests
import re
from bs4 import BeautifulSoup

def get_gps_from_thecrag(route_name):
    search_url = f"https://www.thecrag.com/en/search?query={route_name}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None, None

    if response.status_code != 200:
        print(f"❌ Failed to fetch search results for: {route_name}")
        return None, None

    soup = BeautifulSoup(response.text, 'html.parser')
    result_link = soup.select_one('div.node-info a[href*="/climbing/"]')

    if not result_link:
        print(f"⚠️ No route link found for: {route_name}")
        return None, None

    route_url = "https://www.thecrag.com" + result_link['href']
    route_page = requests.get(route_url, headers=headers)
    if route_page.status_code != 200:
        print(f"❌ Failed to fetch route page: {route_url}")
        return None, None

    match = re.search(r'"lat":([0-9\.\-]+),"lng":([0-9\.\-]+)', route_page.text)
    if match:
        lat = float(match.group(1))
        lng = float(match.group(2))
        return lat, lng

    print(f"⚠️ No coordinates found on route page: {route_url}")
    return None, None
