from datos import pilotos, puntos_por_posicion, carreras, tiempos_carreras
from rich.console import Console
from utils import mostrar_menu_generico, mostrar_panel_generico

# Inicializamos la consola
console = Console()


def obtener_lider(pilotos):
    """
    Objetivo:
        Recorre el diccionario de pilotos para encontrar al líder actual
        del campeonato en base a sus puntos acumulados.
    Entrada:
        - pilotos (dict): El diccionario global de pilotos.
    Salida:
        - lider (str): Sigla del piloto puntero en la tabla.
        - max_puntos (int): Cantidad de puntos del lider.
    """
    lider = None
    max_puntos = -1

    for sigla, datos in pilotos.items():
        if datos["puntos"] > max_puntos:
            max_puntos = datos["puntos"]
            lider = sigla

    return lider, max_puntos


def puede_alcanzar_lider_recursivo(puntos_actuales, carreras_restantes, puntos_lider, max_por_carrera):
    """
    Objetivo:
        Calcula mediante recursividad si un piloto tiene posibilidades
        matemáticas de alcanzar o superar al líder del campeonato,
        cortando la ejecución si la diferencia es insalvable.
    Entrada:
        - puntos_actuales (int): Puntos del piloto a analizar.
        - carreras_restantes (int): Cantidad de carreras faltantes en la temporada.
        - puntos_lider (int): Puntos actuales del líder del campeonato.
        - max_por_carrera (int): Puntos máximos otorgados en una carrera.
    Salida:
        - True (bool): Si es matemáticamente posible que alcance al líder.
        - False (bool): Si ya está matemáticamente eliminado.
    """
    # CASO BASE 1: Matemáticamente insalvable
    if ((puntos_actuales + (carreras_restantes * max_por_carrera)) < puntos_lider):
        return False

    # CASO BASE 2: Ya alcanzo o supero al lider
    if puntos_actuales >= puntos_lider:
        return True

    # CASO BASE 3: No hay mas carreras y no lo alcanzó
    if carreras_restantes == 0:
        return False

    # Llamada recursiva: Simulamos que pasa 1 carrera y el piloto saca el puntaje máximo
    return puede_alcanzar_lider_recursivo(
        puntos_actuales + max_por_carrera,
        carreras_restantes - 1,
        puntos_lider,
        max_por_carrera
    )


def analizar_piloto(sigla):
    """
    Objetivo:
        Calcula automáticamente las carreras restantes en el calendario e
        invoca al motor recursivo para determinar las posibilidades de campeonato
        de la sigla ingresada, imprimiendo el resultado en un panel.
    Entrada:
        - sigla (str): La sigla validada del piloto a analizar.
    Salida:
        - None (Imprime el panel de resultados por consola).
    """
    carreras_totales = len(carreras)
    carreras_disputadas = len(tiempos_carreras)
    carreras_restantes = carreras_totales - carreras_disputadas

    if carreras_restantes == 0:
        console.print(
            "\n[bold yellow]El campeonato ha finalizado. Ya no quedan carreras por disputar.[/bold yellow]")

    lider, puntos_lider = obtener_lider(pilotos)
    puntos_piloto = pilotos[sigla]["puntos"]
    max_por_carrera = max(puntos_por_posicion)

    sigue_en_carrera = puede_alcanzar_lider_recursivo(
        puntos_piloto,
        carreras_restantes,
        puntos_lider,
        max_por_carrera
    )

    resultado = (
        f"Líder del Campeonato: [bold]{lider}[/bold] ({puntos_lider} pts)\n"
        f"Piloto Analizado: [bold]{sigla}[/bold] ({puntos_piloto} pts)\n"
        f"Carreras Restantes: {carreras_restantes} (Máx {max_por_carrera} pts c/u)\n\n"
    )

    if sigue_en_carrera:
        resultado += "[bold green]✅ MATEMÁTICAMENTE POSIBLE:[/bold green] El piloto aún tiene chances de pelear el campeonato."
    else:
        resultado += "[bold red]❌ MATEMÁTICAMENTE ELIMINADO:[/bold red] Ya no puede alcanzar al líder."

    mostrar_panel_generico("RESULTADO DE LA PROYECCIÓN", resultado)


def submenu_proyeccion():
    """
    Objetivo:
        Controlador principal del flujo del súbmenu de Proyección de Campeonato.
        Maneja los inputs del usuario de forma aislada.
    """

    opcion = "-1"
    opciones_menu = [
        "1. Calcular Proyección de Campeonato",
        "0. Volver al Menú Principal"]

    while opcion != "0":

        console.clear()
        opcion = mostrar_menu_generico(
            "Proyeccion del Campeonato", opciones_menu
        )

        if opcion == "1":
            console.clear()
            console.print(
                "[#a61b1b]Analizador de Proyección de Campeonato[/#a61b1b]\n")
            sigla = console.input(
                "[#a61b1b]Ingrese la sigla del piloto a analizar: [/#a61b1b]").upper()

            # Validación realizada en la capa del menú
            if sigla not in pilotos:
                console.print(
                    "[bold red]Error: Piloto no encontrado en el sistema.[/bold red]")
            else:

                analizar_piloto(sigla)

        elif opcion == "0":
            pass
        else:
            console.print("[#a61b1b]Opcion invalida[/#a61b1b]")

        if opcion != "0":
            console.input(
                "[#a61b1b]--> Presione enter para continuar.[/#a61b1b]")
