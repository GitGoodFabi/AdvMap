from django.core.management.base import BaseCommand
from instaloader import Instaloader, Profile
from core.models import InstagramPost
from core.route_marker_parser import extract_route_from_caption


class Command(BaseCommand):
    help = 'Synchronisiere Instagram-Posts und extrahiere Routennamen'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Instagram-Username')

    def handle(self, *args, **options):
        username = options['username'] or 'dein_instagram_username'
        L = Instaloader()

        try:
            L.load_session_from_file(username)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'⚠️  Session konnte nicht geladen werden: {e}'))
            return

        profile = Profile.from_username(L.context, username)
        added = 0

        for post in profile.get_posts():
            shortcode = post.shortcode
            if InstagramPost.objects.filter(shortcode=shortcode).exists():
                continue

            caption = post.caption or ""
            route_name, route_type = extract_route_from_caption(caption)

            if route_name:
                InstagramPost.objects.create(
                    shortcode=shortcode,
                    image_url=post.url,
                    caption=caption,
                    created_at=post.date_utc,
                    extracted_route_name=route_name,
                    route_type=route_type
                )
                self.stdout.write(f"✅ Neue Route: {route_name} ({route_type})")
                added += 1

        self.stdout.write(self.style.SUCCESS(f"Fertig. {added} neue Einträge hinzugefügt."))
