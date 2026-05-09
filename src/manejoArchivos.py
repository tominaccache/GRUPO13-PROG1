from rich.console import Console
from utils import mostrar_menu_generico

console = Console()


def menu_guardar():
    opciones_menu = [
        "1. Guardar estado del sistema",
        "2. Exportar reporte",
        "0. Volver al menú principal",
    ]
    while True:
        console.clear()
        op = mostrar_menu_generico("Guardar Datos", opciones_menu)

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


def menu_cargar():
    opciones_menu = ["1. Restaurar sistema", "0. Volver al menú principal"]
    while True:
        console.clear()
        op = mostrar_menu_generico("Cargar Datos", opciones_menu)

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
