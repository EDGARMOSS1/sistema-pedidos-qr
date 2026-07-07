from django.urls import path
from . import views

urlpatterns = [
    path('mesa/<int:numero_mesa>/', views.menu_mesa, name='menu_mesa'),
    path('pedido/<int:pedido_id>/confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
]