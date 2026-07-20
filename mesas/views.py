from io import BytesIO
import qrcode

from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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


def generar_qr_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)

    url_menu = request.build_absolute_uri(
        reverse('menu_mesa', args=[mesa.numero])
    )

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(url_menu)
    qr.make(fit=True)

    imagen = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    imagen.save(buffer, format='PNG')

    nombre_archivo = f'mesa_{mesa.numero}_qr.png'

    mesa.qr_imagen.save(
        nombre_archivo,
        ContentFile(buffer.getvalue()),
        save=False
    )

    mesa.qr_generado = True
    mesa.save()

    return redirect('mapa_mesas')