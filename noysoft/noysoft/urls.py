from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.png', RedirectView.as_view(url=staticfiles_storage.url('favicons/noysoft-16x16.png'))),
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('noysoftapp/', include('noysoftapp.urls')),
    path('noysoftweb/', include('noysoftweb.urls')),
    path('noysoftgame/', include('noysoftgame.urls')),
]
