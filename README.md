# Sistema Integral de Pedidos Digitales QR para Restaurante

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema web para la gestión de pedidos digitales en un restaurante mediante códigos QR asignados a cada mesa.

El sistema permite que el cliente escanee el QR de su mesa, consulte el menú digital, registre su pedido y lo envíe directamente al panel de cocina. Posteriormente, el personal puede cambiar el estado del pedido y consultar métricas relacionadas con tiempos de atención, ventas y productos vendidos.

El objetivo principal es reducir errores en la toma de pedidos, mejorar el control operativo del restaurante y generar datos útiles para el análisis del proceso de atención.

---

## Problema que resuelve

En muchos restaurantes pequeños, la toma de pedidos se realiza de forma manual, lo que puede provocar:

- Errores al registrar productos.
- Demoras en la comunicación con cocina.
- Falta de seguimiento del estado del pedido.
- Ausencia de métricas sobre tiempos de atención.
- Dificultad para analizar ventas y productos más solicitados.

Este sistema propone una solución digital sencilla, local y accesible para mejorar la administración de pedidos.

---

## Objetivo general

Desarrollar un sistema web funcional que permita registrar pedidos digitales por mesa mediante códigos QR, administrar el flujo de atención en cocina y generar métricas para el análisis operativo del restaurante.

---

## Objetivos específicos

- Crear un menú digital accesible mediante código QR.
- Registrar pedidos asociados a una mesa.
- Administrar estados del pedido: pendiente, en preparación, listo y entregado.
- Visualizar el estado de las mesas.
- Generar códigos QR individuales por mesa.
- Consultar historial de pedidos entregados.
- Generar métricas de atención y ventas.
- Exportar datos en formato CSV para análisis.
- Probar el sistema con datos simulados.

---

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript básico
- Bootstrap / diseño responsivo
- Git y GitHub
- Librería qrcode
- Pillow

---

## Módulos del sistema

### 1. Administración

Permite gestionar desde el panel administrativo:

- Mesas
- Categorías
- Productos
- Pedidos
- Detalles de pedido
- Eventos del sistema

### 2. Menú digital por mesa

Cada mesa cuenta con una URL propia, por ejemplo:

```text
/mesa/1/