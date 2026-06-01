import re
from rich.console import Console
from rich.panel import Panel
from datos import pilotos, escuderias, matriz_resultados, carreras
from rich import box
from utils import (
    mostrar_menu_generico,
    mostrar_tabla_generica,
    mostrar_panel_generico
)

# inicializamos la consola
console = Console()


def agregar_piloto():
    """
    Objetivo:
        Solicita datos por consola para un nuevo piloto, valida el formato
        y los inserta en el diccionario principal y en el de su escudería.
    Parámetros: Ninguno (los datos se ingresan via input)
    Retorno: None (modifica los diccionarios globales en mermoria)
    """
    console.print("[#a61b1b]Agregar Piloto:[/#a61b1b]\n")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla del piloto (3 letras): [/#a61b1b]").upper()

    if not re.fullmatch(r"[A-Z]{3}", sigla):
        console.print(
            "[#a61b1b]Error: La sigla debe "
            "tener exactamente 3 letras.[/#a61b1b]"
        )
        return

    if sigla in pilotos:
        console.print(
            "[#a61b1b]Error: Ya existe un piloto con esa sigla.[/#a61b1b]")
        return

    nombre = console.input(
        "[#a61b1b]Ingrese el nombre del piloto: [/#a61b1b]").strip()
    pais = console.input(
        "[#a61b1b]Ingrese el país del piloto: [/#a61b1b]").strip()

    esc_sigla = console.input(
        "[#a61b1b]Ingrese la sigla de la escudería (ej. RBR, FER): "
        "[/#a61b1b]"
    ).upper()

    if esc_sigla not in escuderias:
        console.print(
            "[#a61b1b]Error: "
            "La escudería ingresada no existe en el sistema.[/#a61b1b]"
        )
        return

    # Agregar al diccionario de pilotos
    pilotos[sigla] = {
        "datos_personales": [nombre, pais],
        "escuderia": esc_sigla,
        "puntos": 0
    }

    # Vincular al piloto dentro del diccionario de la escudería para mantener
    # integridad relacional
    escuderias[esc_sigla]["pilotos"].append(sigla)

    # Agregar una fila vaciá a la matriz para el nuevo piloto
    # (Tantas columnas vacías como carreras existan)
    # La columna 0 es la sigla del piloto (identidad)
    matriz_resultados.append([sigla] + [""] * len(carreras))
    console.print(
        f"\n[bold green]✅ Piloto {nombre} ({sigla}) "
        f"agregado correctamente a la escudería {esc_sigla}.[/bold green]"
    )


def modificar_piloto():
    """
    Objetivo:
        Permite actualizar el nombre, país o escuderia de un piloto existente.
        Si el usuario deja el campo en blanco, se conserva el valor anterior.
    Parámetros: Ninguno (interaccion por consola).
    Retorno: None (modifica el estado global).
    """
    console.print("[#a61b1b]Modificar Piloto:[/#a61b1b]\n")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla del piloto a modificar: [/#a61b1b]"
    ).upper()

    if sigla not in pilotos:
        console.print(
            "[#a61b1b]Error: No se encontró "
            "ningún piloto con esa sigla.[/#a61b1b]"
        )
        return

    piloto_actual = pilotos[sigla]
    console.print(
        f"[#a61b1b]Modificando a: "
        f"{piloto_actual['datos_personales'][0]}[/#a61b1b]"
    )

    nuevo_nombre = console.input(
        "[#a61b1b]Nuevo nombre (Deje en blanco para no modificar): "
        "[/#a61b1b]"
    ).strip()

    if nuevo_nombre == "":
        nuevo_nombre = piloto_actual["datos_personales"][0]

    nuevo_pais = console.input(
        "[#a61b1b]Nuevo país (Deje en blanco para no modificar): "
        "[/#a61b1b]"
    ).strip()

    if nuevo_pais == "":
        nuevo_pais = piloto_actual["datos_personales"][1]

    nueva_escuderia = console.input(
        "[#a61b1b]Nueva escudería (Deje en blanco para no modificar): "
        "[/#a61b1b]"
    ).upper()

    if nueva_escuderia.strip() == "":
        nueva_escuderia = piloto_actual["escuderia"]
    elif nueva_escuderia not in escuderias:
        console.print(
            "[#a61b1b]Error: La escudería ingresada no existe. "
            "Se mantendrá la escudería anterior.[/#a61b1b]"
        )
        nueva_escuderia = piloto_actual["escuderia"]
    else:
        # Descisión de diseño: Asegurar que el piloto se desvincule
        # de su escuderia anterio solo si la escudería vieja aún
        # existe en el sistema
        escuderia_antigua = piloto_actual["escuderia"]
        if nueva_escuderia != escuderia_antigua:

            if (escuderia_antigua in escuderias
                        and sigla in escuderias[escuderia_antigua]["pilotos"]
                    ):
                escuderias[escuderia_antigua]["pilotos"].remove(sigla)

            escuderias[nueva_escuderia]["pilotos"].append(sigla)

    # Actualizar datos en el diccionario principal
    pilotos[sigla]["datos_personales"] = [nuevo_nombre, nuevo_pais]
    pilotos[sigla]["escuderia"] = nueva_escuderia

    console.print(
        f"\n[bold green]✅ Datos del piloto {sigla} "
        f"actualizados correctamente.[/bold green]")


def eliminar_piloto():
    """
    Objetivo:
        Elimina a un piloto del sistema y rompe la relación con su escudería.
    Parametros: Ninguno
    Retorno: None
    """
    console.print("[#a61b1b]Eliminar Piloto:[/#a61b1b]\n")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla del piloto a eliminar: [/#a61b1b]").upper()

    if sigla not in pilotos:
        console.print(
            "[#a61b1b]Error: "
            "No se encontró ningún piloto con esa sigla.[/#a61b1b]"
        )
        return

   # Remover al piloto de la lista de su escudería verificando que la
   # escudería aún exista
    escuderia_asignada = pilotos[sigla]["escuderia"]
    if (escuderia_asignada in escuderias
                and sigla in escuderias[escuderia_asignada]["pilotos"]
            ):
        escuderias[escuderia_asignada]["pilotos"].remove(sigla)

    # Guardamos el nombre antes de eliminar y borramos la fila de la matriz
    nombre_eliminado = pilotos[sigla]["datos_personales"][0]

    for i in range(len(matriz_resultados)):
        if matriz_resultados[i][0] == sigla:
            del matriz_resultados[i]
            break

    # Eliminamos del diccionario principal
    del pilotos[sigla]

    console.print(
        f"\n[bold green]✅ El piloto {nombre_eliminado} ({sigla}) "
        f"ha sido eliminado del sistema.[/bold green]")


def buscar_piloto():
    """
    Objetivo:
        Busca un piloto especifico por su sigla y
        renderiza sus datos en un Panel.
    Parametros: Ninguno
    Retrono: None (imprime un Panel de la libreria Rich)
    """
    console.print("[#a61b1b]Buscar Piloto:[/#a61b1b]")
    sigla = console.input(
        "[#a61b1b]Ingrese la sigla del piloto: [/#a61b1b]").upper()
    print()
    if sigla not in pilotos:
        console.print(
            "[#a61b1b]Error: "
            "No se encontró ningún piloto con esa sigla.[/#a61b1b]"
        )
        return

    datos = pilotos[sigla]
    esc_sigla = datos['escuderia']

    # Manejos de casos donde la escuderia fue eliminada del sistema
    # previamente.
    if esc_sigla in escuderias:
        nombre_escuderia = escuderias[esc_sigla]['nombre']
    else:
        nombre_escuderia = "Escudería Eliminada/No existe"

    info_piloto = (
        f"[#a61b1b]Sigla: {sigla} [/#a61b1b]\n"
        f"[#a61b1b]Nombre: {datos['datos_personales'][0]}[/#a61b1b] \n"
        f"[#a61b1b]Nacionalidad: {datos['datos_personales'][1]}[/#a61b1b]\n"
        f"[#a61b1b]Escudería: {datos['escuderia']} "
        f"- {nombre_escuderia}[/#a61b1b]\n"
        f"[#a61b1b]Puntos Campeonato: {datos['puntos']}[/#a61b1b]"
    )

    mostrar_panel_generico("INFORMACIÓN DEL PILOTO", info_piloto)


def listar_pilotos():
    """
    Objetivo:
        Recolecta los datos de todos los pilotos registrados y los envía
        a la función generica para renderizarlos en formato tabla.
    Parámetros: Ninguno
    Retorno: None.
    """
    if not pilotos:
        console.print(
            "[#a61b1b]No hay pilotos registrados "
            "en el sistema actualmente.[/#a61b1b]")
        return

    # Crear la tabla de Rich
    cabeceras = ["Sigla", "Nombre", "Nacionalidad", "Escudería", "Puntos"]
    alineaciones = ["center", "left", "left", "center", "center"]

    filas = []
    for sigla, datos in pilotos.items():
        fila = [
            sigla,
            datos["datos_personales"][0],
            datos["datos_personales"][1],
            datos["escuderia"],
            datos["puntos"]
        ]
        filas.append(fila)
    mostrar_tabla_generica(
        "Listado Oficial de Pilotos",
        cabeceras,
        filas,
        alineaciones)


def menu_pilotos():
    """
    Objetivo:
        Controlador pricnipal del flujo del submenú de gestion de pilotos.
        Mantiene al usuario en un bucle hasta que decida
        volver al menú principal.
    Parámetros: Ninguno.
    Retorna: None.
    """
    opciones_menu = [
        "1. Agregar Piloto",
        "2. Modificar Piloto",
        "3. Eliminar piloto",
        "4. Buscar Piloto",
        "5. Listar Pilotos",
        "0. Volver al Menú Principal"
    ]
    opcion = "-1"
    while opcion != "0":
        console.clear()

        opcion = mostrar_menu_generico("Gestión de Pilotos", opciones_menu)
        match opcion:
            case "1":
                console.clear()
                agregar_piloto()
            case "2":
                console.clear()
                modificar_piloto()
            case "3":
                console.clear()
                eliminar_piloto()
            case "4":
                console.clear()
                buscar_piloto()
            case "5":
                console.clear()
                listar_pilotos()
            case "0":
                console.print(
                    "[#a61b1b]--> Volviendo al menú principal...[/#a61b1b]")
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if opcion != "0":
            console.input(
                "\n[#a61b1b]Presione Enter para continuar...[/#a61b1b]")
