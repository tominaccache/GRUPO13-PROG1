from functools import reduce
from rich.console import Console
from rich.panel import Panel
from utils import mostrar_tabla_generica  
from datos import pilotos, matriz_resultados, carreras

console = Console()

def mostrar_menu_estadisticas():
    texto_menu = (
        "[bold red]1. Piloto con puntos[/bold red]\n"
        "[bold red]2. Promedio de tiempos[/bold red]\n"
        "[bold red]3. Mejor tiempo[/bold red]\n"
        "[bold red]4. Cantidad de Victorias[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]\n"
    )
    panel = Panel(texto_menu, title="[bold red]Estadísticas[/bold red]", border_style="bold red", style="on white", padding=(1, 4), expand=False, width=49)
    console.print(panel)


def obtener_pilotos_con_puntos():
    filtrados = filter(lambda item: item[1]["puntos"] > 0, pilotos.items())
    lista_con_puntos = []
    for sigla, info in filtrados:
        nombre = info["datos_personales"][0]
        escuderia = info["escuderia"]
        puntos = info["puntos"]
        lista_con_puntos.append([sigla, nombre, escuderia, puntos])
    lista_con_puntos.sort(key=lambda x: x[3], reverse=True)
    return lista_con_puntos


def obtener_promedio_tiempos():
    siglas = list(pilotos.keys())
    promedios = []
    for fila in range(len(matriz_resultados)):
        tiempos_validos = list(filter(lambda t: t > 0, matriz_resultados[fila]))
        try:
            suma_tiempos = reduce(lambda a, b: a + b, tiempos_validos)
            promedio = suma_tiempos / len(tiempos_validos)
        except ZeroDivisionError:
            promedio = 0.0
        
        sigla = siglas[fila]
        nombre = pilotos[sigla]["datos_personales"][0]
        escuderia = pilotos[sigla]["escuderia"]
        if promedio > 0:
            promedios.append([sigla, nombre, escuderia, round(promedio, 3)])
            
    promedios.sort(key=lambda x: x[3])
    return promedios


def obtener_mejor_tiempo():
    """
    Objetivo: Buscar el valor mínimo absoluto mayor a 0 recorriendo la matriz completa. Retorna una Tupla.
    """
    siglas = list(pilotos.keys())
    mejor_tiempo = float('inf')
    tupla_mejor_resultado = ()

    for fila in range(len(matriz_resultados)):
        for col in range(len(matriz_resultados[fila])):
            tiempo = matriz_resultados[fila][col]
            if 0 < tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                piloto_nombre = pilotos[siglas[fila]]["datos_personales"][0]
                carrera_nombre = carreras[col]
                tupla_mejor_resultado = (piloto_nombre, carrera_nombre, mejor_tiempo)
                
    return tupla_mejor_resultado


def obtener_victorias():
    """
    Objetivo: Iterar sobre las columnas de la matriz para determinar ganadores de carreras individuales.
    """
    siglas = list(pilotos.keys())
    victorias_dict = {sigla: 0 for sigla in siglas}

    if len(matriz_resultados) > 0:
        for col in range(len(matriz_resultados[0])):
            mejor_tiempo_carrera = float('inf')
            indice_ganador = -1
            
            for fila in range(len(matriz_resultados)):
                tiempo = matriz_resultados[fila][col]
                if 0 < tiempo < mejor_tiempo_carrera:
                    mejor_tiempo_carrera = tiempo
                    indice_ganador = fila
            
            if indice_ganador != -1:
                sigla_ganadora = siglas[indice_ganador]
                victorias_dict[sigla_ganadora] += 1

    ganadores = list(filter(lambda item: item[1] > 0, victorias_dict.items()))
    lista_final = []
    for sigla, cant_victorias in ganadores:
        nombre = pilotos[sigla]["datos_personales"][0]
        lista_final.append([sigla, nombre, cant_victorias])
        
    lista_final.sort(key=lambda x: x[2], reverse=True)
    return lista_final


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
                promedios = obtener_promedio_tiempos()
                if len(promedios) > 0:
                    columnas = ["Pos", "Sigla", "Piloto", "Escudería", "Tiempo Promedio"]
                    filas_tabla = [[pos] + dato for pos, dato in enumerate(promedios, start=1)]
                    mostrar_tabla_generica("Promedio de Tiempos", columnas, filas_tabla, ["center", "center", "left", "center", "center"])
                else:
                    console.print("[bold yellow]--> No hay tiempos registrados en el campeonato aún.[/bold yellow]")
            case "3":
                resultado = obtener_mejor_tiempo()
                if len(resultado) > 0:
                    piloto, carrera, tiempo = resultado
                    filas = [[piloto, carrera, f"{tiempo} seg"]]
                    mostrar_tabla_generica("Mejor Tiempo del Campeonato", ["Piloto", "Gran Premio", "Tiempo"], filas, ["left", "center", "center"])
                else:
                    console.print("[bold yellow]--> No hay tiempos registrados en la matriz.[/bold yellow]")
            case "4":
                victorias = obtener_victorias()
                if len(victorias) > 0:
                    columnas = ["Pos", "Sigla", "Piloto", "Victorias"]
                    filas_tabla = [[pos] + dato for pos, dato in enumerate(victorias, start=1)]
                    mostrar_tabla_generica("Cantidad de Victorias", columnas, filas_tabla, ["center", "center", "left", "center"])
                else:
                    console.print("[bold yellow]--> No hay victorias registradas.[/bold yellow]")
            case "0":
                console.print("[bold red]--> Volviendo al menú principal. [/bold red]")
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")
                
        if opcion != "0":
            console.input("\n[bold red]--> Presione Enter para continuar. [/bold red]")