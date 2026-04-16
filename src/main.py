def mostrar_menu():
    """
    Objetivo: Mostrar el menú principal del sistema.
    Salida: Retorna la opción ingresada por el usuario como un int 
    """
    print("\n Administrador de Campeonato de Formula 1")
    print("1. Gestionar Pilotos")
    print("2. Gestionar Escuderías")
    print("3. Registrar Resultados de Gran Premio")
    print("4. Ver Tabla de Posiciones")
    print("5. Ver Estadísticas")
    print("6. Proyección de Campeonato")
    print("7. Guardar Datos")
    print("8. Cargar Datos")
    print("0. Salir")
    
    opcion = int (input("\nSeleccione una opción: "))
    return opcion
    
def main():
    """
    Objetivo: Funcion Principal que mantiene el ciclo de vida del proyecto
    """
    