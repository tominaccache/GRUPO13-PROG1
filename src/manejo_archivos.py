import json
import os
from rich.console import Console
from utils import mostrar_menu_generico
import datos

console = Console()

# Nombres de archivos por defecto
ARCHIVO_JSON = "data/campeonato_f1.json"
ARCHIVO_REPORTE = "out/reporte_campeonato.txt"


def guardar_estado_sistema():
    """
    Objetivo: Serializar y guardar el estado actual de todas las estructuras
              del campeonato en formato JSON.
    Parámetros: Ninguno.
    Retorno: None. Escribe el archivo en disco.
    """
    directorio = os.path.dirname(ARCHIVO_JSON)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)

    console.print(
        f"\n[bold yellow]Guardando estado en '{ARCHIVO_JSON}' ..."
        "[/bold yellow]"
    )

    # Empaquetamos todas las estructuras globales en un unico diccionario
    estado = {
        "pilotos": datos.pilotos,
        "escuderias": datos.escuderias,
        "carreras": datos.carreras,
        "matriz_resultado": datos.matriz_resultados,
        "tiempos_carreras": datos.tiempos_carreras
    }

    try:
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as file:
            json.dump(estado, file, ensure_ascii=False, indent=4)
        console.print(
            "[bold green]Estado del sistema guardado "
            " exitosamente.[/bold green]"
        )

    except OSError as e:
        console.print(
            f"[bold red] Error critico de E/S: "
            f" No se pudo escribir el archivo."
            f" Detalle: {e}[/bold red]"
        )

    except Exception as e:
        console.print(
            f"[bold red]Ocurrio un error inesperado al guardar: "
            f" {e}[/bold red]"
        )


def calcular_ancho_nombre_pilotos():
    """
    Objetivo: Función auxiliar que calcula la longitud del nombre de piloto
              más largo para asegurar un espaciado perfecto en el reporte .txt.
    Entrada:
        - Ninguna.
    Salida:
        - ancho (int): Cantidad máxima de caracteres encontrada.
    """
    ancho = len("Nombre")

    for info in datos.pilotos.values():
        nombre = info["datos_personales"][0]
        ancho = max(ancho, len(nombre))

    return ancho


def calcular_ancho_nombre_escuderias():
    """
    Objetivo: Función auxiliar que calcula la longitud del nombre de escudería
              más largo para asegurar un alineamiento preciso en el reporte.
    Entrada:
        - Ninguna.
    Salida:
        - ancho (int): Cantidad máxima de caracteres encontrada.
    """
    ancho = len("Nombre Escuderia")

    for info in datos.escuderias.values():
        nombre = info["nombre"]
        ancho = max(ancho, len(nombre))

    return ancho


def exportar_reporte_txt():
    """
    Objetivo: Generar un reporte en texto plano (.txt) con la clasificación
              actual de pilotos y escuderías, ordenada por puntos.
    Parámetros: Ninguno.
    Retorno: None. Escribe el archivo en disco.
    """
    console.print(
        f"\n[bold yellow]Generando reporte en "
        f"'{ARCHIVO_REPORTE}...[/bold yellow]'")

    try:
        # Ordenamos pilotos de mayor a menor puntaje para el report
        pilotos_ordenados = sorted(
            datos.pilotos.items(),
            key=lambda item: item[1]["puntos"],
            reverse=True)

        # Ordenamos escuderias de mayor a menor puntaje
        escuderias_ordenadas = sorted(
            datos.escuderias.items(),
            key=lambda item: item[1]["puntos"],
            reverse=True
        )

        ANCHO_POS = 4
        ANCHO_SIGLA = 5
        ANCHO_PUNTOS = 6

        ANCHO_NOMBRE_PILOTO = calcular_ancho_nombre_pilotos()
        ANCHO_NOMBRE_ESCUDERIA = calcular_ancho_nombre_escuderias()

        separador_pilotos = (
            f"+{'-' * (ANCHO_POS + 2)}"
            f"+{'-' * (ANCHO_SIGLA + 2)}"
            f"+{'-' * (ANCHO_NOMBRE_PILOTO + 2)}"
            f"+{'-' * (ANCHO_PUNTOS + 2)}+\n"
        )

        separador_escuderias = (
            f"+{'-' * (ANCHO_POS + 2)}"
            f"+{'-' * (ANCHO_SIGLA + 2)}"
            f"+{'-' * (ANCHO_NOMBRE_ESCUDERIA + 2)}"
            f"+{'-' * (ANCHO_PUNTOS + 2)}+\n"
        )

        ancho_total = max(
            len(separador_pilotos.rstrip()),
            len(separador_escuderias.rstrip())
        )

        with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as file:
            # ENCABEZADO
            file.write("=" * ancho_total + "\n")
            file.write(
                "REPORTE OFICIAL - CAMPEONATO DE FÓRMULA 1"
                .center(ancho_total) + "\n"
            )
            file.write("=" * ancho_total + "\n\n")

            # PILOTOS
            file.write("CLASIFICACIÓN DE PILOTOS\n\n")

            file.write(separador_pilotos)

            file.write(
                f"| {'Pos':^{ANCHO_POS}} "
                f"| {'Sigla':^{ANCHO_SIGLA}} "
                f"| {'Nombre':<{ANCHO_NOMBRE_PILOTO}} "
                f"| {'Puntos':^{ANCHO_PUNTOS}} |\n"
            )

            file.write(separador_pilotos)

            pos_piloto = 1
            for sigla, info in pilotos_ordenados:

                nombre = info["datos_personales"][0]
                puntos = info["puntos"]

                file.write(
                    f"| {pos_piloto:>{ANCHO_POS}} "
                    f"| {sigla:^{ANCHO_SIGLA}} "
                    f"| {nombre:<{ANCHO_NOMBRE_PILOTO}} "
                    f"| {puntos:>{ANCHO_PUNTOS}} |\n"
                )

                pos_piloto += 1

            file.write(separador_pilotos)

            # CONSTRUCTORES
            file.write("\n")
            file.write("CLASIFICACION DE CONSTRUCTORES\n\n")

            file.write(separador_escuderias)

            file.write(
                f"| {'Pos':^{ANCHO_POS}} "
                f"| {'Sigla':^{ANCHO_SIGLA}} "
                f"| {'Nombre Escudería':<{ANCHO_NOMBRE_ESCUDERIA}} "
                f"| {'Puntos':^{ANCHO_PUNTOS}} |\n"
            )

            file.write(separador_escuderias)

            pos_escuderia = 1
            for sigla, info in escuderias_ordenadas:

                nombre = info["nombre"]
                puntos = info["puntos"]

                file.write(
                    f"| {pos_escuderia:>{ANCHO_POS}} "
                    f"| {sigla:^{ANCHO_SIGLA}} "
                    f"| {nombre:<{ANCHO_NOMBRE_ESCUDERIA}} "
                    f"| {puntos:>{ANCHO_PUNTOS}} |\n"
                )

                pos_escuderia += 1

            file.write(separador_escuderias)

            # PIE
            file.write("\n")
            file.write("=" * ancho_total + "\n")
            file.write(
                "Reporte generado automaticamente "
                "por el sistema de Gestión F1.\n"
            )

        console.print(
            f"[bold green]Reporte '{ARCHIVO_REPORTE}' "
            f"exportado correctamente.[/bold green]"
        )

    except OSError as e:
        console.print(
            f"[bold red]Error de E/S: "
            f" No se pudo escribir el reporte: {e}[/bold red]"
        )


