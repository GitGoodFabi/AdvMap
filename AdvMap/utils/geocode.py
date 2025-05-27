import requests

def geocode_location_nominatim(location_name):
    if not location_name:
        return None, None

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': location_name,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'AdvMapScraper/1.0 (your.email@example.com)'
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data['lat']), float(data['lon'])
    return None, None
