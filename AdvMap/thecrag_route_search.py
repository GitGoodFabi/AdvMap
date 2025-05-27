# thecrag_route_search.py
import requests
from core.route_marker_parser import extract_route_from_caption

SEARCH_ENDPOINT = "https://www.thecrag.com/api/search"
NODE_ENDPOINT = "https://www.thecrag.com/api/node/{}"

# Search theCrag API for a climbing route, then fetch detailed info
def search_thecrag_route(route_name):
    params = {
        "q": route_name,
        "type": "route"
    }
    headers = {
        'User-Agent': 'AdvMapBot/1.0 (your.email@example.com)'
    }
    
    # Step 1: Search for the route name
    response = requests.get(SEARCH_ENDPOINT, params=params, headers=headers)
    if response.status_code != 200 or not response.json():
        return None

    matches = response.json().get("matches", [])
    if not matches:
        return None

    # Step 2: Get full node details using nodeId
    node_id = matches[0].get("nodeId")
    if not node_id:
        return None

    node_response = requests.get(NODE_ENDPOINT.format(node_id), headers=headers)
    if node_response.status_code != 200 or not node_response.json():
        return None

    node = node_response.json()

    return {
        "name": node.get("name"),
        "node_id": node_id,
        "latitude": node.get("latitude"),
        "longitude": node.get("longitude"),
        "grade": node.get("grade"),
        "crag": node.get("areaName")
    }

# Example test
test_captions = [
    "#boulder:Helicopter",
    "#multi:Cerberus",
    "#sport:Supernova"
]

for caption in test_captions:
    route_name, route_type = extract_route_from_caption(caption)
    if route_name:
        print(f"🔍 Looking up: {route_name} ({route_type})")
        result = search_thecrag_route(route_name)
        if result:
            print("✅ Found:", result)
        else:
            print("❌ Not found.")
    else:
        print("⚠️ No route marker found in caption.")
    print()
