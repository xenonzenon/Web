from django.urls import path
from . import views

urlpatterns = [
    path('', views.noysoftgameindex, name='noysoft-game-index')
]
