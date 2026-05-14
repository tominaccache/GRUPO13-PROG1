from rich.console import Console
import re
from utils import mostrar_menu_generico, mostrar_tabla_generica
from datos import (
    pilotos,
    escuderias,
    carreras,
    puntos_por_posicion,
    matriz_resultados,
    tiempos_carreras,
)

console = Console()


# Funciones Auxiliares
def tiempo_a_segundos(tiempo):
    """
    Objetivo: Convertir un tiempo en formato HH:MM:SS.mmm a segundos.
    Entrada: tiempo (string) en formato HH:MM:SS.mmm
    Salida: tiempo en segundos (float)
    """
    hora, minutos, segundos = tiempo.split(":")
    return int(hora) * 3600 + int(minutos) * 60 + float(segundos)


def validar_tiempo(tiempo):
    """
    Objetivo: Validar que el tiempo ingresado tenga el formato correcto.
    Entrada: tiempo (string)
    Salida: True si es correcto, False si no lo es
    """
    return bool(re.fullmatch(r"\d{2}:\d{2}:\d{2}\.\d{3}", tiempo))


def validar_vuelta_perdida(tiempo):
    """
    Objetivo: Validar que el indicador de vuelta perdida tenga el formato correcto.
    Entrada: tiempo (string)
    Salida: True si es válido, False si no lo es
    """
    return bool(re.fullmatch(r"\+\d+", tiempo))


def clave_orden(item):
    """
    Objetivo: Definir el criterio de ordenamiento de los tiempos.
    Entrada: item (tupla con sigla y tiempo)
    Salida: Tupla de prioridad para la función sorted()
    """
    tiempo = item[1]
    if tiempo == "DNF":
        return (2, 0)
    elif validar_vuelta_perdida(tiempo):
        vueltas = int(tiempo[1:])
        return (1, vueltas)
    else:
        return (0, tiempo_a_segundos(tiempo))


def revertir_resultados_carrera(carrera_seleccionada):
    """
    Objetivo: Función auxiliar para descontar puntos y limpiar la matriz.
    Se utiliza tanto al eliminar como al modificar una carrera.
    """
    # Logica de reversion (Descontar puntos y limpiar matriz)
    resultados_viejos = sorted(
        tiempos_carreras[carrera_seleccionada].items(), key=clave_orden
    )
    indice_carrera = carreras.index(carrera_seleccionada)
    indice_carrera_matriz = indice_carrera + 1

    pos = 0
    for item in resultados_viejos:
        sigla = item[0]
        tiempo = item[1]

        # Solo funciona si el piloto aún existe en el sistema
        if sigla in pilotos:
            # Descontar puntos (si sumo puntos en la carrera)
            if pos < len(puntos_por_posicion) and validar_tiempo(tiempo):
                puntos_a_restar = puntos_por_posicion[pos]
                pilotos[sigla]["puntos"] -= puntos_a_restar

                escuderia_actual = pilotos[sigla]["escuderia"]
                if escuderia_actual in escuderias:
                    escuderias[escuderia_actual]["puntos"] -= puntos_a_restar

            # Vaciar el tiempo de la matriz
            for fila in matriz_resultados:
                if fila[0] == sigla:
                    fila[indice_carrera_matriz] = ""
                    break

        pos += 1

    # Eliminar el registro principal
    del tiempos_carreras[carrera_seleccionada]