def restaurar_sistema_json():
    """
    Objetivo: Leer el archivo JSON de respaldo, validar su estructura
              y restaurar el estado de las variables del módulo datos.py
    """
    if not os.path.exists(ARCHIVO_JSON):
        console.print(
            f"[bold red]Error: No se enontro el "
            f" archivo de respaldo '{ARCHIVO_JSON}'.[/bold red]"
        )
        return
    console.print(
        f"[bold yellow]Cargando datos desde '{ARCHIVO_JSON}'...[/bold yellow]")

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as file:
            estado = json.load(file)

        # Validacion de seguridad: verificar que las llaves principales existan
        llaves_requeridas = [
            "pilotos",
            "escuderias",
            "carreras",
            "matriz_resultados",
            "tiempos_carreras"
        ]
        if not all(llave in estado for llave in llaves_requeridas):
            console.print(
                "[bold red]Error: El archivo JSON no tiene "
                " el formato válido del campeonato.[/bold red]"
            )
            return

        # Mutamos el contenido de las estructuras
        # globales apuntando al modulo 'datos'
        datos.pilotos.clear()
        datos.pilotos.update(estado["pilotos"])

        datos.escuderias.clear()
        datos.escuderias.update(estado["escuderias"])

        datos.carreras.clear()
        datos.carreras.extend(estado["carreras"])

        datos.matriz_resultados.clear()
        datos.matriz_resultados.extend(estado["matriz_resultados"])

        datos.tiempos_carreras.clear()
        datos.tiempos_carreras.update(estado["tiempos_carreras"])

        console.print(
            "[bold green]Sistema restaurado "
            "por completo en memoria con éxito.[/bold green]"
        )

    except json.JSONDecodeError:
        console.print(
            "[bold red]Error: El archivo JSON "
            " está corrupto o tiene un formato ilegible.[/bold red]"
        )
    except PermissionError:
        console.print(
            "[bold red]Error de Permisos: "
            " No se puede leer el archivo de respaldo.[/bold red]"
        )
    except Exception as e:
        console.print(
            f"[bold red]Error inesperado al restaurar: {e}[/bold red]")


def menu_guardar():
    """
    Objetivo: Controlador del submenú para la exportación y persistencia de datos.
    Entrada:
        - Ninguna (Interacción por consola).
    Salida:
        - None.
    """
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
                guardar_estado_sistema()
            case "2":
                exportar_reporte_txt()
            case "0":
                break
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if op in ("1", "2"):
            console.input(
                "\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")


def menu_cargar():
    """
    Objetivo: Controlador del submenú para la restauración del sistema desde JSON.
    Entrada:
        - Ninguna (Interacción por consola).
    Salida:
        - None.
    """
    opciones_menu = ["1. Restaurar sistema", "0. Volver al menú principal"]
    while True:
        console.clear()
        op = mostrar_menu_generico("Cargar Datos", opciones_menu)

        match op:
            case "1":
                restaurar_sistema_json()
            case "0":
                break
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if op in ("1",):
            console.input(
                "\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")
