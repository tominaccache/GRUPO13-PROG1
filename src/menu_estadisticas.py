from rich.console import Console
from utils import mostrar_menu_generico, mostrar_tabla_generica, mostrar_panel_generico
from registrar_resultado import tiempo_a_segundos, validar_tiempo, clave_orden
import datos

console = Console()


def pilotos_con_puntos():
    pilotos_filtrados = [
        (sigla, info) for sigla, info in datos.pilotos.items()
        if info["puntos"] > 0
    ]
    if not pilotos_filtrados:
        console.print("[#a61b1b]Ningún piloto tiene puntos aún.[/#a61b1b]")
        return

    pilotos_ordenados = sorted(
        pilotos_filtrados,
        key=lambda item: item[1]["puntos"],
        reverse=True
    )

    cabeceras = ["Pos", "Sigla", "Piloto", "Puntos"]
    alineaciones = ["center", "center", "left", "right"]
    filas = []
    for pos, (sigla, info) in enumerate(pilotos_ordenados, 1):
        filas.append([pos, sigla, info["datos_personales"][0], info["puntos"]])

    mostrar_tabla_generica("Pilotos con Puntos",
                           cabeceras, filas, alineaciones)


def promedio_tiempos():

    if not datos.tiempos_carreras:
        console.print("[#a61b1b]No hay carreras registradas aún.[/#a61b1b]")
        return

    cabeceras = ["Sigla", "Piloto", "Carreras", "Promedio (s)"]
    alineaciones = ["center", "left", "center", "right"]
    filas = []

    for sigla, info in datos.pilotos.items():
        tiempos = []
        for resultados in datos.tiempos_carreras.values():
            if sigla in resultados:
                tiempo = resultados[sigla]
                if validar_tiempo(tiempo):
                    tiempos.append(tiempo_a_segundos(tiempo))

        if tiempos:
            promedio = sum(tiempos) / len(tiempos)
            filas.append([
                sigla,
                info["datos_personales"][0],
                len(tiempos),
                round(promedio, 3)
            ])

    if not filas:
        console.print("[#a61b1b]No hay tiempos válidos registrados.[/#a61b1b]")
        return

    filas.sort(key=lambda f: f[3])
    mostrar_tabla_generica(
        "Promedio de Tiempos por Piloto", cabeceras, filas, alineaciones
    )


def mejor_tiempo():

    if not datos.tiempos_carreras:
        console.print("[#a61b1b]No hay carreras registradas aún.[/#a61b1b]")
        return

    mejor = None
    mejor_sigla = None
    mejor_carrera = None

    for carrera, resultados in datos.tiempos_carreras.items():
        for sigla, tiempo in resultados.items():
            if validar_tiempo(tiempo):
                segundos = tiempo_a_segundos(tiempo)
                if mejor is None or segundos < mejor:
                    mejor = segundos
                    mejor_sigla = sigla
                    mejor_carrera = carrera
                    mejor_tiempo_str = tiempo

    if mejor is None:
        console.print("[#a61b1b]No hay tiempos válidos registrados.[/#a61b1b]")
        return

    if mejor_sigla and mejor_sigla in datos.pilotos:
        nombre = datos.pilotos[mejor_sigla]["datos_personales"][0]
    else:
        nombre = "Piloto Eliminado"

    info_mejor = (
        f"[#a61b1b]Piloto: {nombre} ({mejor_sigla})[/#a61b1b]"
        f"[#a61b1b]Carrera: {mejor_carrera}[/#a61b1b]"
        f"[#a61b1b]Tiempo: {mejor_tiempo_str}[/#a61b1b]"
    )
    mostrar_panel_generico("MEJOR TIEMPO DEL CAMPEONATO", info_mejor)


def cantidad_victorias():
    if not datos.tiempos_carreras:
        console.print("[#a61b1b]No hay carreras registradas aún.[/#a61b1b]")
        return

    victorias = {}
    for sigla in datos.pilotos:
        victorias[sigla] = 0

    for resultados in datos.tiempos_carreras.values():
        ordenados = sorted(resultados.items(), key=clave_orden)
        if ordenados:
            ganador = ordenados[0][0]
            if ganador in victorias:
                victorias[ganador] += 1

    cabeceras = ["Pos", "Sigla", "Piloto", "Victorias"]
    alineaciones = ["center", "center", "left", "center"]
    filas = []

    pilotos_con_victorias = sorted(
        victorias.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for pos, (sigla, wins) in enumerate(pilotos_con_victorias, 1):
        if wins > 0:
            nombre = datos.pilotos[sigla]["datos_personales"][0]
            filas.append([pos, sigla, nombre, wins])

    if not filas:
        console.print("[#a61b1b]Ningún piloto tiene victorias aún.[/#a61b1b]")
        return

    mostrar_tabla_generica(
        "Cantidad de Victorias", cabeceras, filas, alineaciones
    )


def menu_estadisticas():
    opcion = "-1"
    opciones_menu = [
        "1. Pilotos con Puntos",
        "2. Promedio de Tiempos",
        "3. Mejor Tiempo",
        "4. Cantidad de Victorias",
        "0. Volver al Menú Principal",
    ]
    while opcion != "0":
        console.clear()
        opcion = mostrar_menu_generico("Estadisticas", opciones_menu)
        match opcion:
            case "1":
                console.clear()
                pilotos_con_puntos()
            case "2":
                console.clear()
                promedio_tiempos()
            case "3":
                console.clear()
                mejor_tiempo()
            case "4":
                console.clear()
                cantidad_victorias()
            case "0":
                console.print(
                    "[#a61b1b]--> Volviendo al menú principal[/#a61b1b]")
            case _:
                console.print("[#a61b1b]--> Opción no válida[/#a61b1b]")
        if opcion != "0":
            console.input(
                "[#a61b1b]--> Presione Enter para continuar[/#a61b1b]")