def asignar_puntos_y_guardar(carrera_seleccionada, tiempos_carrera_actual):
    """
    Objetivo: Ordenar tiempos, asignar puntos a pilotos y escuderías,
              actualizar la matriz y guardar en tiempos_carreras.
    Entrada: carrera_seleccionada (string), tiempos_carrera_actual (dict)
    Retorno: None. Modifica pilotos, escuderias, matriz_resultados y tiempos_carreras.
    """
    indice_carrera = carreras.index(carrera_seleccionada)
    # +1 Porque la columna 0 es la sigla del piloto
    indice_carrera_matriz = indice_carrera + 1
    resultados_ordenados = sorted(
        tiempos_carrera_actual.items(),
        key=clave_orden)

    pos = 0
    for item in resultados_ordenados:
        sigla = item[0]
        tiempo = item[1]

        # Guardado seguro en matriz: buscamos la fila por sigla
        for fila in matriz_resultados:
            if fila[0] == sigla:
                fila[indice_carrera_matriz] = tiempo
                break

        if pos < len(puntos_por_posicion) and validar_tiempo(tiempo):
            puntos = puntos_por_posicion[pos]
        else:
            puntos = 0

        # Sumamos puntos al piloto
        pilotos[sigla]["puntos"] += puntos

        # Sumamos a la escuderia solo si existe en el sistema
        escuderia_actual = pilotos[sigla]["escuderia"]
        if escuderia_actual in escuderias:
            escuderias[escuderia_actual]["puntos"] += puntos

        pos += 1

    tiempos_carreras[carrera_seleccionada] = tiempos_carrera_actual


def cargar_tiempos_manual(siglas_pilotos):
    tiempos_carrera = {}
    console.print("\n[#a61b1b]Ingrese los tiempos:[/#a61b1b]")

    console.print("[#a61b1b]Formato: HH:MM:SS.mmm | +N | DNF[/#a61b1b]\n")

    for sigla in siglas_pilotos:
        nombre = pilotos[sigla]["datos_personales"][0]
        while True:
            tiempo = (
                console.input(f"[#a61b1b]{sigla} - {nombre}: [/#a61b1b]")
                .strip()
                .upper()
            )
            if (
                validar_tiempo(tiempo)
                or validar_vuelta_perdida(tiempo)
                or tiempo == "DNF"
            ):
                tiempos_carrera[sigla] = tiempo
                break
            else:
                console.print(
                    "[#a61b1b]Error: Formato inválido. Use HH:MM:SS.mmm, +N, DNF[/#a61b1b]"
                )
    return tiempos_carrera


def cargar_tiempos_archivo():
    console.print("[#a61b1b] En produccion[/#a61b1b]")
    return {}


def registrar_tiempos():
    console.print("[#a61b1b]Registrar tiempos de carrera[/#a61b1b]\n")

    # Filtrar carreras sin resultados
    carreras_disponibles = [c for c in carreras if c not in tiempos_carreras]

    if not carreras_disponibles:
        console.print(
            "[#a61b1b]No hay carreras disponibles para registrar[/#a61b1b]")
        return

    i = 1
    # Mostramos las carreras disponibles
    for carrera in carreras_disponibles:
        console.print(f"[#a61b1b]{i}. {carrera}[/#a61b1b]")
        i += 1

    # Seleccionar carrera
    try:
        opcion = int(
            console.input("\n[#a61b1b]Seleccione una carrera: [/#a61b1b]"))
        if opcion < 1 or opcion > len(carreras_disponibles):
            console.print("[#a61b1b]Error: Opción no válida.[/#a61b1b]")
            return
    except ValueError:
        console.print("[#a61b1b]Error: Ingrese un número válido[/#a61b1b].")
        return
    console.clear()
    carrera_seleccionada = carreras_disponibles[opcion - 1]

    # Seleccionar el modo de carga
    opciones_menu = ["1. Carga Manul", "2. Cargar desde Archivo"]
    modo = mostrar_menu_generico("Modo de Carga", opciones_menu)

    # Pedir los tiempos para cada piloto
    siglas_pilotos = list(pilotos.keys())

    if modo == "1":
        tiempos_carrera_actual = cargar_tiempos_manual(siglas_pilotos)

    elif modo == "2":
        tiempos_carrera_actual = cargar_tiempos_archivo()
    else:
        console.print("[#a61b1b]Opcion Inválida[/#a61b1b]")
        return

    # Validar catidad de pilotos
    if len(tiempos_carrera_actual) != len(pilotos):
        console.print("[#a61b1b]Faltan pilotos cargados[/#a61b1b]")
        return

    asignar_puntos_y_guardar(carrera_seleccionada, tiempos_carrera_actual)
    console.print(
        f"\n[#a61b1b]Tiempos de {carrera_seleccionada} registrados correctamente.[/#a61b1b]"
    )


