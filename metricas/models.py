from django.db import models
from mesas.models import Mesa
from pedidos.models import Pedido


class RegistroEvento(models.Model):

    class TipoEvento(models.TextChoices):
        PEDIDO_CREADO = 'pedido_creado', 'Pedido creado'
        CAMBIO_ESTADO = 'cambio_estado', 'Cambio de estado'
        PEDIDO_ENTREGADO = 'pedido_entregado', 'Pedido entregado'

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='eventos',
        null=True,
        blank=True
    )
    mesa = models.ForeignKey(
        Mesa,
        on_delete=models.CASCADE,
        related_name='eventos'
    )
    tipo_evento = models.CharField(
        max_length=30,
        choices=TipoEvento.choices
    )
    descripcion = models.TextField(blank=True)
    fecha_evento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_evento} - Mesa {self.mesa.numero}"


class LogPedido(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='logs_metricas'
    )
    tiempo_captura_ms = models.PositiveIntegerField()
    tiempo_procesamiento_ms = models.PositiveIntegerField()

    class Meta:
        db_table = 'log_pedidos'
        ordering = ['-timestamp']

    def __str__(self):
        return f"Log pedido #{self.pedido.id}"