import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from pedidos.models import Pedido, DetallePedido


def dashboard_metricas(request):
    pedidos = Pedido.objects.all().order_by('-fecha_creacion')
    pedidos_entregados = pedidos.filter(estado=Pedido.Estado.ENTREGADO)
    pedidos_activos = pedidos.exclude(estado=Pedido.Estado.ENTREGADO)

    total_pedidos = pedidos.count()
    total_entregados = pedidos_entregados.count()
    total_activos = pedidos_activos.count()

    registros_validos = pedidos.exclude(tiempo_registro_segundos=0)

    promedio_registro = 0
    if registros_validos.exists():
        suma_registros = sum(p.tiempo_registro_segundos for p in registros_validos)
        promedio_registro = round(suma_registros / registros_validos.count(), 2)

    tiempos_atencion = []

    for pedido in pedidos_entregados:
        tiempo = pedido.tiempo_total_minutos()
        if tiempo is not None:
            tiempos_atencion.append(tiempo)

    promedio_atencion = 0
    if tiempos_atencion:
        promedio_atencion = round(sum(tiempos_atencion) / len(tiempos_atencion), 2)

    return render(request, 'metricas/dashboard_metricas.html', {
        'pedidos': pedidos,
        'total_pedidos': total_pedidos,
        'total_entregados': total_entregados,
        'total_activos': total_activos,
        'promedio_registro': promedio_registro,
        'promedio_atencion': promedio_atencion,
    })


def exportar_metricas_csv(request):
    pedidos = Pedido.objects.all().order_by('fecha_creacion')

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="metricas_pedidos.csv"'
    response.write('\ufeff')

    writer = csv.writer(response)

    writer.writerow([
        'ID pedido',
        'Mesa',
        'Cliente',
        'Estado',
        'Total',
        'Fecha creación',
        'Fecha entregado',
        'Tiempo registro segundos',
        'Tiempo atención minutos'
    ])

    for pedido in pedidos:
        tiempo_atencion = pedido.tiempo_total_minutos()

        writer.writerow([
            pedido.id,
            pedido.mesa.numero,
            pedido.nombre_cliente,
            pedido.get_estado_display(),
            pedido.total,
            pedido.fecha_creacion,
            pedido.fecha_entregado or '',
            pedido.tiempo_registro_segundos,
            tiempo_atencion if tiempo_atencion is not None else ''
        ])

    return response


def analisis_resultados(request):
    pedidos = Pedido.objects.all().order_by('-fecha_creacion')
    pedidos_entregados = pedidos.filter(estado=Pedido.Estado.ENTREGADO)

    total_pedidos = pedidos.count()
    total_entregados = pedidos_entregados.count()

    venta_total = sum(pedido.total for pedido in pedidos)
    venta_promedio = 0

    if total_pedidos > 0:
        venta_promedio = round(venta_total / total_pedidos, 2)

    tiempos_atencion = []
    pedido_mas_rapido = None
    pedido_mas_lento = None
    menor_tiempo = None
    mayor_tiempo = None

    for pedido in pedidos_entregados:
        tiempo = pedido.tiempo_total_minutos()

        if tiempo is not None:
            tiempos_atencion.append(tiempo)

            if menor_tiempo is None or tiempo < menor_tiempo:
                menor_tiempo = tiempo
                pedido_mas_rapido = pedido

            if mayor_tiempo is None or tiempo > mayor_tiempo:
                mayor_tiempo = tiempo
                pedido_mas_lento = pedido

    promedio_atencion = 0
    if tiempos_atencion:
        promedio_atencion = round(sum(tiempos_atencion) / len(tiempos_atencion), 2)

    producto_mas_vendido = DetallePedido.objects.values(
        'producto__nombre'
    ).annotate(
        total_vendido=Sum('cantidad')
    ).order_by('-total_vendido').first()

    return render(request, 'metricas/analisis_resultados.html', {
        'total_pedidos': total_pedidos,
        'total_entregados': total_entregados,
        'venta_total': venta_total,
        'venta_promedio': venta_promedio,
        'promedio_atencion': promedio_atencion,
        'pedido_mas_rapido': pedido_mas_rapido,
        'pedido_mas_lento': pedido_mas_lento,
        'menor_tiempo': menor_tiempo,
        'mayor_tiempo': mayor_tiempo,
        'producto_mas_vendido': producto_mas_vendido,
    })