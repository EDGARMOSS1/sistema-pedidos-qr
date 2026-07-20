from django.urls import path
from . import views

urlpatterns = [
    path('mesas/', views.mapa_mesas, name='mapa_mesas'),
    path('mesas/<int:mesa_id>/generar-qr/', views.generar_qr_mesa, name='generar_qr_mesa'),
]