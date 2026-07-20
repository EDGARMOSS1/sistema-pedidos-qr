import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from mesas.models import Mesa
from menu.models import Producto
from pedidos.models import Pedido, DetallePedido
from metricas.models import RegistroEvento, LogPedido


class Command(BaseCommand):
    help = 'Genera 20 registros en la tabla log_pedidos para análisis cuantificable'

    def handle(self, *args, **options):
        mesas = list(Mesa.objects.filter(activa=True))
        productos = list(Producto.objects.filter(disponible=True))

        if not mesas:
            self.stdout.write(self.style.ERROR('No hay mesas registradas. Ejecuta primero: python manage.py cargar_datos_iniciales'))
            return

        if not productos:
            self.stdout.write(self.style.ERROR('No hay productos registrados. Ejecuta primero: python manage.py cargar_datos_iniciales'))
            return

        nombres = [
            'Edgar', 'Alan', 'Karol', 'Omar', 'Luis',
            'Andrea', 'Mariana', 'Carlos', 'Sofia', 'Diego',
            'Fernanda', 'Miguel', 'Valeria', 'Jorge', 'Diana',
            'Pedro', 'Paola', 'Ricardo', 'Daniela', 'Hugo'
        ]

        for i in range(20):
            mesa = random.choice(mesas)
            nombre_cliente = nombres[i]

            tiempo_captura_ms = random.randint(35000, 160000)
            tiempo_procesamiento_ms = random.randint(80, 900)

            fecha_creacion = timezone.now() - timedelta(
                days=random.randint(0, 5),
                minutes=random.randint(10, 300)
            )

            fecha_entregado = fecha_creacion + timedelta(
                minutes=random.randint(8, 28)
            )

            pedido = Pedido.objects.create(
                mesa=mesa,
                nombre_cliente=nombre_cliente,
                estado=Pedido.Estado.ENTREGADO,
                inicio_registro=fecha_creacion - timedelta(milliseconds=tiempo_captura_ms),
                fin_registro=fecha_creacion,
                tiempo_registro_segundos=round(tiempo_captura_ms / 1000)
            )

            productos_pedido = random.sample(
                productos,
                k=min(random.randint(1, 3), len(productos))
            )

            for producto in productos_pedido:
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=random.randint(1, 3),
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
                descripcion='Pedido registrado para prueba cuantificable'
            )

            RegistroEvento.objects.create(
                pedido=pedido,
                mesa=mesa,
                tipo_evento=RegistroEvento.TipoEvento.PEDIDO_ENTREGADO,
                descripcion='Pedido entregado para prueba cuantificable'
            )

            LogPedido.objects.create(
                pedido=pedido,
                tiempo_captura_ms=tiempo_captura_ms,
                tiempo_procesamiento_ms=tiempo_procesamiento_ms
            )

        self.stdout.write(
            self.style.SUCCESS('Se generaron 20 registros en la tabla log_pedidos correctamente.')
        )