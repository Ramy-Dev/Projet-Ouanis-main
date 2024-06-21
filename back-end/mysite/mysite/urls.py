from django.conf import settings
from django.conf.urls.static import static
from ouanis.admin import admin_site
from django.urls import include, path
urlpatterns = [
    path("", include("ouanis.urls")),
     path('admin/', admin_site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)