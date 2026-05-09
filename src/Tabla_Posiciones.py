from rich.console import Console
from rich.panel import Panel
from utils import mostrar_menu_generico, mostrar_tabla_generica

console = Console()


def menu_tabla_posiciones():
    opciones_menu = [
        "1. Ver Tabla de Pilotos",
        "2. Ver Tabla de Escuderías",
        "3. Exportar Clasificación",
        "0. Volver al menú principal"
    ]
    continuar_programa = True
    while continuar_programa:
        console.clear()
        op = mostrar_menu_generico("Tabla de Posiciones", opciones_menu)
        match op:
            case "1":
                console.print(
                    "[bold red]--> Ver Tabla de Pilotos (próximamente)[/bold red]"
                )
            case "2":
                console.print(
                    "[bold red]--> Ver Tabla de Escuderías (próximamente)[/bold red]"
                )
            case "3":
                console.print(
                    "[bold red]--> Exportar Clasificación (proximamente)[/bold red]"
                )
            case "0":
                continuar_programa = False
            case _:
                console.print("[bold red]--> Opcion no Válida.[/bold red]")

        if op != "0":
            console.input("\n[bold red]Presione Enter para continuar.[/bold red]")
