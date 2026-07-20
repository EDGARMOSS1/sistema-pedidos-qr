# Hipótesis Causal y Métricas Cuantificables

## Sistema Integral de Pedidos Digitales QR para Restaurante

Este documento presenta la hipótesis causal cuantificable del proyecto, incluyendo variable independiente, variable dependiente, baseline, porcentaje esperado de mejora y estructura de medición mediante la tabla `log_pedidos`.

---

## Hipótesis causal cuantificable

La implementación de un sistema digital de pedidos mediante códigos QR reducirá el tiempo de captura y procesamiento de pedidos en comparación con el proceso manual tradicional, esperando una disminución mínima del 25% en el tiempo promedio de atención operativa durante pruebas con 20 o más registros.

---

## Estructura de la hipótesis

| Elemento | Definición |
|---|---|
| Variable independiente | Implementación del sistema digital de pedidos mediante códigos QR |
| Variable dependiente | Tiempo de captura y procesamiento de pedidos |
| Baseline | Proceso manual tradicional de toma de pedidos sin sistema digital |
| Métrica principal | Tiempo de captura y procesamiento medido en milisegundos |
| Porcentaje esperado | Reducción mínima del 25% |
| Muestra mínima | 20 registros de pedidos |
| Tabla de medición | `log_pedidos` |

---

## Variable independiente

La variable independiente es el uso del sistema digital de pedidos mediante códigos QR.

Esta variable representa el cambio aplicado al proceso tradicional del restaurante, sustituyendo la captura manual del pedido por un flujo digital donde el cliente escanea un QR, selecciona productos y envía el pedido directamente al sistema.

---

## Variable dependiente

La variable dependiente corresponde al tiempo de captura y procesamiento del pedido.

Esta variable se mide mediante los siguientes campos:

| Campo | Descripción |
|---|---|
| `tiempo_captura_ms` | Tiempo que tarda el cliente en capturar el pedido desde que abre el menú hasta que lo envía |
| `tiempo_procesamiento_ms` | Tiempo que tarda el sistema en registrar y procesar el pedido en la base de datos |

---

## Baseline

El baseline corresponde al proceso manual tradicional de toma de pedidos.

En este proceso, el mesero toma el pedido de forma verbal o escrita, lo comunica a cocina y posteriormente se registra o confirma de manera manual. Este flujo puede generar demoras, errores de captura y falta de datos medibles.

Para fines del proyecto, el baseline se considera como el tiempo promedio estimado de captura y procesamiento manual contra el cual se compara el sistema digital.

---

## Porcentaje esperado de mejora

El porcentaje esperado de mejora es una reducción mínima del 25% en el tiempo promedio de captura y procesamiento de pedidos.

Esto significa que el sistema digital será considerado favorable si logra reducir el tiempo operativo frente al proceso manual tradicional.

---

## Tabla de medición: `log_pedidos`

Para respaldar la hipótesis con datos cuantificables, el sistema incluye una tabla llamada `log_pedidos`.

La tabla almacena registros con la siguiente estructura:

| Campo | Descripción |
|---|---|
| `timestamp` | Fecha y hora en que se generó el registro |
| `pedido_id` | Identificador del pedido asociado |
| `tiempo_captura_ms` | Tiempo de captura del pedido en milisegundos |
| `tiempo_procesamiento_ms` | Tiempo de procesamiento interno en milisegundos |

---

## Estructura esperada de registros

La tabla `log_pedidos` debe contener al menos 20 registros para realizar el análisis.

Ejemplo de estructura:

| timestamp | pedido_id | tiempo_captura_ms | tiempo_procesamiento_ms |
|---|---:|---:|---:|
| 2026-07-20 13:45:00 | 1 | 85000 | 250 |
| 2026-07-20 13:47:00 | 2 | 72000 | 190 |
| 2026-07-20 13:50:00 | 3 | 95000 | 310 |

---

## Interpretación esperada

Si el tiempo promedio de captura y procesamiento con el sistema digital es menor al baseline manual en al menos 25%, la hipótesis se considera apoyada por los datos del sistema.

La información registrada permite analizar el comportamiento operativo del restaurante, identificar tiempos de atención y generar evidencia cuantitativa para la evaluación del proyecto.

---

## Conclusión

La hipótesis causal del proyecto queda definida con una estructura completa de variable independiente, variable dependiente, baseline y porcentaje esperado de mejora.

Además, la tabla `log_pedidos` permite respaldar la evaluación mediante registros cuantificables generados por el sistema.