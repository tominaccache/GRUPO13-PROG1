from rich.console import Console
from rich.panel import Panel

# Inicializamos la consola
console = Console()

def mostrar_menu_estadisticas():
    """
    Objetivo: Mostrar el panel visual con las opciones de estadísticas.
    """
    texto_menu = (
        "[bold red]1. Piloto con puntos[/bold red]\n"
        "[bold red]2. Promedio de tiempos[/bold red]\n"
        "[bold red]3. Mejor Tiempo[/bold red]\n"
        "[bold red]4. Cantidad de Victorias[/bold red]\n"
        "[bold red]0. Salir[/bold red]\n"
    )
    panel = Panel(
        texto_menu,
        title="[bold red]Estadísticas[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=False,
        width=49
    )
    console.print(panel)


def menu_estadisticas():
    """
    Objetivo: Controlar el flujo y navegación del submenú.
    """
    opcion = "-1"
    while opcion != "0":
        console.clear()
        mostrar_menu_estadisticas()
        opcion = console.input("\n[bold red]Seleccione una opción: [/bold red]")
        match opcion:
            case "1":
                console.print("[bold yellow]--> Opción 1: Pilotos con puntos (En desarrollo)...[/bold yellow]")
            case "2":
                console.print("[bold yellow]--> Opción 2: Promedio de tiempos (En desarrollo)...[/bold yellow]")
            case "3":
                console.print("[bold yellow]--> Opción 3: Mejor tiempo (En desarrollo)...[/bold yellow]")
            case "4":
                console.print("[bold yellow]--> Opción 4: Cantidad de victorias (En desarrollo)...[/bold yellow]")
            case "0":
                console.print("[bold red]--> Volviendo al menú principal. [/bold red]")
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")
                
        if opcion != "0":
            console.input("\n[bold red]--> Presione Enter para continuar. [/bold red]")