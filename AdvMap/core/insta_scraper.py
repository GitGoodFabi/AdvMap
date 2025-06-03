import instaloader
from core.route_marker_parser import extract_route_from_caption


def extract_routes_from_instagram(profile_name="pixels.of.fabi", max_posts=100):
    L = instaloader.Instaloader()

    try:
        L.load_session_from_file(profile_name)
    except Exception as e:
        print(f"⚠️ Konnte Session nicht laden: {e}")
        return []

    posts = instaloader.Profile.from_username(L.context, profile_name).get_posts()

    route_data = []
    for i, post in enumerate(posts):
        if i >= max_posts:
            break

        caption = post.caption
        route_name, route_type = extract_route_from_caption(caption)

        if route_name and route_type:
           print(f"✅ Gefundene Route: {route_name} ({route_type})")
           route_data.append({
                "route_name": route_name,
                "route_type": route_type,
                "shortcode": post.shortcode,
                "image_url": post.url,  # statt "thumbnail"
                "caption": caption,
                "post_url": f"https://www.instagram.com/p/{post.shortcode}/"

            })

    return route_data