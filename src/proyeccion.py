from datos import pilotos, puntos_por_posicion
from rich.console import Console
from rich.panel import Panel
from utils import mostrar_menu_generico

# Inicializamos la consola
console = Console()


def obtener_lider(pilotos):
    lider = None
    max_puntos = -1

    for sigla, datos in pilotos.items():
        if datos["puntos"] > max_puntos:
            max_puntos = datos["puntos"]
            lider = sigla

    return lider, max_puntos


def analizar_piloto():
    sigla = input("Ingrese sigla del piloto: ").upper()

    if sigla not in pilotos:
        print("Piloto no encontrado")
        return

    carreras_restantes = int(input("Carreras restantes: "))

    lider, puntos_lider = obtener_lider(pilotos)
    puntos_piloto = pilotos[sigla]["puntos"]

    max_por_carrera = max(puntos_por_posicion)

    maximo_posible = puntos_piloto + (carreras_restantes * max_por_carrera)
    resultado = (
        f"[#a61b1b]Lider: {lider} ({puntos_lider} pts)[/#a61b1b]\n",
        f"[#a61b1b]{sigla}: {puntos_piloto} pts [/#a61b1b]\n"
    )
    if maximo_posible >= puntos_lider:
        resultado += "[bold green]Sigue en competencia[/bold green]"
    else:
        resultado += "[#a61b1b]Ya no puede alcanzar al piloto lider[/#a61b1b]"
    panel = Panel(
        resultado,
        title="[#a61b1b]Resultado Proyección[/#a61b1b]",
        border_style="#a61b1b",
        style="on white",
        padding=(1, 4),
        expand=False,
        width=70,
    )
    console.print(panel)


def submenu_proyeccion():
    opcion = "-1"
    opciones_menu = [
        "1. Puntos Maximos Posibles",
        "0. Volver al Menú Principal"]
    while opcion != "0":

        console.clear()
        opcion = mostrar_menu_generico(
            "Proyeccion del Campeonato", opciones_menu)

        if opcion == "1":
            analizar_piloto()
        elif opcion == "0":
            console.print(
                "[#a61b1b]--> Volviendo al menú principal...[/#a61b1b]")
        else:
            console.print("[#a61b1b]Opcion invalida[/#a61b1b]")
        if opcion != "0":
            console.input(
                "[#a61b1b]--> Presione enter para continuar.[/#a61b1b]")
