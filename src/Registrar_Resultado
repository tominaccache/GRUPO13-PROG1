from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def limpiar_consola():
    console.clear()

def mostrar_menu():
    texto_menu = (
        "[bold red]1. Gestionar Pilotos[/bold red]\n"
        "[bold red]2. Gestionar Escuderías[/bold red]\n"
        "[bold red]3. Registrar Resultados de Gran Premio[/bold red]\n"
        "[bold red]4. Ver Tabla de Posiciones[/bold red]\n"
        "[bold red]5. Ver Estadísticas[/bold red]\n"
        "[bold red]6. Proyección de Campeonato[/bold red]\n"
        "[bold red]7. Guardar Datos[/bold red]\n"
        "[bold red]8. Cargar Datos[/bold red]\n"
        "[bold red]0. Salir[/bold red]"
    )
    
    panel = Panel(texto_menu, title="[bold red] Administrador de Campeonato F1 🏆[/bold red]"
                  ,border_style ="bold red",style="on white",padding=(1, 4), expand=False)
    console.print(panel)

    return console.input("\n[bold red]Seleccione una opción: [/bold red]")

def menu_resultados():
    """
    Objetivo: Mostrar el submenú de Registro de Resultados.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold blue]1. Registrar tiempos de carrera[/bold blue]\n"
        "[bold blue]2. Ver resultados[/bold blue]\n"
        "[bold blue]3. Modificar resultados[/bold blue]\n"
        "[bold blue]4. Eliminar resultados[/bold blue]\n"
        "[bold blue]0. Volver al menú principal[/bold blue]"
    )
    
    panel = Panel(
        texto_menu, 
        title="[bold blue] Registro de Resultados de Gran Premio 🏁 [/bold blue]",
        border_style="bold blue",
        style="on white",
        padding=(1, 4), 
        expand=False
    )
    console.print(panel)

    return console.input("\n[bold blue]Seleccione una opción: [/bold blue]")

def mostrar_ejemplo_resultados():
    tabla = Table(title="Resultados del Gran Premio", header_style="bold blue", border_style="blue")

    tabla.add_column("Pos", justify="center")
    tabla.add_column("Piloto")
    tabla.add_column("Tiempo (HH:MM:SS.mmm)")
    tabla.add_column("Puntos", justify="right")

    tabla.add_row("1", "Max Verstappen", "01:25:30.450", "25")
    tabla.add_row("2", "Lando Norris", "01:25:35.120", "18")

    console.print(tabla)

def main():
    continuar_programa = True
    
    while continuar_programa:
        limpiar_consola()
        opcion = mostrar_menu()
        
        match opcion:
            case "3":
                en_menu_resultados = True
                while en_menu_resultados:
                    limpiar_consola()
                    op_res = menu_resultados()
                    
                    if op_res == "1":
                        limpiar_consola()
                        console.print("[bold blue]--> Módulo para ingresar tiempos (HH:MM:SS.mmm)[/bold blue]")
                        console.input("\n[bold blue]Presione Enter para continuar...[/bold blue]")
                    
                    elif op_res == "2":
                        limpiar_consola()
                        mostrar_ejemplo_resultados()
                        console.input("\n[bold blue]Presione Enter para volver...[/bold blue]")
                        
                    elif op_res == "0":
                        en_menu_resultados = False
            
            case "0":
                console.print("\n[bold red]--> Saliendo del programa...[/bold red]")
                continuar_programa = False
            case _:
                console.print("\n[bold red]--> Opción no válida o en desarrollo.[/bold red]")
                console.input("[bold red]Presione Enter para continuar...[/bold red]")

if __name__ == "__main__":
    main()