from django.contrib import admin
from .models import RegistroEvento, LogPedido


@admin.register(RegistroEvento)
class RegistroEventoAdmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'mesa', 'pedido', 'fecha_evento')
    list_filter = ('tipo_evento', 'fecha_evento')


@admin.register(LogPedido)
class LogPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'timestamp',
        'pedido',
        'tiempo_captura_ms',
        'tiempo_procesamiento_ms'
    )
    list_filter = ('timestamp',)
    search_fields = ('pedido__id', 'pedido__nombre_cliente')