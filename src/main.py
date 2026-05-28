from rich.console import Console
from utils import mostrar_menu_generico

# Importamos desde tus archivos
from Tabla_Posiciones import menu_tabla_posiciones
# Asumo que el archivo de guardado se llama archivos.py
from archivos import menu_guardar, menu_cargar

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
    opciones = [
        "1. Gestionar Pilotos",
        "2. Gestionar Escuderías",
        "3. Registrar Resultados de Gran Premio",
        "4. Ver Tabla de Posiciones",
        "5. Ver Estadísticas",
        "6. Proyección de Campeonato",
        "7. Guardar Datos",
        "8. Cargar Datos",
        "0. Salir"
    ]
    return mostrar_menu_generico("Administrador de Campeonato F1 🏆", opciones, ancho=55)


def main():
    """Objetivo: Funcion Principal que mantiene el ciclo de vida del proyecto"""
    opcion = "-1"
    while opcion != "0":
        limpiar_consola()
        opcion = mostrar_menu()
        print()

        match opcion:
            case "1":
                console.print(
                    "[#a61b1b]--> Abriendo Modulo de Pilotos[/#a61b1b]")
            case "2":
                console.print(
                    "[#a61b1b]--> Abriendo Modulo de Escuderias[/#a61b1b]")
            case "3":
                console.print(
                    "[#a61b1b]--> Abriendo Registro de Carreras[/#a61b1b]")
            case "4":
                menu_tabla_posiciones()
            case "5":
                console.print("[#a61b1b]--> Generando Estadisticas[/#a61b1b]")
            case "6":
                console.print(
                    "[#a61b1b]--> Generando Proyeccion del Campeonato[/#a61b1b]")
            case "7":
                menu_guardar()
            case "8":
                menu_cargar()
            case "0":
                console.print(
                    "[#a61b1b]--> ¡Gracias por utilizar la aplicacion! Nos vemos la proxima.[/#a61b1b]")
            case _:
                console.print(
                    "[#a61b1b]--> Error: Opción no válida. Ingrese un número del 0 al 8.[/#a61b1b]")

        # Pausa solo para las opciones que aún no tienen su propio menú implementado o errores
        if opcion in ["1", "2", "3", "5", "6"] or (opcion != "0" and opcion not in [str(i) for i in range(1, 9)]):
            print()
            console.input(
                "[#a61b1b]Presione Enter para continuar... [/#a61b1b]")


if __name__ == "__main__":
    main()
