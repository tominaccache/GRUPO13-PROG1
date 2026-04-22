from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def limpiar_consola():
    console.clear()


def menu_tabla_posiciones():
    while True:
        limpiar_consola()
        texto_menu = (
            "[bold red]1. Ver Tabla de Pilotos[/bold red]\n"
            "[bold red]2. Ver Tabla de Escuderías[/bold red]\n"
            "[bold red]3. Exportar Clasificación[/bold red]\n"
            "[bold red]0. Volver al menú principal[/bold red]"
        )

        panel = Panel(
            texto_menu,
            title="[bold red] Tabla de Posiciones 📊 [/bold red]",
            border_style="bold red",
            style="on white",
            padding=(1, 4),
            expand=False,
        )
        console.print(panel)

        op = console.input("\n[bold red]Seleccione una opción: [/bold red]")
        if op == "1":
            limpiar_consola()
            mostrar_tabla_ejemplo()
            console.input("\nPresione Enter para volver...")

        elif op == "0":
            break


def mostrar_tabla_ejemplo():
    tabla = Table(
        title="Clasificación Actual F1", header_style="bold red", border_style="red"
    )

    tabla.add_column("Pos", justify="center")
    tabla.add_column("Piloto")
    tabla.add_column("Escudería")
    tabla.add_column("Puntos", justify="right")

    tabla.add_row("1", "Max Verstappen", "Red Bull", "350")
    tabla.add_row("2", "Lando Norris", "McLaren", "280")
    tabla.add_row("3", "Charles Leclerc", "Ferrari", "275")

    console.print(tabla)
