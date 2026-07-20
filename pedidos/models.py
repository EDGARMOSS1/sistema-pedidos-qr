from decimal import Decimal
from django.db import models
from django.utils import timezone
from mesas.models import Mesa
from menu.models import Producto


class Pedido(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        PREPARACION = 'preparacion', 'En preparación'
        LISTO = 'listo', 'Listo'
        ENTREGADO = 'entregado', 'Entregado'

    mesa = models.ForeignKey(
        Mesa,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    nombre_cliente = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inicio_registro = models.DateTimeField(null=True, blank=True)
    fin_registro = models.DateTimeField(null=True, blank=True)
    tiempo_registro_segundos = models.PositiveIntegerField(default=0)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_preparacion = models.DateTimeField(null=True, blank=True)
    fecha_listo = models.DateTimeField(null=True, blank=True)
    fecha_entregado = models.DateTimeField(null=True, blank=True)

    def calcular_total(self):
        total = Decimal('0.00')
        for detalle in self.detalles.all():
            total += detalle.subtotal()
        self.total = total
        self.save()
        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

        if nuevo_estado == self.Estado.PREPARACION:
            self.fecha_preparacion = timezone.now()

        elif nuevo_estado == self.Estado.LISTO:
            self.fecha_listo = timezone.now()

        elif nuevo_estado == self.Estado.ENTREGADO:
            self.fecha_entregado = timezone.now()

        self.save()

    def tiempo_total_minutos(self):
        if self.fecha_entregado:
            diferencia = self.fecha_entregado - self.fecha_creacion
            return round(diferencia.total_seconds() / 60, 2)
        return None

    def tiempo_registro_texto(self):
        if self.tiempo_registro_segundos:
            minutos = self.tiempo_registro_segundos // 60
            segundos = self.tiempo_registro_segundos % 60
            return f"{minutos} min {segundos} seg"
        return "Sin registro"

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa.numero}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def save(self, *args, **kwargs):
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"