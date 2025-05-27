import re

# Parse climbing route and type from Instagram caption
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



#for caption in test_captions:
    route, typ = extract_route_from_caption(caption)
    print(f"📌 Caption: {caption}\n🔍 Route: {route} | Type: {typ}\n")
# This function will extract the route name and type from the caption.
# It uses regex to find patterns like #boulder:RouteName, #sport:RouteName, and #multi:RouteName.
# The extracted route name and type are returned as a tuple.
# If no match is found, it returns (None, None).
# This is a simple example and can be expanded based on the specific needs of the application.
# The regex patterns can be adjusted to match different formats or additional types of routes.
# The function can also be integrated into a larger application where Instagram captions are processed.
# The extracted route names and types can be stored in a database or used for further processing.
