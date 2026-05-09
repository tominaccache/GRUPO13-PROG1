import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datos import pilotos, escuderias
from rich import box
from utils import mostrar_menu_generico,mostrar_tabla_generica
console = Console()

def agregar_piloto():
    """Solicita datos para un nuevo piloto, valida e inserta en el diccionario."""
    console.print("[#a61b1b]Agregar Piloto:[/#a61b1b]\n")
    sigla = console.input("[#a61b1b]Ingrese la sigla del piloto (3 letras): [/#a61b1b]").upper()
    
    if not re.fullmatch(r"[A-Z]{3}", sigla):
        console.print("[#a61b1b]Error: La sigla debe tener exactamente 3 letras.[/#a61b1b]")
        return
    
    if sigla in pilotos:
        console.print("[#a61b1b]Error: Ya existe un piloto con esa sigla.[/#a61b1b]")
        return
    
    nombre = console.input("[#a61b1b]Ingrese el nombre del piloto: [/#a61b1b]")
    pais = console.input("[#a61b1b]Ingrese el país del piloto: [/#a61b1b]")
    
    esc_sigla = console.input("[#a61b1b]Ingrese la sigla de la escudería (ej. RBR, FER): [/#a61b1b]").upper()
    
    if esc_sigla not in escuderias:
        console.print("[#a61b1b]Error: La escudería ingresada no existe en el sistema.[/#a61b1b]")
        return

    # Agregar al diccionario de pilotos
    pilotos[sigla] = {
        "datos_personales": [nombre, pais],
        "escuderia": esc_sigla,
        "puntos": 0
    }
    
    # Vincular al piloto dentro del diccionario de la escudería
    escuderias[esc_sigla]["pilotos"].append(sigla)
    
    console.print(f"\n[bold green]✅ Piloto {nombre} ({sigla}) agregado correctamente a la escudería {esc_sigla}.[/bold green]")

def modificar_piloto():
    """Permite actualizar el nombre, país o escudería de un piloto existente."""
    console.print("[#a61b1b]Modificar Piloto:[/#a61b1b]\n")
    sigla = console.input("[#a61b1b]Ingrese la sigla del piloto a modificar: [/#a61b1b]").upper()
    
    if sigla not in pilotos:
        console.print("[#a61b1b]Error: No se encontró ningún piloto con esa sigla.[/#a61b1b]")
        return
    
    piloto_actual = pilotos[sigla]
    console.print(f"[#a61b1b]Modificando a: {piloto_actual['datos_personales'][0]}[/#a61b1b]")
    
    nuevo_nombre = console.input("[#a61b1b]Nuevo nombre (Deje en blanco para no modificar): [/#a61b1b]")
    if nuevo_nombre.strip() == "":
        nuevo_nombre = piloto_actual["datos_personales"][0]
        
    nuevo_pais = console.input("[#a61b1b]Nuevo país (Deje en blanco para no modificar): [/#a61b1b]")
    if nuevo_pais.strip() == "":
        nuevo_pais = piloto_actual["datos_personales"][1]
        
    nueva_escuderia = console.input("[#a61b1b]Nueva escudería (Deje en blanco para no modificar): [/#a61b1b]").upper()
    if nueva_escuderia.strip() == "":
        nueva_escuderia = piloto_actual["escuderia"]
    elif nueva_escuderia not in escuderias:
        console.print("[#a61b1b]Error: La escudería ingresada no existe. Se mantendrá la escudería anterior.[/#a61b1b]")
        nueva_escuderia = piloto_actual["escuderia"]
    else:
        # Si la escudería cambia, remover al piloto de la antigua (si existe) y agregarlo a la nueva
        escuderia_antigua = piloto_actual["escuderia"]
        if escuderia_antigua in escuderias and sigla in escuderias[escuderia_antigua]["pilotos"]:
            escuderias[escuderia_antigua]["pilotos"].remove(sigla)
        escuderias[nueva_escuderia]["pilotos"].append(sigla)

    # Actualizar datos en el diccionario
    pilotos[sigla]["datos_personales"] = [nuevo_nombre, nuevo_pais]
    pilotos[sigla]["escuderia"] = nueva_escuderia
    
    console.print(f"\n[bold green]✅ Datos del piloto {sigla} actualizados correctamente.[/bold green]")

