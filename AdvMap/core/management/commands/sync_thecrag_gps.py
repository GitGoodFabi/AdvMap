from django.core.management.base import BaseCommand
import time
from core.models import InstagramPost
from core.thecrag_scraper import get_gps_from_thecrag

class Command(BaseCommand):
    help = "Fetches GPS data for extracted routes from theCrag and saves them in InstagramPost"

    def handle(self, *args, **options):
        posts = InstagramPost.objects.exclude(extracted_route_name__isnull=True).iterator()

        updated = 0
        skipped = 0
        failed = 0

        for post in posts:
            if post.lat is not None and post.lng is not None:
                skipped += 1
                continue

            route_name = post.extracted_route_name
            self.stdout.write(f"📌 Searching coordinates for: {route_name}...")

            try:
                lat, lng = get_gps_from_thecrag(route_name)

                if lat and lng:
                    post.lat = lat
                    post.lng = lng
                    post.save()
                    self.stdout.write(self.style.SUCCESS(f"✅ Found: {lat}, {lng}"))
                    updated += 1
                else:
                    self.stdout.write(self.style.WARNING("⚠️ No coordinates found"))
                    failed += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Error fetching coordinates: {e}"))
                failed += 1

            time.sleep(1.1)  # Add a 1.1 second delay between requests

        self.stdout.write(self.style.SUCCESS(f"✨ Done: {updated} updated, {skipped} skipped, {failed} failed."))
