from rich.console import Console
from rich.panel import Panel

# Inicializamos la consola
console = Console()


def menu_pilotos():
    """
    Objetivo: Mostrar el submenú de Gestión de Pilotos.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold red]1. Agregar piloto[/bold red]\n"
        "[bold red]2. Modificar Piloto[/bold red]\n"
        "[bold red]3. Eliminar piloto[/bold red]\n"
        "[bold red]4. Buscar piloto[/bold red]\n"
        "[bold red]5. Listar pilotos[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]"
    )
    panel = Panel(
        texto_menu,
        title="[bold red]Gestión de Pilotos[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=True,
        width=49,
    )
    console.print(panel)

    return console.input("\n[bold red]Seleccione una opción: [/bold red]")


