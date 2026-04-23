from datos import pilotos, puntos_por_posicion
from rich.console import Console
from rich.panel import Panel

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


def mostrar_menu_proyeccion():
    """
    Objetivo: Mostrar el submenu de Proyeccion del Campeonato
    Salida: Retorna la opcion ingresada por el usuario como un string
    """
    texto_menu = (
        "[bold red]1. Puntos Maximos Posibles[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]\n"
    )
    panel = Panel(
        texto_menu,
        title="[bold red] Proyeccion del Campeonato[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=True,
        width=49,
    )
    console.print(panel)


def submenu_proyeccion():
    opcion = "-1"
    while opcion != "0":
        console.clear()
        mostrar_menu_proyeccion()
        opcion = console.input("[bold red] Seleccione una opción: [/bold red]")

        if opcion == "1":
            # analizar_piloto()
            console.print("[bold red]--> Posibilidades de alcanzar al lider (proximamente)[/bold red]")
        elif opcion == "0":
            console.print("[bold red]--> Volviendo al menú principal...[/bold red]")
        else:
            console.print("[bold red]Opcion invalida[/bold red]")
