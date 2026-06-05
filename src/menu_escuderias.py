from rich.console import Console
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
    console.print("[#a61b1b]Agregar Escuderia: [/#a61b1b]\n")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla de la escuderia (3 letras): [/#a61b1b]"
    ).upper()

    if not validar_sigla(sigla):
        console.print(
            "[#a61b1b]Error: "
            "La sigla debe tener exactamente 3 letras.[/#a61b1b]"
        )
        return

    if sigla in escuderias:
        console.print(
            "[#a61b1b]Error: Ya existe una escuderia con esa sigla.[/#a61b1b]"
        )
        return

    nombre = console.input(
        "[#a61b1b]Ingrese el nombre de la escuderia: [/#a61b1b]")

    if not nombre:
        console.print(
            "[#a61b1b]Error: El nombre no puede estar vacío.[/#a61b1b]")
        return
    pais = console.input(
        "[#a61b1b]Ingrese el pais de la escuderia: [/#a61b1b]")

    if not pais:
        console.print(
            "[#a61b1b]Error: El pais no puede estar vacío.[/#a61b1b]")
        return
    escuderias[sigla] = {
        "nombre": nombre,
        "pais": pais,
        "pilotos": [],
        "puntos": 0}
    console.print(
        f"[#a61b1b]Escuderia {nombre} agregada correctamente.[/#a61b1b]")


def modificar_escuderia():
    """
    Objetivo: Modificar el nombre y/o pais de una escuderia existente.
    Entrada: No recibe parametros, los datos se ingresan por consola.
    Salida: No retorna nada, modifica el diccionario escuderias en memoria.
    """
    console.print("[#a61b1b] Modificar Escuderia[/#a61b1b]")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla de la escuderia: [/#a61b1b]"
    ).upper()
    if not validar_sigla(sigla):
        console.print("[#a61b1b] Error: "
                      "La sigla debe tener exactamente 3 letras.[/#a61b1b]"
                      )
        return

    if sigla not in escuderias:
        console.print(
            "[#a61b1b]Error: No existe una escuderia con esa sigla[/#a61b1b]"
        )
        return
    console.print(
        f"[#a61b1b]Nombre Actual: {escuderias[sigla]['nombre']}[/#a61b1b]")
    console.print(
        f"[#a61b1b]Pais actual: {escuderias[sigla]['pais']}[/#a61b1b]")

    nombre = console.input(
        "[#a61b1b]Nuevo nombre (deje en blanco para no modificar): [/#a61b1b]")
    if nombre == "":
        nombre = escuderias[sigla]["nombre"]
    pais = console.input(
        "[#a61b1b]Nuevo pais (deje en blanco para no modificar): [/#a61b1b]\n")
    if pais == "":
        pais = escuderias[sigla]["pais"]
    escuderias[sigla]["nombre"] = nombre
    escuderias[sigla]["pais"] = pais

    console.print(
        f"[#a61b1b]Escuderia '{sigla}' modificada correctamente.[/#a61b1b]")


def ver_escuderias():
    """
    Objetivo: Mostrar todas las escuderias cargadas usando la tabla generica
    """
    if not escuderias:
        console.print(
            "[#a61b1b]No hay escuderías registradas en el sistema.[/#a61b1b]"
        )
        return

    # Cabeceras de la tabla
    cabeceras = ["Sigla", "Nombre", "Pais", "Pilotos", "Puntos"]

    # Lista de filas
    filas = []
    for sigla, datos in escuderias.items():
        # Formateamos la lista de pilotos para que sea un string separado por
        # comas

        if datos["pilotos"]:
            pilotos_formateados = ", ".join(datos["pilotos"])
        else:
            pilotos_formateados = "Sin Pilotos"
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
    console.print("[#a61b1b]Eliminar escuderia[/#a61b1b]\n")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla de la escuderia: [/#a61b1b]"
    ).upper()
    if not validar_sigla(sigla):
        console.print(
            "[#a61b1b] Error: "
            "La sigla debe tener exactamente 3 letras.[/#a61b1b]\n"
        )
        return

    if sigla not in escuderias:
        console.print(
            "[#a61b1b]Error: No existe una escuderia con esa sigla[/#a61b1b]\n"
        )
        return

    console.print(
        f"[#a61b1b]Nombre: {
            escuderias[sigla]['nombre']}[/#a61b1b]\n")
    console.print(f"[#a61b1b]Pais: {escuderias[sigla]['pais']}[/#a61b1b]\n")
    confirmacion = console.input(
        "[#a61b1b]¿Esta seguro "
        "que desea eliminar esta escuderia (S= si, N= no)?: "
    )
    if confirmacion.upper() == "S":
        for sigla_piloto in escuderias[sigla]["pilotos"]:
            if sigla_piloto in pilotos:
                pilotos[sigla_piloto]["escuderia"] = "SIN ESCUDERIA"

        del escuderias[sigla]
        console.print(
            f"[#a61b1b]Escuderia '{sigla}' eliminada exitosamente.[/#a61b1b]\n"
        )
    else:
        console.print("\n[#a61b1b]Operacion cancelada.[/#a61b1b]")


def menu_escuderias():
    """
    Objetivo: Controlador principal del flujo del submenú del ABM de Escuderías.
    Entrada:
        - Ninguna (Interacción por consola).
    Salida:
        - None (Retorna al menú principal al seleccionar '0').
    """
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
                console.print(
                    "[#a61b1b]--> Volviendo al menú principal...[/#a61b1b]")
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if opcion != "0":
            console.input(
                "\n[#a61b1b]Presione Enter para continuar...[/#a61b1b]")
