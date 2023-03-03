from django.urls import path
from . import views

urlpatterns = [
    path('', views.noysoftwebindex, name='noysof-web-index'),
]
