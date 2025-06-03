from django.db import models
from core.route_marker_parser import extract_route_from_caption

# Create your models here.
class Crag(models.Model):
    name = models.CharField(max_length=180)
    location = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    image = models.ImageField(upload_to='crags/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    Instagram = models.URLField(blank=True)


    def __str__(self):
        return self.name
    
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

def preview(self):
    import markdown2
    text = self.content[:180]
    return markdown2.markdown(text)


class InstagramPost(models.Model):
    shortcode = models.CharField(max_length=100, unique=True, null=True, blank=True)
    image_url = models.URLField()
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField()
    extracted_route_name = models.CharField(max_length=200, blank=True, null=True)
    route_type = models.CharField(max_length=50, blank=True, null=True)
    # optional für spätere Geo-Integration:
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    post_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Routendaten nur setzen, wenn sie fehlen
        if not self.extracted_route_name and self.caption:
            try:
                route_name, route_type = extract_route_from_caption(self.caption)
                if route_name:
                    self.extracted_route_name = route_name
                    self.route_type = route_type
            except Exception as e:
                print(f"⚠️ Fehler beim Parsen der Caption: {e}")

        # Post-URL automatisch erzeugen (wenn Shortcode vorhanden)
        if self.shortcode and not self.post_url:
            self.post_url = f"https://www.instagram.com/p/{self.shortcode}/"

        super().save(*args, **kwargs)


class CragLocation(models.Model): # Crag Location Model
    name = models.CharField(max_length=100)
    node_id = models.IntegerField(unique=True)
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.CharField(max_length=100, blank=True)
    aliases = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class ClimbingRoute(models.Model): # Climbing Route Model
    name = models.CharField(max_length=100)
    route_type = models.CharField(max_length=20, choices=[("boulder", "Boulder" ), ("sport", "Sport"), ("multi", "Multipitch")])
    lat = models.FloatField()
    lng = models.FloatField()
    difficulty = models.CharField(max_length=20, blank=True)
    crag_name = models.CharField(max_length=100, blank=True)
    node_id = models.IntegerField(unique=True)


class InstaRoute(models.Model):
    route_name = models.TextField()
    route_type = models.TextField()
    post_url = models.URLField(unique=True)
    image_url = models.URLField()
    caption = models.TextField()
    lat = models.FloatField(null=True)  # 👈 hier neu
    lon = models.FloatField(null=True)  # 👈 hier neu
    shortcode = models.CharField(max_length=100, unique=True, null=True, blank=True)	
    
    class Meta:
        managed = False  # <- wichtig!
        db_table = 'insta_routes'  # muss exakt zur Tabelle passen
