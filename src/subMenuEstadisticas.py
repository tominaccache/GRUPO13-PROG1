from rich.console import Console
from rich.panel import Panel
from utils import mostrar_tabla_generica  
from datos import pilotos

console = Console()

def mostrar_menu_estadisticas():
    texto_menu = (
        "[bold red]1. Piloto con puntos[/bold red]\n"
        "[bold red]2. Promedio de tiempos[/bold red]\n"
        "[bold red]3. Mejor Tiempo[/bold red]\n"
        "[bold red]4. Cantidad de Victorias[/bold red]\n"
        "[bold red]0. Salir[/bold red]\n"
    )
    panel = Panel(texto_menu, title="[bold red]Estadísticas[/bold red]", border_style="bold red", style="on white", padding=(1, 4), expand=False, width=49)
    console.print(panel)


def obtener_pilotos_con_puntos():
    """
    Objetivo: Filtrar y ordenar de mayor a menor los pilotos con unidades sumadas.
    """
    filtrados = filter(lambda item: item[1]["puntos"] > 0, pilotos.items())
    lista_con_puntos = []
    for sigla, info in filtrados:
        nombre = info["datos_personales"][0]
        escuderia = info["escuderia"]
        puntos = info["puntos"]
        lista_con_puntos.append([sigla, nombre, escuderia, puntos])
            
    lista_con_puntos.sort(key=lambda x: x[3], reverse=True)
    return lista_con_puntos


def menu_estadisticas():
    opcion = "-1"
    while opcion != "0":
        console.clear()
        mostrar_menu_estadisticas()
        opcion = console.input("\n[bold red]Seleccione una opción: [/bold red]")
        match opcion:
            case "1":
                ranking_puntos = obtener_pilotos_con_puntos()
                if len(ranking_puntos) > 0:
                    columnas = ["Pos", "Sigla", "Piloto", "Escudería", "Puntos"]
                    filas_tabla = [[pos] + pil for pos, pil in enumerate(ranking_puntos, start=1)]
                    mostrar_tabla_generica("Pilotos con Puntos", columnas, filas_tabla, ["center", "center", "left", "center", "center"])
                else:
                    console.print("[bold yellow]--> Actualmente ningún piloto ha sumado puntos.[/bold yellow]")
            case "2":
                console.print("[bold yellow]--> Opción 2: Promedio de tiempos (En desarrollo)...[/bold yellow]")
            case "3":
                console.print("[bold yellow]--> Opción 3: Mejor tiempo (En desarrollo)...[/bold yellow]")
            case "4":
                console.print("[bold yellow]--> Opción 4: Cantidad de victorias (En desarrollo)...[/bold yellow]")
            case "0":
                console.print("[bold red]--> Volviendo al menú principal. [/bold red]")
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")
                
        if opcion != "0":
            console.input("\n[bold red]--> Presione Enter para continuar. [/bold red]")