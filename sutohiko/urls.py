from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', startup),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('robots.txt', robots),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

