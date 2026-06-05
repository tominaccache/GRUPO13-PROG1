from rich.console import Console
from rich.panel import Panel
from utils import mostrar_menu_generico, mostrar_tabla_generica
import datos
from manejo_archivos import exportar_reporte_txt

console = Console()


def mostrar_tabla_pilotos():
    """
    Objetivo: Generar y renderizar la clasificación actual del Campeonato
              Mundial de Pilotos, ordenada por puntaje de mayor a menor.
    Entrada:
        - Ninguna.
    Salida:
        - None (Imprime la tabla dinámica por consola).
    """
    if not datos.pilotos:
        console.print(
            "[yellow]Aún no hay datos registrados.[/yellow]"
        )
        return

    titulo = "Clasificación de Pilotos"
    columnas = ["Pos", "Sigla", "Piloto",
                "Nacionalidad", "Escudería", "Puntos"]
    alineaciones = ["center", "center", "left", "left", "center", "right"]

    pilotos_ordenados = sorted(
        datos.pilotos.items(),
        key=lambda item: item[1]["puntos"],
        reverse=True,
    )

    filas = []
    for pos, (sigla, info) in enumerate(pilotos_ordenados, 1):
        filas.append([
            pos,
            sigla,
            info["datos_personales"][0],
            info["datos_personales"][1],
            info["escuderia"],
            info["puntos"]
        ])

    mostrar_tabla_generica(titulo, columnas, filas, alineaciones)


def menu_tabla_posiciones():
    """
    Objetivo: Generar y renderizar la clasificación del Campeonato Mundial
              de Constructores, sumando los puntos de sus pilotos.
    Entrada:
        - Ninguna.
    Salida:
        - None (Imprime la tabla dinámica por consola).
    """
    opciones = [
        "1. Ver Tabla de Pilotos",
        "2. Ver Tabla de Escuderías",
        "3. Exportar Clasificación",
        "0. Volver al menú principal"
    ]

    while True:
        console.clear()

        op = mostrar_menu_generico("Tabla de Posiciones 📊", opciones)

        if op == "1":
            console.clear()
            mostrar_tabla_pilotos()
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "2":
            console.clear()
            mostrar_tabla_escuderias()
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "3":
            console.clear()
            exportar_reporte_txt()
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "0":
            break

        else:
            console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")
            console.input(
                "\n[#a61b1b]Presione Enter para continuar...[/#a61b1b]")


def mostrar_tabla_escuderias():
    """
    Objetivo: Controlador del submenú para visualizar clasificaciones y reportes.
    Entrada:
        - Ninguna (Interacción por consola).
    Salida:
        - None (Retorna al menú principal al seleccionar '0').
    """
    if not datos.escuderias:
        console.print(
            "[yellow]Aún no hay datos registrados en el sistema para mostrar[/yellow]"
        )
        return
    titulo = "Clasificación de Escuderías"
    columnas = ["Sigla", "Escudería", "País", "Puntos", "Pilotos"]
    alineaciones = ["center", "left", "left", "right", "left"]

    escuderias = sorted(
        datos.escuderias.items(),
        key=lambda item: item[1].get("puntos", 0),
        reverse=True,
    )

    filas = []
    for sigla, info in escuderias:
        nombres_pilotos = ", ".join(
            datos.pilotos[p]["datos_personales"][0] if p in datos.pilotos else p
            for p in info.get("pilotos", [])
        )

        filas.append([
            sigla,
            info.get("nombre", "N/A"),
            info.get("pais", "N/A"),
            info.get("puntos", 0),
            nombres_pilotos
        ])

    mostrar_tabla_generica(titulo, columnas, filas, alineaciones)
