from django.urls import path
from . import views

urlpatterns = [
    path('mesa/<int:numero_mesa>/', views.menu_mesa, name='menu_mesa'),
    path('pedido/<int:pedido_id>/confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
    path('cocina/', views.panel_cocina, name='panel_cocina'),
    path('historial/', views.historial_pedidos, name='historial_pedidos'),
    path('pedido/<int:pedido_id>/cambiar-estado/<str:nuevo_estado>/', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
]