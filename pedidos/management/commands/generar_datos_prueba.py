import random
from decimal import Decimal
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from mesas.models import Mesa
from menu.models import Producto
from pedidos.models import Pedido, DetallePedido
from metricas.models import RegistroEvento


class Command(BaseCommand):
    help = 'Genera pedidos de prueba para métricas del sistema'

    def handle(self, *args, **options):
        mesas = list(Mesa.objects.filter(activa=True))
        productos = list(Producto.objects.filter(disponible=True))

        if not mesas:
            self.stdout.write(self.style.ERROR('No hay mesas registradas.'))
            return

        if not productos:
            self.stdout.write(self.style.ERROR('No hay productos registrados.'))
            return

        nombres = [
            'Edgar', 'Alan', 'Karol', 'Omar', 'Luis',
            'Andrea', 'Mariana', 'Carlos', 'Sofia', 'Diego',
            'Fernanda', 'Miguel', 'Valeria', 'Jorge', 'Diana',
            'Pedro', 'Paola', 'Ricardo', 'Daniela', 'Hugo'
        ]

        for i in range(20):
            mesa = random.choice(mesas)
            nombre_cliente = nombres[i % len(nombres)]

            minutos_atencion = random.randint(8, 28)
            segundos_registro = random.randint(35, 160)

            fecha_creacion = timezone.now() - timedelta(days=random.randint(0, 5), minutes=random.randint(30, 300))
            fecha_entregado = fecha_creacion + timedelta(minutes=minutos_atencion)

            pedido = Pedido.objects.create(
                mesa=mesa,
                nombre_cliente=nombre_cliente,
                estado=Pedido.Estado.ENTREGADO,
                inicio_registro=fecha_creacion - timedelta(seconds=segundos_registro),
                fin_registro=fecha_creacion,
                tiempo_registro_segundos=segundos_registro
            )

            productos_pedido = random.sample(productos, k=min(random.randint(1, 3), len(productos)))

            for producto in productos_pedido:
                cantidad = random.randint(1, 3)

                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )

            pedido.calcular_total()

            Pedido.objects.filter(id=pedido.id).update(
                fecha_creacion=fecha_creacion,
                fecha_entregado=fecha_entregado
            )

            RegistroEvento.objects.create(
                pedido=pedido,
                mesa=mesa,
                tipo_evento=RegistroEvento.TipoEvento.PEDIDO_CREADO,
                descripcion='Pedido de prueba generado para análisis de métricas'
            )

            RegistroEvento.objects.create(
                pedido=pedido,
                mesa=mesa,
                tipo_evento=RegistroEvento.TipoEvento.PEDIDO_ENTREGADO,
                descripcion='Pedido de prueba marcado como entregado'
            )

        self.stdout.write(self.style.SUCCESS('Se generaron 20 pedidos de prueba correctamente.'))