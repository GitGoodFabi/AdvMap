import re

def extract_route_from_caption(caption):
    if not caption:
        return None, None

    patterns = {
        'boulder': r'#boulder:\s*([^\n#]+)',
        'sport': r'#sport:\s*([^\n#]+)',
        'multi': r'#multi:\s*([^\n#]+)',
    }

    for route_type, pattern in patterns.items():
        match = re.search(pattern, caption, re.IGNORECASE)
        if match:
            route_name = match.group(1).strip()
            return route_name, route_type

    return None, None


# 🔍 TESTBLOCK – kann später wieder gelöscht werden
if __name__ == "__main__":
    test_captions = [
        "#boulder: Cosmic Crimp",
        "#sport: Geierwandführe",
        "#multi: Il Richiamo del Mare",
        "Just climbed something awesome! #boulder:White Russian",
        "Kein Hashtag hier.",
        "#multi : Mit Leerzeichen",
    ]

    for caption in test_captions:
        route, typ = extract_route_from_caption(caption)
        print(f"📌 Caption: {caption}\n➡️ Route: {route} | Type: {typ}\n")