# Pruebas del Sistema

## Sistema Integral de Pedidos Digitales QR para Restaurante

Este documento describe las pruebas realizadas al sistema con el objetivo de validar el funcionamiento de sus módulos principales: menú digital, registro de pedidos, panel de cocina, mapa de mesas, generación de códigos QR, métricas, historial y análisis de resultados.

---

## Objetivo de las pruebas

Comprobar que el sistema permite registrar pedidos digitales mediante códigos QR, administrar su estado desde cocina, generar datos de atención y consultar métricas útiles para el análisis operativo del restaurante.

---

## Ambiente de prueba

| Elemento | Descripción |
|---|---|
| Sistema operativo | Windows |
| Lenguaje | Python |
| Framework | Django |
| Base de datos | SQLite |
| Navegador | Google Chrome / Microsoft Edge |
| Servidor | Servidor local de desarrollo |
| URL base | `http://127.0.0.1:8000/` |

---

## Datos iniciales utilizados

Para realizar las pruebas se cargaron datos iniciales mediante el comando:

```bash
python manage.py cargar_datos_iniciales