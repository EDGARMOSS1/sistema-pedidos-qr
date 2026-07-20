from django.urls import path
from . import views

urlpatterns = [
    path('metricas/', views.dashboard_metricas, name='dashboard_metricas'),
    path('metricas/exportar-csv/', views.exportar_metricas_csv, name='exportar_metricas_csv'),
    path('metricas/analisis/', views.analisis_resultados, name='analisis_resultados'),
]