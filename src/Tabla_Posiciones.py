from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def limpiar_consola():
    console.clear()


def mostrar_menu_tabla_posiciones():
  
    texto_menu = (
            "[bold red]1. Ver Tabla de Pilotos[/bold red]\n"
            "[bold red]2. Ver Tabla de Escuderías[/bold red]\n"
            "[bold red]3. Exportar Clasificación[/bold red]\n"
            "[bold red]0. Volver al menú principal[/bold red]"
    )
    panel = Panel(
            texto_menu,
            title="[bold red] Tabla de Posiciones[/bold red]",
            border_style="bold red",
            style="on white",
            padding=(1, 4),
            expand=False,
            width=49
    )
    console.print(panel)
    return console.input("\n[bold red]Seleccione una opción: [/bold red]")
        
def menu_tabla_posiciones():
    continuar_programa = True
    while continuar_programa:
        limpiar_consola()      
        op=mostrar_menu_tabla_posiciones()

        match op:
            case "1":
                console.print("[bold red]--> Ver Tabla de Pilotos (próximamente)[/bold red]")
            case "2":
                console.print("[bold red]--> Ver Tabla de Escuderías (próximamente)[/bold red]")
            case "3":
                console.print("[bold red]--> Exportar Clasificación (proximamente)[/bold red]")
            case "0":
                continuar_programa= False
            case _:
                console.print("[bold red]--> Opcion no Válida.[/bold red]")
            
        if op != "0":
            console.input("\n[bold red]Presione Enter para continuar.[/bold red]")
                    