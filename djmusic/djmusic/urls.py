from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),
    path('albums/', include('albums.urls'))
]
