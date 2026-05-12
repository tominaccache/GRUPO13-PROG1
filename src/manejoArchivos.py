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
                    "[#a61b1b]--> Guardar estado del sistema (en producción)[/#a61b1b]"
                )
            case "2":
                console.print(
                    "[#a61b1b]--> Exportar reporte.txt (en producción)[/#a61b1b]"
                )
            case "0":
                break
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if op in ("1", "2"):
            console.input(
                "\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")


def menu_cargar():
    opciones_menu = ["1. Restaurar sistema", "0. Volver al menú principal"]
    while True:
        console.clear()
        op = mostrar_menu_generico("Cargar Datos", opciones_menu)

        match op:
            case "1":
                console.print(
                    "[#a61b1b]--> Restaurar desde JSON (en producción)[/#a61b1b]"
                )
            case "0":
                break
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if op in ("1",):
            console.input(
                "\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")
