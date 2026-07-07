from django.urls import path
from . import views

urlpatterns = [
    path('mesas/', views.mapa_mesas, name='mapa_mesas'),
]