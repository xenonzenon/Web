from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('noysoftapp/', include('noysoftapp.urls')),
    path('noysoftweb/', include('noysoftweb.urls')),
    path('noysoftgame/', include('noysoftgame.urls')),
]
