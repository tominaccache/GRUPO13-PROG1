# Administrador de Campeonato F1

Sistema de gestión por consola para administrar los datos de telemetría y puntuación de una temporada de Fórmula 1, simulando el sistema utilizado por los equipos.

## Contexto Académico

- **Institución:** UADE - Facultad de Ingeniería (FAIN)
- **Materia:** Programación I
- **Docente:** Lic. María Julia Monasterio
- **Período:** 1er Cuatrimestre - 2026
- **Grupo:** 13

## Integrantes

- Facundo Baigun (Legajo: 1.229.371)
- Tomás Naccache (Legajo: 1.213.462)
- Nicolas Tobon (Legajo: 1.231.286)
- Matías Torres (Legajo: 1.226.466)

## Características Principales

- Interfaz de usuario interactiva por consola con la librería `rich`.
- Gestión completa (ABM) de Pilotos y Escuderías con validación de siglas mediante Expresiones Regulares.
- Registro y validación de tiempos de carrera en formato `HH:MM:SS.mmm`, con soporte para vuelta perdida (`+N`) y abandono (`DNF`).
- Cálculo automático de puntos y Tabla de Posiciones mediante matrices bidimensionales.
- Proyección matemática de chances de campeonato por piloto.
- Persistencia de datos mediante archivos JSON.

## Estructura del Proyecto

```
src/
├── main.py                  # Punto de entrada y menú principal
├── datos.py                 # Estructuras de datos globales
├── utils.py                 # Funciones genéricas reutilizables
├── subMenuGestionPiloto.py  # ABM de pilotos
├── menuEscuderias.py        # ABM de escuderías
├── Registrar_Resultado.py   # Registro y gestión de resultados de carrera
├── Tabla_Posiciones.py      # Tabla de pilotos y constructores
├── subMenuEstadisticas.py   # Estadísticas del campeonato
├── proyeccion.py            # Proyección de campeonato
└── manejoArchivos.py        # Guardar y cargar datos
```

Este proyecto utiliza la librería `rich` para mejorar la interfaz visual de la consola (autorizado por la profesora).

Para instalar las dependencias necesarias, ejecutar en la terminal:

```bash
pip install rich
```

## Cómo Ejecutar

```bash
cd src
python main.py
```

## Estado del Proyecto

| Módulo                   | Estado           |
| ------------------------ | ---------------- |
| ABM Pilotos              | ✅ Completo      |
| ABM Escuderías           | ✅ Completo      |
| Registrar Resultados     | ✅ Completo      |
| Tabla de Posiciones      | 🔄 En desarrollo |
| Estadísticas             | 🔄 En desarrollo |
| Proyección de Campeonato | 🔄 En desarrollo |
| Guardar/Cargar Datos     | ✅ En desarrollo |
