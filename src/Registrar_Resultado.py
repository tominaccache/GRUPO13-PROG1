from rich.console import Console
from utils import mostrar_menu_generico

console = Console()


def limpiar_consola():
    console.clear()


def registrar_tiempos():
    return


def ver_resultados():
    return


def modificar_resultados():
    return


def eliminar_resultados():
    return


def menu_resultados():
    continuar_programa = True

    opciones_submenu = [
        "1. Registrar tiempos de carrera",
        "2. Ver resultados",
        "3. Modificar Resultados",
        "4. Eliminar resultados",
        "0. Volver al menú principal",
    ]

    while continuar_programa:
        limpiar_consola()
        opcion = mostrar_menu_generico(
            "Registro de Resultados de Gran Premio", opciones_submenu
        )
        match opcion:
            case "1":
                registrar_tiempos()
            case "2":
                ver_resultados()
            case "3":
                modificar_resultados()
            case "4":
                eliminar_resultados()
            case "0":
                console.print("[bold red]--> Volviendo al menú principal...[/bold red]")
                continuar_programa = False
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")
        if opcion != "0":
            console.input("\n[bold red]Presione enter para continuar.[/bold red]")
