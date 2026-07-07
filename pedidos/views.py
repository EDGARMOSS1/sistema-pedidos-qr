from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from mesas.models import Mesa
from menu.models import Categoria, Producto
from metricas.models import RegistroEvento
from .models import Pedido, DetallePedido


def menu_mesa(request, numero_mesa):
    mesa = get_object_or_404(Mesa, numero=numero_mesa, activa=True)
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True).select_related('categoria')

    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente', '').strip()

        if not nombre_cliente:
            return render(request, 'pedidos/menu_mesa.html', {
                'mesa': mesa,
                'categorias': categorias,
                'productos': productos,
                'error': 'Debes ingresar un nombre para el pedido.'
            })

        productos_seleccionados = []

        for producto in productos:
            cantidad_texto = request.POST.get(f'producto_{producto.id}', '0')

            try:
                cantidad = int(cantidad_texto)
            except ValueError:
                cantidad = 0

            if cantidad > 0:
                productos_seleccionados.append((producto, cantidad))

        if not productos_seleccionados:
            return render(request, 'pedidos/menu_mesa.html', {
                'mesa': mesa,
                'categorias': categorias,
                'productos': productos,
                'error': 'Debes seleccionar al menos un producto.'
            })

        with transaction.atomic():
            pedido = Pedido.objects.create(
                mesa=mesa,
                nombre_cliente=nombre_cliente
            )

            for producto, cantidad in productos_seleccionados:
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )

            pedido.calcular_total()

            RegistroEvento.objects.create(
                pedido=pedido,
                mesa=mesa,
                tipo_evento=RegistroEvento.TipoEvento.PEDIDO_CREADO,
                descripcion=f'Pedido creado desde la mesa {mesa.numero}'
            )

        return redirect('pedido_confirmado', pedido_id=pedido.id)

    return render(request, 'pedidos/menu_mesa.html', {
        'mesa': mesa,
        'categorias': categorias,
        'productos': productos
    })


def pedido_confirmado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    return render(request, 'pedidos/pedido_confirmado.html', {
        'pedido': pedido
    })