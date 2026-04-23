from rich.console import Console
from rich.panel import Panel

console = Console()


def mostrar_menu_guardar():
    """
    Objetivo: Mostrar el submenú de Guardar Datos.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold red]1. Guardar estado del sistema[/bold red]\n"
        "[bold red]2. Exportar reporte[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]\n"
    )
    panel = Panel(
        texto_menu,
        title="[bold red] Guardar Datos[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=False,
        width=49,
    )
    console.print(panel)
    return console.input("\n[bold red]Seleccione una opción: [/bold red]")


def menu_guardar():
    while True:
        console.clear()
        op = mostrar_menu_guardar()

        match op:
            case "1":
                console.print(
                    "[bold red]--> Guardar estado del sistema (en producción)[/bold red]"
                )
            case "2":
                console.print(
                    "[bold red]--> Exportar reporte.txt (en producción)[/bold red]"
                )
            case "0":
                break
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")

        if op in ("1", "2"):
            console.input("\n[bold red]Presione Enter para continuar.[/bold red]")


def mostrar_menu_cargar():
    """
    Objetivo: Mostrar el submenú de Cargar Datos.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold red]1. Restaurar sistema[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]"
    )
    panel = Panel(
        texto_menu,
        title="[bold red] Cargar Datos[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=False,
        width=49,
    )
    console.print(panel)
    return console.input("\n[bold red]Seleccione una opción: [/bold red]")


def menu_cargar():
    while True:
        console.clear()
        op = mostrar_menu_cargar()

        match op:
            case "1":
                console.print(
                    "[bold red]--> Restaurar desde JSON (en producción)[/bold red]"
                )
            case "0":
                break
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")

        if op in ("1",):
            console.input("\n[bold red]Presione Enter para continuar.[/bold red]")
