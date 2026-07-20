from django.core.management.base import BaseCommand

from mesas.models import Mesa
from menu.models import Categoria, Producto


class Command(BaseCommand):
    help = 'Carga datos iniciales del sistema'

    def handle(self, *args, **options):
        mesas = [
            (1, 'Mesa cerca de entrada'),
            (2, 'Mesa central'),
            (3, 'Mesa junto a ventana'),
            (4, 'Mesa familiar'),
        ]

        for numero, descripcion in mesas:
            Mesa.objects.get_or_create(
                numero=numero,
                defaults={
                    'descripcion': descripcion,
                    'activa': True
                }
            )

        comida, _ = Categoria.objects.get_or_create(
            nombre='Comida',
            defaults={'descripcion': 'Platillos principales del restaurante'}
        )

        bebidas, _ = Categoria.objects.get_or_create(
            nombre='Bebidas',
            defaults={'descripcion': 'Bebidas disponibles'}
        )

        postres, _ = Categoria.objects.get_or_create(
            nombre='Postres',
            defaults={'descripcion': 'Postres del restaurante'}
        )

        productos = [
            {
                'nombre': 'Hamburguesa clásica',
                'categoria': comida,
                'descripcion': 'Hamburguesa con carne, queso, lechuga y jitomate',
                'precio': 85.00,
                'tiempo_estimado': 12
            },
            {
                'nombre': 'Papas a la francesa',
                'categoria': comida,
                'descripcion': 'Orden individual de papas fritas',
                'precio': 45.00,
                'tiempo_estimado': 7
            },
            {
                'nombre': 'Refresco',
                'categoria': bebidas,
                'descripcion': 'Bebida fría embotellada',
                'precio': 28.00,
                'tiempo_estimado': 2
            },
            {
                'nombre': 'Café americano',
                'categoria': bebidas,
                'descripcion': 'Café americano caliente',
                'precio': 35.00,
                'tiempo_estimado': 5
            },
            {
                'nombre': 'Rebanada de pastel',
                'categoria': postres,
                'descripcion': 'Postre individual del día',
                'precio': 55.00,
                'tiempo_estimado': 4
            },
        ]

        for producto in productos:
            Producto.objects.get_or_create(
                nombre=producto['nombre'],
                defaults={
                    'categoria': producto['categoria'],
                    'descripcion': producto['descripcion'],
                    'precio': producto['precio'],
                    'tiempo_estimado': producto['tiempo_estimado'],
                    'disponible': True
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Datos iniciales cargados correctamente.')
        )