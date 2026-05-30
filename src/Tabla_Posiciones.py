from rich.console import Console
from rich.panel import Panel
from utils import mostrar_menu_generico, mostrar_tabla_generica
import datos
console = Console()


def menu_tabla_posiciones():
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
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "2":
            console.clear()
            mostrar_tabla_escuderias()
            console.input("\n[#a61b1b]Presione Enter para volver...[/#a61b1b]")

        elif op == "0":
            break


def mostrar_tabla_escuderias():
    if not datos.pilotos:
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
