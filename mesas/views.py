from django.shortcuts import render
from .models import Mesa
from pedidos.models import Pedido


def mapa_mesas(request):
    mesas = Mesa.objects.filter(activa=True).order_by('numero')
    datos_mesas = []

    for mesa in mesas:
        pedido_activo = Pedido.objects.filter(
            mesa=mesa
        ).exclude(
            estado=Pedido.Estado.ENTREGADO
        ).order_by('-fecha_creacion').first()

        if pedido_activo:
            estado = pedido_activo.estado
            estado_texto = pedido_activo.get_estado_display()
            pedido_id = pedido_activo.id
            cliente = pedido_activo.nombre_cliente
        else:
            estado = 'libre'
            estado_texto = 'Libre'
            pedido_id = None
            cliente = None

        datos_mesas.append({
            'mesa': mesa,
            'estado': estado,
            'estado_texto': estado_texto,
            'pedido_id': pedido_id,
            'cliente': cliente
        })

    return render(request, 'mesas/mapa_mesas.html', {
        'datos_mesas': datos_mesas
    })