def ver_resultados():
    """
    Objetivo: Mostrar la tabla de resultados finales de un Gran Premio específico.
    """
    console.print("[#a61b1b]Ver resultados de Carrera[/#a61b1b] ")
    if not tiempos_carreras:
        console.print(
            "[#a61b1b]No hay resultados registrados en el sistema actual.[/#a61b1b]"
        )
        return

    # Listar carreras que ya tienen tiempos cargados
    carreras_disponibles = [c for c in carreras if c in tiempos_carreras]

    opciones_numeradas = []
    for i in range(len(carreras_disponibles)):
        opciones_numeradas.append(f"{i+1}. {carreras_disponibles[i]}")

    opcion = mostrar_menu_generico(
        "Seleccione una Carrera",
        opciones_numeradas)

    # Seleccionar carrera
    try:
        opcion_int = int(opcion)
        if opcion_int < 1 or opcion_int > len(carreras_disponibles):
            console.print("[#a61b1b]Error: Opción no válida[/#a61b1b]")
            return
    except ValueError:
        console.print("[#a61b1b]Error: Ingrese un número válido.[/#a61b1b]")
        return

    carrera_seleccionada = carreras_disponibles[opcion_int - 1]
    resultados_desordenados = tiempos_carreras[carrera_seleccionada]

    # Ordenar el Diccionario
    resultados_ordenados = sorted(
        resultados_desordenados.items(),
        key=clave_orden)

    # Definimos cabeceras y alineacion para la tabla generica
    cabeceras = ["Pos", "Piloto", "Tiempo/Estado", "Pts"]
    aliniaciones = ["center", "left", "right", "center"]
    filas = []

    # Armamos las filas
    pos = 1
    for sigla, tiempo in resultados_ordenados:
        # Mostramos los puntos que ganó en esa carrera
        if pos <= len(puntos_por_posicion) and validar_tiempo(tiempo):
            puntos = puntos_por_posicion[pos - 1]
        else:
            puntos = 0

        nombre = pilotos[sigla]["datos_personales"][0]

        # Guardamos la fila en la lista
        fila = [pos, f"{nombre} ({sigla})", tiempo, puntos]
        filas.append(fila)

        pos += 1

    mostrar_tabla_generica(
        f"Resultados Oficiales - {carrera_seleccionada}",
        cabeceras,
        filas,
        aliniaciones)


def modificar_resultados():
    """
    Objetivo: Corregir tiempos de una carrera, reasignando puntos correctamente
    """
    if not tiempos_carreras:
        console.print(
            "[#a61b1b]No hay resultados registrados para modificar[/#a61b1b]")
        return

    carreras_disponibles = [c for c in carreras if c in tiempos_carreras]

    opciones_numeradas = []

    for i in range(len(carreras_disponibles)):
        opciones_numeradas.append(f"{i+1}. {carreras_disponibles[i]}")
    opcion = mostrar_menu_generico(
        "Seleccione la carrera a modificar", opciones_numeradas
    )

    try:
        opcion_int = int(opcion)
        if opcion_int < 1 or opcion_int > len(carreras_disponibles):
            console.print("[#a61b1b]Error: Opción no válida.[/#a61b1b]")
            return
    except ValueError:
        console.print("[#a61b1b]Error: Ingrese un número válido.[/#a61b1b]")
        return

    carrera_seleccionada = carreras_disponibles[opcion_int - 1]

    # Borrar los DATOS VIEJOS usando la función auxiliar
    revertir_resultados_carrera(carrera_seleccionada)
    tiempos_carrera_actual = cargar_tiempos_manual(list(pilotos.keys()))
    asignar_puntos_y_guardar(carrera_seleccionada, tiempos_carrera_actual)
    console.print(
        f"[#a61b1b]Resultados de {carrera_seleccionada} modificados correctamente.[/#a61b1b]"
    )


