from rich.console import Console
from rich.panel import Panel

# Inicializamos la consola 
console = Console()

def limpiar_consola():
    """Objetivo: Limpiar la consola para que quede más prolijo""" 
    console.clear()

def mostrar_menu():
    """
    Objetivo: Mostrar el menú principal del sistema usando la libreria rich.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
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

def menu_pilotos():
    """
    Objetivo: Mostrar el submenú de Gestión de Pilotos.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold blue]1. Agregar piloto[/bold blue]\n"
        "[bold blue]2. Modificar Piloto[/bold blue]\n"
        "[bold blue]3. Eliminar piloto[/bold blue]\n"
        "[bold blue]4. Buscar piloto[/bold blue]\n"
        "[bold blue]5. Listar pilotos[/bold blue]\n"
        "[bold blue]0. Volver al menú principal[/bold blue]"
    )
    
    panel = Panel(texto_menu, title="[bold blue] Gestión de Pilotos 🏎️ [/bold blue]"
                  ,border_style ="bold blue",style="on white",padding=(1, 4), expand=False)
    console.print(panel)

    return console.input("\n[bold blue]Seleccione una opción: [/bold blue]")

def menu_escuderias():
    """
    Objetivo: Mostrar el submenú de Gestión de Escuderías.
    Salida: Retorna la opción ingresada por el usuario como un string.
    """
    texto_menu = (
        "[bold green]1. Agregar escudería[/bold green]\n"
        "[bold green]2. Modificar escudería[/bold green]\n"
        "[bold green]3. Eliminar escudería[/bold green]\n"
        "[bold green]4. Ver escuderías[/bold green]\n"
        "[bold green]0. Volver al menú principal[/bold green]"
    )
    
    panel = Panel(texto_menu, title="[bold green] Gestión de Escuderías 🛠️ [/bold green]"
                  ,border_style ="bold green",style="on white",padding=(1, 4), expand=False)
    console.print(panel)

    return console.input("\n[bold green]Seleccione una opción: [/bold green]")
    
def main():
    """Objetivo: Funcion Principal que mantiene el ciclo de vida del proyecto """
    continuar_programa = True
    
    while continuar_programa:
        limpiar_consola()
        opcion = mostrar_menu()
        
        match opcion:
            case "1":
                en_menu_pilotos = True
                while en_menu_pilotos:
                    limpiar_consola()
                    op_pilotos = menu_pilotos()
                    if op_pilotos == "0":
                        en_menu_pilotos = False
            case "2":
                en_menu_escuderias = True
                while en_menu_escuderias:
                    limpiar_consola()
                    op_escuderias = menu_escuderias()
                    if op_escuderias == "0":
                        en_menu_escuderias = False
            case "0":
                console.print("\n[bold red]--> Saliendo del programa...[/bold red]")
                continuar_programa = False
            case _:
                console.print("\n[bold red]--> Opción en desarrollo o no válida.[/bold red]")
                console.input("[bold red]Presione Enter para continuar...[/bold red]")

# Punto de entrada para ejecutar el script por sí solo
if __name__ == "__main__":
    main()