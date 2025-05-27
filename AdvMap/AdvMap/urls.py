from django.contrib import admin
from django.urls import path
from core import views  # saubere Importstruktur

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Hauptseiten
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('map/', views.map_view, name='map'),

    # Blog
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]

# Media-Dateien im Entwicklungsmodus verfügbar machen
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