def eliminar_piloto():
    """Elimina a un piloto del sistema y rompe la relación con su escudería."""
    console.print("[#a61b1b]Eliminar Piloto:[/#a61b1b]\n")
    sigla = console.input("[#a61b1b]Ingrese la sigla del piloto a eliminar: [/#a61b1b]").upper()
    
    if sigla not in pilotos:
        console.print("[#a61b1b]Error: No se encontró ningún piloto con esa sigla.[/#a61b1b]")
        return
    
   # Remover al piloto de la lista de su escudería verificando que la escudería aún exista
    escuderia_asignada = pilotos[sigla]["escuderia"]
    if escuderia_asignada in escuderias and sigla in escuderias[escuderia_asignada]["pilotos"]:
        escuderias[escuderia_asignada]["pilotos"].remove(sigla)
        
    # Eliminar del diccionario principal
    nombre_eliminado = pilotos[sigla]["datos_personales"][0]
    del pilotos[sigla]
    
    console.print(f"\n[bold green]✅ El piloto {nombre_eliminado} ({sigla}) ha sido eliminado del sistema.[/bold green]")

def buscar_piloto():
    """Objetivo: Busca un piloto por su sigla y muestra sus datos en un panel."""
    console.print("[#a61b1b]Buscar Piloto:[/#a61b1b]")
    sigla = console.input("[#a61b1b]Ingrese la sigla del piloto: [/#a61b1b]").upper()
    print()
    if sigla not in pilotos:
        console.print("[#a61b1b]Error: No se encontró ningún piloto con esa sigla.[/#a61b1b]")
        return
    
    datos = pilotos[sigla]
    esc_sigla = datos['escuderia']
    if esc_sigla in escuderias:
        nombre_escuderia = escuderias[esc_sigla]['nombre']
    else:
        nombre_escuderia = "Escudería Eliminada/No existe"
    
    info_piloto = (
        f"[#a61b1b]Sigla: {sigla} [/ #a61b1b]\n"
        f"[#a61b1b]Nombre: {datos['datos_personales'][0]}[/#a61b1b] \n"
        f"[#a61b1b]Nacionalidad: {datos['datos_personales'][1]}[/#a61b1b]\n"
        f"[#a61b1b]Escudería: {datos['escuderia']} - {nombre_escuderia}[/#a61b1b]\n"
        f"[#a61b1b]Puntos Campeonato: {datos['puntos']}[/#a61b1b]"
    )
    
    panel = Panel(
        info_piloto, 
        title="[white on #a61b1b]Información del Piloto[/white on #a61b1b]",
        box=box.DOUBLE,
        border_style="#a61b1b",
        expand=False
    )
    console.print(panel)

def listar_pilotos():
    """Muestra todos los pilotos registrados en formato de tabla (rich)."""
    if not pilotos:
        console.print("[bold yellow]No hay pilotos registrados en el sistema actualmente.[/bold yellow]")
        return

    # Crear la tabla de Rich
    cabeceras=["Sigla","Nombre","Nacionalidad","Escudería","Puntos"]
    alineaciones = ["center","left","left","center","center"]
    
    filas = []
    for sigla, datos in pilotos.items():
        fila = [
            sigla,
            datos["datos_personales"][0],
            datos["datos_personales"][1],
            datos["escuderia"],
            datos["puntos"]
        ]
        filas.append(fila)
    mostrar_tabla_generica("Listado Oficial de Pilotos",cabeceras,filas,alineaciones)
        
def menu_pilotos():
    """Controlador del flujo del submenú de pilotos."""
    opciones_menu= [
        "1. Agregar Piloto",
        "2. Modificar Piloto",
        "3. Eliminar piloto",
        "4. Buscar Piloto",
        "5. Listar Pilotos",
        "0. Volver al Menú Principal"
    ]
    opcion = "-1"
    while opcion != "0":
        console.clear()
        
        opcion = mostrar_menu_generico("Gestión de Pilotos",opciones_menu)
        match opcion:
            case "1":
                console.clear()
                agregar_piloto()
            case "2":
                console.clear()
                modificar_piloto()
            case "3":
                console.clear()
                eliminar_piloto()
            case "4":
                console.clear()
                buscar_piloto()
            case "5":
                console.clear()
                listar_pilotos()
            case "0":
                console.print("[#a61b1b]--> Volviendo al menú principal...[/#a61b1b]")
            case _:
                console.print("[#a61b1b]--> Opción no válida.[/#a61b1b]")

        if opcion != "0":
            console.input("\n[#a61b1b]Presione Enter para continuar...[/#a61b1b]")