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
            console.input("\nPresione Enter para volver...")

        elif op == "0":
            break

