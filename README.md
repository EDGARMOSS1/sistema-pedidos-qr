# Sistema Integral de Pedidos Digitales QR para Restaurante

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema web para la gestión de pedidos digitales en un restaurante mediante códigos QR asignados a cada mesa.

El sistema permite que el cliente escanee el QR de su mesa, consulte el menú digital, registre su pedido y lo envíe directamente al panel de cocina. Posteriormente, el personal puede cambiar el estado del pedido y consultar métricas relacionadas con tiempos de atención, ventas y productos vendidos.

El objetivo principal es reducir errores en la toma de pedidos, mejorar el control operativo del restaurante y generar datos útiles para el análisis del proceso de atención.

---

## Problema que resuelve

En muchos restaurantes pequeños, la toma de pedidos se realiza de forma manual, lo que puede provocar errores al registrar productos, demoras en la comunicación con cocina, falta de seguimiento del estado del pedido y ausencia de métricas sobre tiempos de atención.

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
- Git y GitHub
- qrcode
- Pillow

---

## Módulos del sistema

### Administración

Permite gestionar mesas, categorías, productos, pedidos, detalles de pedido y eventos del sistema desde el panel administrativo de Django.

### Menú digital por mesa

Cada mesa cuenta con una URL propia, por ejemplo:

```text
/mesa/1/
```

Desde esta pantalla el cliente puede ingresar su nombre, seleccionar productos y enviar su pedido.

### Panel de cocina

Disponible en:

```text
/cocina/
```

Permite visualizar pedidos activos y cambiar su estado durante el proceso de atención.

### Mapa de mesas

Disponible en:

```text
/mesas/
```

Muestra el estado actual de cada mesa: libre, pendiente, en preparación o listo.

### Códigos QR

El sistema permite generar QR individuales para cada mesa y una vista para imprimirlos:

```text
/mesas/qrs/imprimir/
```

### Historial de pedidos

Disponible en:

```text
/historial/
```

Muestra pedidos entregados, ventas registradas y tiempos de atención.

### Dashboard de métricas

Disponible en:

```text
/metricas/
```

Presenta indicadores como total de pedidos, pedidos activos, pedidos entregados, promedio de registro y promedio de atención.

### Análisis de resultados

Disponible en:

```text
/metricas/analisis/
```

Muestra venta total, venta promedio, pedido más rápido, pedido más lento, producto más vendido y tiempo promedio de atención.

### Exportación CSV

Disponible en:

```text
/metricas/exportar-csv/
```

Permite descargar las métricas del sistema en formato CSV.

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/EDGARMOSS1/sistema-pedidos-qr.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd sistema-pedidos-qr
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual en Windows

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Aplicar migraciones

```bash
python manage.py migrate
```

### 7. Crear superusuario

```bash
python manage.py createsuperuser
```

### 8. Ejecutar servidor

```bash
python manage.py runserver
```

### 9. Abrir el sistema

```text
http://127.0.0.1:8000/
```

---

## Datos de prueba

El sistema incluye un comando para generar pedidos simulados:

```bash
python manage.py generar_datos_prueba
```

Este comando crea registros de prueba para alimentar el historial, las métricas y el análisis de resultados.

---

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Página principal |
| `/admin/` | Panel administrativo |
| `/mesas/` | Mapa visual de mesas |
| `/mesa/1/` | Menú digital de la mesa 1 |
| `/cocina/` | Panel de cocina |
| `/historial/` | Historial de pedidos entregados |
| `/metricas/` | Dashboard de métricas |
| `/metricas/analisis/` | Análisis automático de resultados |
| `/metricas/exportar-csv/` | Exportación de métricas en CSV |
| `/mesas/qrs/imprimir/` | Códigos QR listos para impresión |

---

## Estado actual del proyecto

El proyecto cuenta con un MVP funcional que permite registrar pedidos desde un menú digital, administrar pedidos desde cocina, cambiar estados de atención, visualizar mesas activas, generar códigos QR, imprimirlos, consultar historial, generar métricas, exportar información a CSV y analizar resultados automáticamente.

Avance estimado del proyecto: 87%.

---

## Hipótesis del proyecto

La implementación de un sistema digital de pedidos mediante códigos QR puede mejorar el control operativo del restaurante al reducir la dependencia del registro manual, facilitar el seguimiento de pedidos y generar datos medibles sobre tiempos de atención y ventas.

---

## Autor

Proyecto desarrollado como parte del Proyecto Integrador Dual de Ingeniería en Sistemas Computacionales.

Repositorio:

```text
https://github.com/EDGARMOSS1/sistema-pedidos-qr
```