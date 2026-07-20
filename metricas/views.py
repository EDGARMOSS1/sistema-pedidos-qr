from django.shortcuts import render
from pedidos.models import Pedido


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