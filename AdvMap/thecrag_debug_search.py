# thecrag_debug_search.py
import requests

SEARCH_ENDPOINT = "https://www.thecrag.com/api/search"
NODE_ENDPOINT = "https://www.thecrag.com/api/node/{}"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}


def debug_route_search(route_name):
    print(f"🔎 Searching for route: {route_name}\n")

    params = {
        "q": route_name,
        "type": "route"
    }

    response = requests.get(SEARCH_ENDPOINT, params=params, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ Search request failed with status {response.status_code}")
        return

    data = response.json()
    matches = data.get("matches", [])

    print(f"🔁 Matches found: {len(matches)}")
    if not matches:
        print("⚠️ No matches returned.")
        return

    for match in matches:
        print("\n🧩 Raw Match:", match)
        node_id = match.get("nodeId")
        if node_id:
            node_response = requests.get(NODE_ENDPOINT.format(node_id), headers=HEADERS)
            print(f"➡️ Requesting node details for nodeId {node_id}")
            if node_response.status_code == 200:
                node = node_response.json()
                print("📍 Node info:")
                print("   Name:", node.get("name"))
                print("   Crag:", node.get("areaName"))
                print("   Grade:", node.get("grade"))
                print("   Lat/Lng:", node.get("latitude"), node.get("longitude"))
            else:
                print(f"❌ Failed to get node info: {node_response.status_code}")

if __name__ == "__main__":
    route_query = input("🔍 Enter route name to search: ")
    debug_route_search(route_query)
