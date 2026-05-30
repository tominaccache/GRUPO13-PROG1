from rich.console import Console
from rich.panel import Panel
from gestion_piloto import menu_pilotos
from menu_escuderias import menu_escuderias
from tabla_posiciones import menu_tabla_posiciones
from proyeccion import submenu_proyeccion
from registrar_resultado import menu_resultados
from menu_estadisticas import menu_estadisticas
from manejo_archivos import menu_cargar, menu_guardar
from utils import mostrar_menu_generico

# Inicializamos la consola
console = Console()


def main():
    """
    Objetivo: Funcion Principal que mantiene el ciclo de vida del proyecto
    """
    opciones_menu = [
        "1. Gestionar Pilotos",
        "2. Gestionar Escuderías",
        "3. Registrar Resultados de Gran Premio",
        "4. Ver Tabla de Posiciones",
        "5. Ver Estadísticas",
        "6. Proyección del Campeonato",
        "7. Guardar Datos",
        "8. Cargar Datos",
        "0. Salir",
    ]
    opcion = "-1"
    while opcion != "0":
        console.clear()
        opcion = mostrar_menu_generico(
            "Administrador de Campeonato de F1", opciones_menu
        )
        match opcion:
            case "1":
                menu_pilotos()
            case "2":
                menu_escuderias()
            case "3":
                menu_resultados()
            case "4":
                menu_tabla_posiciones()
            case "5":
                menu_estadisticas()
            case "6":
                submenu_proyeccion()
            case "7":
                menu_guardar()
            case "8":
                menu_cargar()
            case "0":
                console.print(
                    "[#a61b1b]--> Gracias por utilizar la aplicacion.\n"
                    "Nos vemos la proxima.[/#a61b1b]"
                )
            case _:
                console.print(
                    "[#a61b1b]--> Error: Opción no válida. "
                    "Ingrese un número del 0 al 8.[/#a61b1b]"
                )

        if opcion != "0":
            console.input(
                "\n[#a61b1b]Presione Enter para continuar.[/#a61b1b]"
            )


if __name__ == "__main__":
    main()
