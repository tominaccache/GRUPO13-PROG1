import json
import os
from rich.console import Console
from utils import mostrar_menu_generico
import datos

console = Console()

ARCHIVO_JSON = "campeonato_f1.json"
ARCHIVO_REPORTE = "reporte_campeonato.txt"

def guardar_estado_sistema():
    console.print(f"\n[bold yellow]Guardando estado en '{ARCHIVO_JSON}' ...[/bold yellow]")

    estado = {
        "pilotos": datos.pilotos,
        "escuderias": datos.escuderias_, # Asegurate de que en datos.py se llame 'escuderias_' o modificalo a 'escuderias'
        "carreras": datos.carreras,
        "matriz_resultados": datos.matriz_resultados, # Corregido a plural para que coincida
        "tiempos_carreras": datos.tiempos_carreras # Asegurate que esto exista en datos.py
    }

    try:
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as file:
            json.dump(estado, file, ensure_ascii=False, indent=4)
        console.print("[bold green]Estado del sistema guardado exitosamente.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Ocurrio un error inesperado al guardar: {e}[/bold red]")


def exportar_reporte_txt():
    console.print(f"\n[bold yellow]Generando reporte en '{ARCHIVO_REPORTE}'...[/bold yellow]")
    try:
        pilotos_ordenados = sorted(datos.pilotos.items(), key=lambda item: item[1]["puntos"], reverse=True)
        escuderias_ordenadas = sorted(datos.escuderias_.items(), key=lambda item: item[1].get("puntos", 0), reverse=True)

        with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as file:
            file.write("=====================================================\n")
            file.write("       REPORTE OFICIAL - CAMPEONATO DE FÓRMULA 1     \n")
            file.write("=====================================================\n\n")

            file.write("------------- CLASIFICACIÓN DE PILOTOS -------------\n")
            file.write(f"{'Pos':<4} | {'Sigla':<5} | {'Nombre':<25} | {'Puntos':<6}\n")
            file.write("-" * 50 + "\n")

            for pos, (sigla, info) in enumerate(pilotos_ordenados, 1):
                nombre = info["datos_personales"][0]
                puntos = info["puntos"]
                file.write(f"{pos:<4} | {sigla:<5} | {nombre:<25} | {puntos:<6}\n")

            file.write("\n" + "=" * 50 + "\n\n")

            file.write("--- CLASIFICACION DE CONSTRUCTORES (ESCUDERÍAS) ---\n")
            file.write(f"{'Pos':<4} | {'Sigla':<5} | {'Nombre Escudería':<30} | {'Puntos':<6}\n")
            file.write("-" * 55 + "\n")

            for pos, (sigla, info) in enumerate(escuderias_ordenadas, 1):
                nombre = info.get("nombre", "N/A")
                puntos = info.get("puntos", 0)
                file.write(f"{pos:<4} | {sigla:<5} | {nombre:<30} | {puntos:<6}\n")

            file.write("\n\nReporte generado automaticamente por el sistema de Gestión F1.\n")
            console.print(f"[bold green]Reporte '{ARCHIVO_REPORTE}' exportado correctamente.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error: No se pudo escribir el reporte de texto. {e}[/bold red]")


def restaurar_sistema_json():
    if not os.path.exists(ARCHIVO_JSON):
        console.print(f"[bold red]Error: No se encontro el archivo de respaldo '{ARCHIVO_JSON}'.[/bold red]")
        return
    console.print(f"[bold yellow]Cargando datos desde '{ARCHIVO_JSON}'...[/bold yellow]")

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as file:
            estado = json.load(file)

        datos.pilotos = estado["pilotos"]
        datos.escuderias_ = estado["escuderias"]
        datos.carreras = estado["carreras"]
        datos.matriz_resultados = estado["matriz_resultados"]
        datos.tiempos_carreras = estado["tiempos_carreras"]

        console.print("[bold green]Sistema restaurado por completo en memoria con éxito.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error inesperado al restaurar: {e}[/bold red]")


def menu_guardar():
    opciones_menu = ["1. Guardar estado del sistema", "2. Exportar reporte", "0. Volver al menú principal"]
    while True:
        console.clear()
        op = mostrar_menu_generico("Guardar Datos", opciones_menu)
        match op:
            case "1": guardar_estado_sistema()
            case "2": exportar_reporte_txt()
            case "0": break
            case _: console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")
        if op in ("1", "2"):
            console.input("\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")


def menu_cargar():
    opciones_menu = ["1. Restaurar sistema", "0. Volver al menú principal"]
    while True:
        console.clear()
        op = mostrar_menu_generico("Cargar Datos", opciones_menu)
        match op:
            case "1": restaurar_sistema_json()
            case "0": break
            case _: console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")
        if op in ("1",):
            console.input("\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]")