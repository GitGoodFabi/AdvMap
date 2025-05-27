import os
import sys
import django
import instaloader
from datetime import datetime

from thecrag_route_search import search_thecrag_route

# Django setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvMap.settings")
django.setup()

from core.models import InstagramPost
from utils.geocode import geocode_location_nominatim
from core.route_marker_parser import extract_route_from_caption
#from thecrag_route_search import search_thecrag_route

L = instaloader.Instaloader()
L.load_session_from_file('pixels.of.fabi')

profile = instaloader.Profile.from_username(L.context, 'pixels.of.fabi')

for post in profile.get_posts():
    post_url = f"https://www.instagram.com/p/{post.shortcode}/"
    if InstagramPost.objects.filter(post_url=post_url).exists():
        continue

    caption = post.caption or ""
    image_url = post.url
    created_at = post.date

    lat, lng = None, None
    location_name = ""

    # Priority 1: Try to extract route from caption and resolve via theCrag
    route_name, route_type = extract_route_from_caption(caption)
    print(f"📍 Extracted route: {route_name} ({route_type})")       #test

    if route_name:
        route_data = search_thecrag_route(route_name)
if route_data:
    lat = route_data.get("latitude")
    lng = route_data.get("longitude")
    location_name = route_data.get("crag") or location_name
    print(f"🔍 Searching theCrag for: {route_name}")                    #testi
    print(f"🔁 Route data returned: {route_data}")              #test      

    # Priority 2: Try Instagram location if coordinates still missing
    if not lat or not lng:
        try:
            raw_location = post._node.get('location')
            if raw_location:
                location_name = (
                    raw_location.get('name') or
                    raw_location.get('title') or
                    raw_location.get('slug', '').replace('-', ' ')
                )
        except Exception:
            pass

    # Priority 3: Fallback to known crag names in caption
    if not lat or not lng:
        for place in ['Hampi', 'Fontainebleau', 'Magic Wood', 'Siurana', 'Kalymnos']:
            if place.lower() in caption.lower():
                location_name = place
                break

    # Priority 4: Try to geocode location name
    if (not lat or not lng) and location_name:
        lat, lng = geocode_location_nominatim(location_name)

    InstagramPost.objects.create(
        caption=caption,
        image_url=image_url,
        post_url=post_url,
        location_name=location_name,
        lat=lat,
        lng=lng,
        created_at=created_at
    )

    print(f"✅ Imported: {caption[:40]} | {location_name} → {lat}, {lng}")
