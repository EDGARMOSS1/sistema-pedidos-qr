from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime
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

        inicio_registro_texto = request.POST.get('inicio_registro')
        inicio_registro = parse_datetime(inicio_registro_texto) if inicio_registro_texto else None
        fin_registro = timezone.now()

        if inicio_registro and timezone.is_naive(inicio_registro):
            inicio_registro = timezone.make_aware(inicio_registro)

        tiempo_registro = 0

        if inicio_registro:
            tiempo_registro = int((fin_registro - inicio_registro).total_seconds())

            if tiempo_registro < 0:
                tiempo_registro = 0

        if not nombre_cliente:
            return render(request, 'pedidos/menu_mesa.html', {
                'mesa': mesa,
                'categorias': categorias,
                'productos': productos,
                'error': 'Debes ingresar un nombre para el pedido.',
                'inicio_registro': inicio_registro_texto or timezone.now().isoformat()
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
                'error': 'Debes seleccionar al menos un producto.',
                'inicio_registro': inicio_registro_texto or timezone.now().isoformat()
            })

        with transaction.atomic():
            pedido = Pedido.objects.create(
                mesa=mesa,
                nombre_cliente=nombre_cliente,
                inicio_registro=inicio_registro,
                fin_registro=fin_registro,
                tiempo_registro_segundos=tiempo_registro
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
        'productos': productos,
        'inicio_registro': timezone.now().isoformat()
    })


def pedido_confirmado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    return render(request, 'pedidos/pedido_confirmado.html', {
        'pedido': pedido
    })


def panel_cocina(request):
    pedidos = Pedido.objects.exclude(
        estado=Pedido.Estado.ENTREGADO
    ).order_by('fecha_creacion')

    return render(request, 'pedidos/panel_cocina.html', {
        'pedidos': pedidos
    })


def cambiar_estado_pedido(request, pedido_id, nuevo_estado):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    estados_validos = [
        Pedido.Estado.PENDIENTE,
        Pedido.Estado.PREPARACION,
        Pedido.Estado.LISTO,
        Pedido.Estado.ENTREGADO
    ]

    if nuevo_estado in estados_validos:
        pedido.cambiar_estado(nuevo_estado)

        RegistroEvento.objects.create(
            pedido=pedido,
            mesa=pedido.mesa,
            tipo_evento=RegistroEvento.TipoEvento.CAMBIO_ESTADO,
            descripcion=f'El pedido cambió al estado: {pedido.get_estado_display()}'
        )

    return redirect('panel_cocina')
def historial_pedidos(request):
    pedidos = Pedido.objects.filter(
        estado=Pedido.Estado.ENTREGADO
    ).order_by('-fecha_entregado', '-fecha_creacion')

    total_entregados = pedidos.count()
    venta_total = sum(pedido.total for pedido in pedidos)

    tiempos_atencion = []

    for pedido in pedidos:
        tiempo = pedido.tiempo_total_minutos()
        if tiempo is not None:
            tiempos_atencion.append(tiempo)

    promedio_atencion = 0
    if tiempos_atencion:
        promedio_atencion = round(sum(tiempos_atencion) / len(tiempos_atencion), 2)

    return render(request, 'pedidos/historial_pedidos.html', {
        'pedidos': pedidos,
        'total_entregados': total_entregados,
        'venta_total': venta_total,
        'promedio_atencion': promedio_atencion
    })