from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datos import escuderias, pilotos
import re
from utils import mostrar_menu_generico, mostrar_tabla_generica

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
    Salida: No retorna nada, modifica el diccionario escuderias en memoria.
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
    Salida: No retorna nada, modifica el diccionario escuderias en memoria.
    """
    console.print("[bold red] Modificar Escuderia[/bold red]")
    sigla = console.input(
        "[bold red]Ingrese la sigla de la escuderia: [/bold red]"
    ).upper()
    if not validar_sigla(sigla):
        console.print(
            "[bold red] Error: La sigla debe tener exactamente 3 letras.[/bold red]"
        )
        return

    if sigla not in escuderias:
        console.print(
            "[bold red]Error: No existe una escuderia con esa sigla[/bold red]"
        )
        return
    console.print(f"[bold red]Nombre Actual: {escuderias[sigla]['nombre']}[/bold red]")
    console.print(f"[bold red]Pais actual: {escuderias[sigla]['pais']}[/bold red]")

    nombre = console.input("[bold red]Ingrese el nuevo nombre: [/bold red]")
    pais = console.input("[bold red]Ingrese el nuevo pais: [/bold red]\n")
    escuderias[sigla]["nombre"] = nombre
    escuderias[sigla]["pais"] = pais

    console.print(f"[bold red]Escuderia '{sigla}' modificada correctamente.[/bold red]")


def ver_escuderias():
    """
    Objetivo: Mostrar todas las escuderias cargadas usando la tabla generica
    """
    if not escuderias:
        console.print(
            "[bold red]No hay escuderías registradas en el sistema.[/bold red]"
        )
        return

    # Cabeceras de la tabla
    cabeceras = ["Sigla", "Nombre", "Pais", "Pilotos", "Puntos"]

    # Lista de filas
    filas = []
    for sigla, datos in escuderias.items():
        # Formateamos la lista de pilotos para que sea un string separado por comas
        pilotos_formateados = ", ".join(
            datos["pilotos"] if datos["pilotos"] else "Sin Pilotos"
        )

        fila = [
            sigla,
            datos["nombre"],
            datos["pais"],
            pilotos_formateados,
            datos["puntos"],
        ]
        filas.append(fila)

    # Llamamos a la funcion generica
    mostrar_tabla_generica("Escuderias Oficiales F1", cabeceras, filas)


def eliminar_escuderia():
    """
    Objetivo: Eliminar una escuderia existente del diccionario de escuderias.
    Entrada: No recibe parametros, los datos se ingresan por consola.
    Salida: No retorna nada, modifica el diccionario escuderias en memoria.
    """
    console.print("[bold red]Eliminar escuderia[/bold red]\n")
    sigla = console.input(
        "[bold red]Ingrese la sigla de la escuderia: [/bold red]"
    ).upper()
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

    console.print(f"[bold red]Nombre: {escuderias[sigla]['nombre']}[/bold red]\n")
    console.print(f"[bold red]Pais: {escuderias[sigla]['pais']}[/bold red]\n")
    confirmacion = console.input(
        "[bold red]¿Esta seguro que desea eliminar esta escuderia (S= si, N= no)?: "
    )
    if confirmacion.upper() == "S":
        for sigla_piloto in escuderias[sigla]["pilotos"]:
            if sigla_piloto in pilotos:
                pilotos[sigla_piloto]["escuderia"] = "SIN ESCUDERIA"

        del escuderias[sigla]
        console.print(
            f"[bold red]Escuderia '{sigla}' eliminada exitosamente.[/bold red]\n"
        )
    else:
        console.print("\n[bold red]Operacion cancelada.[/bold red]")


def menu_escuderias():
    opciones_menu = [
        "1. Agregar Escudería",
        "2. Modificar Escudería",
        "3. Eliminar Escudería",
        "4. Ver Escuderías",
        "0. Volver al menú principal",
    ]
    opcion = "-1"
    while opcion != "0":
        console.clear()

        opcion = mostrar_menu_generico("Gestion de Escuderías", opciones_menu)
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
