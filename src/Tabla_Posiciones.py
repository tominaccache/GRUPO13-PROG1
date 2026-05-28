from rich.console import Console
import datos
from utils import mostrar_menu_generico, mostrar_tabla_generica

console = Console()


def limpiar_consola():
    console.clear()


def menu_tabla_posiciones():
    opciones = [
        "1. Ver Tabla de Pilotos",
        "2. Ver Tabla de Escuderías",
        "3. Exportar Clasificación",
        "0. Volver al menú principal"
    ]

    while True:
        limpiar_consola()

        op = mostrar_menu_generico("Tabla de Posiciones 📊", opciones)

        if op == "1":
            limpiar_consola()
            mostrar_tabla_ejemplo()
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "2":
            limpiar_consola()
            mostrar_tabla_escuderias()
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "0":
            break


def mostrar_tabla_ejemplo():
    titulo = "Clasificación Actual F1"
    columnas = ["Pos", "Piloto", "Escudería", "Puntos"]
    alineaciones = ["center", "left", "left", "right"]

    filas = [
        ["1", "Max Verstappen", "Red Bull", "350"],
        ["2", "Lando Norris", "McLaren", "280"],
        ["3", "Charles Leclerc", "Ferrari", "275"]
    ]

    mostrar_tabla_generica(titulo, columnas, filas, alineaciones)


def mostrar_tabla_escuderias():
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