def eliminar_resultados():
    """Objetivo: Eliminar los resultados de un carrera y descontar puntos"""
    console.print("[#a61b1b]Eliminar Resultados de Carrera[/#a61b1b]")

    if not tiempos_carreras:
        console.print(
            "[#a61b1b]No hay resultados registrados para eliminar.[/#a61b1b]")
        return
    carreras_disponibles = [c for c in carreras if c in tiempos_carreras]
    opcion = mostrar_menu_generico(
        "Seleccione la carrera a eliminar", carreras_disponibles
    )
    try:
        opcion_int = int(opcion)
        if opcion_int < 1 or opcion_int > len(carreras_disponibles):
            console.print("[#a61b1b]Error: Opción no válida.[/#a61b1b]")
            return
    except ValueError:
        console.print("[#a61b1b]Error: Ingrese un número válido.[/#a61b1b]")
        return

    carrera_seleccionada = carreras_disponibles[opcion_int - 1]

    # Confirmacion de seguridad
    confirmacion = console.input(
        f"[#a61b1b]¿Está seguro que desea eliminar {carrera_seleccionada}? (S/N): [/#a61b1b]"
    ).upper()
    if confirmacion != "S":
        console.print("[#a61b1b]Operacion cancelada.[/#a61b1b]")
        return

    revertir_resultados_carrera(carrera_seleccionada)
    console.print(
        f"[bold green] Resultados de {carrera_seleccionada} eliminados exitosamente.[/bold green]"
    )


def agregar_carrera():
    """
    Objetivo: Agregar un nuevo Gran Premio al calendario de la temporada,
              garantizando que no existan circuitos duplicados mediante conjuntos,
              y extendiendo la matriz de resultados con una nueva columna vacía.
    Parámetros: Ninguno (los datos se ingresan por consola).
    Retorno: None. Modifica las listas globales 'carreras' y 'matriz_resultados'.
    """
    console.print("[#a61b1b]Agregar Nueva Carrera al Calendario[#a61b1b]\n")

    nueva_carrera = console.input(
        "[#a61b1b]Ingrese el Nombre del Nuevo Gran Premio: [/#a61b1b]\n").strip().title()

    conjunto_carreras = set(carreras)

    if nueva_carrera in conjunto_carreras:
        console.print(
            f"[#a61b1b]Error: El Gran Premio '{nueva_carrera}' "
            f"ya existe en el calendario[/#a61b1b]"
        )
        return

    # Agregar la nueva carrera al calendario oficial
    carreras.append(nueva_carrera)

    # Extender cada fila de la matriz con una celda vacia para la nueva
    # carrera
    for fila in matriz_resultados:
        fila.append("")

    console.print(f"[bold green] Gran Premio '{nueva_carrera}' agregada"
                  f"correctamente. Total de carreras: {len(carreras)}. [/bold green]"
                  )


def menu_resultados():
    continuar_programa = True

    opciones_submenu = [
        "1. Registrar tiempos de carrera",
        "2. Ver resultados",
        "3. Modificar resultados",
        "4. Eliminar resultados",
        "5. Agregar carrera nueva",
        "0. Volver al menú principal",
    ]

    while continuar_programa:
        console.clear()
        opcion = mostrar_menu_generico(
            "Registro de Resultados de Gran Premio", opciones_submenu
        )
        match opcion:
            case "1":
                registrar_tiempos()
            case "2":
                ver_resultados()
            case "3":
                modificar_resultados()
            case "4":
                eliminar_resultados()
            case "0":
                console.print(
                    "[#a61b1b]--> Volviendo al menú principal...[/#a61b1b]")
                continuar_programa = False
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")
        if opcion != "0":
            console.input(
                "\n[#a61b1b]Presione enter para continuar.[/#a61b1b]")
