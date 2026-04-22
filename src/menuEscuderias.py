from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datos import escuderias
import re

# Inicializacion de la Consola
console = Console()


def validar_sigla(sigla):
    """
    Objetivo: Validar que la sigla tenga exactamente 3 letras mayúsculas
    Entrada: sigla (string)
    Salida: True si es valido, False si no lo es
    """
    return bool(re.fullmatch(r"[A-Z]{3}", sigla))


def agregar_escuderia():
    """
    Objetivo: Agregar una nueva escuderia al diccionario de escuderias.
    Entrada: No recibe parametros, los datos se ingresan por consola.
    Salida: No retorna nada, modifica el diccionario escuderias_ en memoria.
    """
    console.print("[bold red]Agregar Escuderia: [/bold red]\n")
    sigla = console.input(
        "[bold red]Ingrese la sigla de la escuderia (3 letras): [/bold red]"
    ).upper()

    if not validar_sigla(sigla):
        console.print(
            "[bold red]Error: La sigla debe tener exactamente 3 letras.[/bold red]"
        )
        return

    if sigla in escuderias:
        console.print(
            "[bold red]Error: Ya existe una escuderia con esa sigla.[/bold red]"
        )
        return

    nombre = console.input("[bold red]Ingrese el nombre de la escuderia: [/bold red]")
    pais = console.input("[bold red]Ingrese el pais de la escuderia: [/bold red]")
    escuderias[sigla] = {"nombre": nombre, "pais": pais, "pilotos": [], "puntos": 0}
    console.print(f"[bold red]Escuderia {nombre} agregada correctamente.[/bold red]")


def modificar_escuderia():
    """
    Objetivo: Modificar el nombre y/o pais de una escuderia existente.
    Entrada: No recibe parametros, los datos se ingresan por consola.
    Salida: No retorna nada, modifica el diccionario escuderias_ en memoria.
    """
    console.print("[bold red] Modificar Escuderia[/bold red]\n")
    sigla = console.input("[bold red]Ingrese la sigla de la escuderia ")
    if not validar_sigla(sigla):
        console.print(
            "[bold red] Error: La sigla debe tener exactamente 3 letras.[/bold red]\n"
        )
        return

    if sigla not in escuderias:
        console.print(
            "[bold red]Error: No existe una escuderia con esa sigla[/bold red]\n"
        )
        return
    console.print(
        f"[bold red]Nombre Actual: {escuderias[sigla]['nombre']}[/bold red]\n"
    )
    console.print(f"[bold red]Pais actual: {escuderias[sigla]['pais']}[/bold red]\n")

    nombre = console.input("[bold red]Ingrese el nuevo nombre: [/bold red]\n")
    pais = console.input("[bold red]Ingrese el nuevo pais: [/bold red]\n")
    escuderias[sigla]["nombre"] = nombre
    escuderias[sigla]["pais"] = pais

    console.print(
        f"[bold red]Escuderia '{sigla}' modificada correctamente.[/bold red]\n"
    )


def ver_escderias():
    """
    Objetivo: Mostrar todas las escuderias cargadas en una tabla.
    Entrada: No recibe parametros.
    Salida: No retorna nada, imprime la tabla por consola.
    """

    tabla = Table(title="Escuderias", border_style="bold red", style="on white")

    # Definimos las columnas de la tabla
    tabla.add_column("Sigla", style="bold white", justify="center")
    tabla.add_column("Nombre", style="bold white", justify="center")
    tabla.add_column("Pais", style="bold white", justify="center")
    tabla.add_column("Pilotos", style="bold white", justify="center")
    tabla.add_column("Puntos", style="bold white", justify="center")

    for sigla, datos in escuderias.items():
        tabla.add_row(
            sigla,
            datos["nombre"],
            datos["pais"],
            ",".join(datos["pilotos"]) if datos["pilotos"] else "Sin Pilotos",
            str(datos["puntos"]),
        )
    console.print(tabla)


def eliminar_escuderia():
    return


def ver_escuderias():
    return


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
