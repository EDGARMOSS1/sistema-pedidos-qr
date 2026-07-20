from django.urls import path
from . import views

urlpatterns = [
    path('metricas/', views.dashboard_metricas, name='dashboard_metricas'),
]