
from django.contrib import admin
from django.urls import path, include
from store import urls as store_urls  # Import store.urls as store_urls
from.import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(store_urls)),  # Use the imported store_urls
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
