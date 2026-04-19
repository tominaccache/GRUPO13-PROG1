from rich.console import Console
from rich.panel import Panel
from menuPilotoEscuderia import menu_pilotos
from menuEscuderias import menu_escuderias

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
    # Armamos el texto del menú con etiquetas de colores
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

    # Imprimimos el menú dentro de un recuadro
    panel = Panel(
        texto_menu,
        title="[bold red] Administrador de Campeonato F1[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=False,
        width=70
    )
    console.print(panel)

    return console.input("\n[bold red]Seleccione una opción: [/bold red]")


def main():
    """Objetivo: Funcion Principal que mantiene el ciclo de vida del proyecto"""
    opcion = "-1"
    while opcion != "0":
        limpiar_consola()
        opcion = mostrar_menu()
        print()
        match opcion:
            case "1":
                console.print("[bold red]--> Abriendo Modulo de Pilotos[/bold red]")
                menu_pilotos()
            case "2":
                console.print("[bold red]--> Abriendo Modulo de Escuderias[/bold red]")
                menu_escuderias()
            case "3":
                console.print("[bold red]--> Abriendo Registro de Carreras[/bold red]")
            case "4":
                console.print("[bold red]--> Abriendo Tablas de Posiciones[/bold red]")
            case "5":
                console.print("[bold red]--> Generando Estadisticas[/bold red]")
            case "6":
                console.print(
                    "[bold red]--> Generando Proyeccion del Campeonato[/bold red]"
                )
            case "7":
                console.print("[bold red]--> Guardando datos en Archivo[/bold red]")
            case "8":
                console.print("[bold red]--> Cargando datos en Archivo[/bold red]")
            case "0":
                console.print(
                    "[bold red]--> ¡Gracias por utilizar la aplicacion! Nos vemos la proxima.[/bold red]"
                )
            case _:
                console.print(
                    "[bold red]--> Error: Opción no válida. Ingrese un número del 0 al 8.[/bold red]"
                )

        if opcion != "0":
            print()
            console.input("[bold red]Presione Enter para continuar... [/bold red]")


if __name__ == "__main__":
    main()