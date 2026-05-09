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
        f"[bold red]Lider: [/bold red]{lider} ({puntos_lider} pts)\n"
        f"[bold red]{sigla}:[/bold red] {puntos_piloto} pts\n"
    )
    if maximo_posible >= puntos_lider:
        resultado += "[bold green]Sigue en competencia[/bold green]"
    else:
        resultado += "[bold red]Ya no puede alcanzar al piloto lider[/bold red]"
    panel = Panel(
        resultado,
        title="[bold red]Resultado Proyección[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=False,
        width=70,
    )
    console.print(panel)


def submenu_proyeccion():
    opcion = "-1"
    opciones_menu = ["1. Puntos Maximos Posibles", "0. Volver al Menú Principal"]
    while opcion != "0":

        console.clear()
        opcion = mostrar_menu_generico("Proyeccion del Campeonato", opciones_menu)

        if opcion == "1":
            analizar_piloto()
        elif opcion == "0":
            console.print("[bold red]--> Volviendo al menú principal...[/bold red]")
        else:
            console.print("[bold red]Opcion invalida[/bold red]")
        if opcion != "0":
            console.input("[bold red]--> Presione enter para continuar.[/bold red]")
