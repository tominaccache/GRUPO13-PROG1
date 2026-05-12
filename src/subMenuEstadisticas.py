from rich.console import Console
from utils import mostrar_menu_generico

# Inicializamos la consola

console = Console()


def menu_estadisticas():
    opcion = "-1"
    opciones_menu = [
        "1. Pilotos con Puntos",
        "2. Promedio de Tiempos",
        "3. Mejor Tiempo",
        "4. Cantidad de Victorias",
        "0. Volver al Menú Principal",
    ]
    while opcion != "0":
        console.clear()
        opcion = mostrar_menu_generico("Estadisticas", opciones_menu)
        match opcion:
            case "1":
                console.print(
                    "[#a61b1b]--> Pilotos con puntos (en producción)[/#a61b1b]"
                )
            case "2":
                console.print(
                    "[#a61b1b]--> Promedio de tiempos (en producción)[/#a61b1b]"
                )
            case "3":
                console.print(
                    "[#a61b1b]--> Mejor tiempo (en producción)[/#a61b1b]")
            case "4":
                console.print(
                    "[#a61b1b]--> Cantidad de victorias (en producción)[/#a61b1b]"
                )
            case "0":
                console.print(
                    "[#a61b1b]--> Volviendo al menú principal. [/#a61b1b]")
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")
        if opcion != "0":
            console.input(
                "[#a61b1b]--> Presione Enter para continuar. [/#a61b1b]")
