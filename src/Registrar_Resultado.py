from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def limpiar_consola():
    console.clear()


def mostrar_menu_resultados():
    """
    Objetivo: Mostrar el submenú de Registro de Resultados.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    
    texto_menu = (
        "[bold red]1. Registrar tiempos de carrera[/bold red]\n"
        "[bold red]2. Ver resultados[/bold red]\n"
        "[bold red]3. Modificar resultados[/bold red]\n"
        "[bold red]4. Eliminar resultados[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]"
    )
    
    panel = Panel(
        texto_menu, 
        title="[bold red] Registro de Resultados de Gran Premio[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4), 
        expand=False,
        width=49
    )
    console.print(panel)

    return console.input("\n[bold red]Seleccione una opción: [/bold red]")

def menu_resultados():
    continuar_programa = True
    
    while continuar_programa:
        limpiar_consola()
        opcion = mostrar_menu_resultados()
        match opcion:
            case "1":
                console.print("[bold red]--> Registrar tiempos en HH:MM:SS.mm (proximamente)[/bold red]")
            case "2":
                console.print("[bold red]--> Ver resultados (próximamente)[/bold red]")
            case "3":
                console.print("[bold red]--> Modificar resultados (próximamente)[/bold red]")
            case "4":
                console.print("[bold red]--> Eliminar resultados (próximamente)[/bold red]")
            case "0":
                console.print("[bold red]--> Volviendo al menú principal...[/bold red]")
                continuar_programa = False
            case _: 
                 console.print("[bold red]--> Opción no válida.[/bold red]")
        if opcion != "0":
            console.input("\n[bold red]Presione enter para continuar.[/bold red]")    
