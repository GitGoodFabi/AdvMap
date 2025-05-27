from django.contrib import admin
from django.utils.html import format_html
from core.models import InstagramPost, Crag, Post, ClimbingRoute, CragLocation

@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "extracted_route_name",
        "route_type",
        "shortcode",
        "preview_link",
        "caption_preview",
    )
    list_filter = ("route_type", "created_at")
    search_fields = ("caption", "extracted_route_name", "shortcode")

    readonly_fields = ("preview_image", "post_url", "shortcode", "image_url")

    def caption_preview(self, obj):
        return obj.caption[:40] + "..." if obj.caption else "-"
    caption_preview.short_description = "Caption"

    def preview_link(self, obj):
        if obj.post_url:
            return format_html('<a href="{}" target="_blank">🔗 Instagram</a>', obj.post_url)
        return "-"
    preview_link.short_description = "Post"

    def preview_image(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="300" />', obj.image_url)
        return "No image"
    preview_image.short_description = "Image Preview"

# Optional: Admin-Anzeige für andere Modelle
admin.site.register(Crag)
admin.site.register(Post)

