from rich.console import Console
from rich.panel import Panel
from utils import mostrar_menu_generico, mostrar_tabla_generica

console = Console()


def menu_tabla_posiciones():
    opciones = [
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
                    "[#a61b1b]--> Ver Tabla de Pilotos [/#a61b1b]"
                )
            case "2":
                console.print(
                    "[#a61b1b]--> Ver Tabla de Escuderías [/#a61b1b]"
                )
            case "3":
                console.print(
                    "[#a61b1b]--> Exportar Clasificación [/#a61b1b]"
                )
            case "0":
                continuar_programa = False
            case _:
                console.print("[#a61b1b]--> Opcion no Válida.[/#a61b1b]")

        if op != "0":
            console.input(
                "\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")
