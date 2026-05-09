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
                    "[bold red]--> Pilotos con puntos (en producción)[/bold red]"
                )
            case "2":
                console.print(
                    "[bold red]--> Promedio de tiempos (en producción)[/bold red]"
                )
            case "3":
                console.print("[bold red]--> Mejor tiempo (en producción)[/bold red]")
            case "4":
                console.print(
                    "[bold red]--> Cantidad de victorias (en producción)[/bold red]"
                )
            case "0":
                console.print("[bold red]--> Volviendo al menú principal. [/bold red]")
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")
        if opcion != "0":
            console.input("[bold red]--> Presione Enter para continuar. [/bold red]")
