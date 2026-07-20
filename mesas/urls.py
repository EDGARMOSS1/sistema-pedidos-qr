from django.urls import path
from . import views

urlpatterns = [
    path('mesas/', views.mapa_mesas, name='mapa_mesas'),
    path('mesas/<int:mesa_id>/generar-qr/', views.generar_qr_mesa, name='generar_qr_mesa'),
    path('mesas/generar-todos-qr/', views.generar_todos_qr, name='generar_todos_qr'),
    path('mesas/qrs/imprimir/', views.imprimir_qrs, name='imprimir_qrs'),
]