# Catálogo de Satélites

**Autor:** Juan Cruz Levanto

## Descripción

Este proyecto permite procesar un catálogo de satélites a partir de un archivo JSON. Utiliza Python y la biblioteca Skyfield para obtener la posición de los satélites en una fecha de referencia y organizar la información mediante objetos.

El programa permite consultar estadísticas del catálogo y analizar los satélites según su tipo de órbita.

## Funcionalidades

- Lectura de los registros de satélites desde un archivo JSON.
- Creación de objetos `Satelite` a partir de los datos obtenidos.
- Validación de los atributos de cada satélite.
- Cálculo de la posición geográfica y la altitud mediante Skyfield.
- Clasificación de los satélites por tipo de órbita.
- Generación de estadísticas por órbita: cantidad de satélites, altitud mínima, máxima y promedio.

## Estructura del proyecto

```text
tpi2-satelites-Levanto/
├── consultar_satelites.py
├── catalogo.py
├── satelite.py
├── funciones_base.py
├── datos/
│   └── satelites.json
└── README.md
```

## Requisitos

- Python 3
- Skyfield
- pytest, para ejecutar las pruebas
- pytest-cov

## Instalación

Crear y activar un entorno virtual:

```bash
python -m venv .venv
```

Instalar las dependencias:

```bash
pip install skyfield pytest
```

## Uso

El programa se ejecuta desde la terminal indicando la ruta del archivo JSON y la operación que se desea realizar.

### Consultar el resumen

```bash
python consultar_satelites.py datos/satelites.json resumen
```

Esta operación muestra estadísticas agrupadas por tipo de órbita, incluyendo la cantidad de satélites y las altitudes mínima, máxima y promedio.

### Consultar satélites por zona

```bash
python consultar_satelites.py datos/satelites.json zona <long_min> <lat_min> <long_max> <lat_max>
```

Los límites corresponden a las longitudes y latitudes de un rectángulo geográfico.

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
pytest
```
