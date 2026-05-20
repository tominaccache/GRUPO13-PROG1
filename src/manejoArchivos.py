import json
import os
from rich.console import Console
from utils import mostrar_menu_generico
import datos

console = Console()

# Nombres de archivos por defecto
ARCHIVO_JSON = "campeonato_f1.json"
ARCHIVO_REPORTE = "reporte_campeonato.txt"


def guardar_estado_sistema():
    """
    Objetivo: Serializar y guardar el estado actual de todas las estructuras
              del campeonato
    """
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
    except IOError:
        console.print(
            "[bold red] Error critico de E/S: "
            " No se pudo escribir el archivo.[/bold red]"
        )
    except Exception as e:
        console.print(
            f"[bold red]Ocurrio un error inesperado al guardar: "
            f" {e}[/bold red]"
        )


def exportar_reporte_txt():
    """
    Objetivo: Generar un reporte en texto plano (.txt) con el estado actual
              del campeonato (Clasificacion rapida de pilotos y escuderias).
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

        with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as file:
            file.write(
                "=====================================================\n")
            file.write(
                "       REPORTE OFICIAL - CAMPEONATO DE FÓRMULA 1     \n")
            file.write(
                "=====================================================\n\n")

            file.write("------------- CLASIFICACIÓN DE PILOTOS "
                       "-------------\n"
                       )
            file.write(
                f"{'pos':<4} | {'sigla': <5} | "
                " {'nombre':<25} | {'puntos':<6}\n"
            )
            file.write("-"*50 + "\n")

            pos_piloto = 1
            for sigla, info in pilotos_ordenados:
                nombre = info["datos_personales"][0]
                puntos = info["puntos"]
                file.write(
                    f"{pos_piloto:<4} | {sigla:<5} | "
                    " {nombre:<25} | {puntos:<6}\n"
                )
                pos_piloto += 1

            file.write("\n"+"="*50+"\n\n")

            file.write("--- CLASIFICACION DE CONSTRUCTORES (ESCUDERÍAS) ---\n")
            file.write(
                f"{'Pos':<4} | {'Sigla':<5} | "
                " {'Nombre Escudería':<30} | {'Puntos':<6}\n"
            )
            file.write("-" * 55 + "\n")

            pos_escuderia = 1
            for sigla, info in escuderias_ordenadas:
                nombre = info["nombre"]
                puntos = info["puntos"]
                file.write(
                    f"{pos_escuderia:<4} | {sigla:<5} | "
                    f" {nombre:<30} | {puntos:<6}\n"
                )
                pos_escuderia += 1

            file.write(
                "\n\nReporte generado automaticamente "
                " por el sistema de Gestión F1.\n"
            )

            console.print(
                F"[bold green]Reporte '{ARCHIVO_REPORTE}' "
                "exportado correctamente.[/bold green]"
            )
    except IOError:
        console.print(
            "[bold red]Error de E/S: "
            " No se pudo escribir el reporte de texto.[/bold red]"
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
            "matriz_resultado",
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
        datos.pilotos = estado["pilotos"]
        datos.escuderias = estado["escuderias"]
        datos.carreras = estado["carreras"]
        datos.matriz_resultados = estado["matriz_resultados"]
        datos.tiempos_carreras = estado["tiempos_carreras"]

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
