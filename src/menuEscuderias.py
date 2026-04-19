from rich.console import Console
from rich.panel import Panel
import re
from datos import escuderias

# Inicializacion de la Consola
console = Console()


def agregar_escuderia():
    """_summary_"""
    console.print("[bold red]Agregar Escuderia: [/bold red]\n")
    sigla = console.input("[bold red]Ingrese la sigla de la escuderia (3 letras): [/bold red]").upper()
    
    if not re.fullmatch(r"[A-Z]{3}", sigla):
        console.print("[bold red]Error: La sigla debe tener exactamente 3 letras.[/bold red]")
        return
    
    if sigla in escuderias:
        console.print("[bold red]Error: Ya existe una escuderia con esa sigla.[/bold red]")
        return
    
    nombre = console.input("[bold red]Ingrese el nombre de la escuderia: [/bold red]")
    pais = console.input("[bold red]Ingrese el pais de la escuderia: [/bold red]")
    escuderias[sigla] = {"nombre": nombre, "pais": pais, "pilotos": [], "puntos": 0}
    console.print(f"[bold red]Escuderia {nombre} agregada correctamente.[/bold red]")


def mostrar_menu_escuderias():
    """
    Objetivo: Mostrar el submenú de Gestión de Escuderías.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold red]1. Agregar escudería[/bold red]\n"
        "[bold red]2. Modificar escudería[/bold red]\n"
        "[bold red]3. Eliminar escudería[/bold red]\n"
        "[bold red]4. Ver escuderías[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]"
    )

    panel = Panel(
        texto_menu,
        title="[bold red] Gestión de Escuderías[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=True,
        width=49,
    )
    console.print(panel)


def modificar_escuderia():
    return


def ver_escuderia():
    return


def eliminar_escuderia():
    return


def ver_escuderias():
    return


def menu_escuderias():
    opcion = "-1"
    while opcion != "0":
        console.clear()
        mostrar_menu_escuderias()
        opcion = console.input("\n[bold red]Seleccione una opción: [/bold red]")
        print()
        match opcion:
            case "1":
                console.clear()
                agregar_escuderia()
            case "2":
                console.clear()
                modificar_escuderia()
            case "3":
                console.clear()
                eliminar_escuderia()
            case "4":
                console.clear()
                ver_escuderias()
            case "0":
                console.print("[bold red]--> Volviendo al menú principal...[/bold red]")
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")

        if opcion != "0":
            console.input("\n[bold red]Presione Enter para continuar...[/bold red]")
