from django.contrib import admin
from .models import RegistroEvento


@admin.register(RegistroEvento)
class RegistroEventoAdmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'mesa', 'pedido', 'fecha_evento')
    list_filter = ('tipo_evento', 'fecha_evento')