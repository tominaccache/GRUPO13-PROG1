import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datos import pilotos, escuderias 

console = Console()

def mostrar_menu_pilotos():
    """
    Objetivo: Mostrar el submenú de Gestión de Pilotos.
    """
    texto_menu = (
        "[bold red]1. Agregar piloto[/bold red]\n"
        "[bold red]2. Modificar Piloto[/bold red]\n"
        "[bold red]3. Eliminar piloto[/bold red]\n"
        "[bold red]4. Buscar piloto[/bold red]\n"
        "[bold red]5. Listar pilotos[/bold red]\n"
        "[bold red]0. Volver al menú principal[/bold red]"
    )

    panel = Panel(
        texto_menu,
        title="[bold red] Gestión de Pilotos[/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1, 4),
        expand=True,
        width=49,
    )
    console.print(panel)

def agregar_piloto():
    """Solicita datos para un nuevo piloto, valida e inserta en el diccionario."""
    console.print("[bold red]Agregar Piloto:[/bold red]\n")
    sigla = console.input("[bold red]Ingrese la sigla del piloto (3 letras): [/bold red]").upper()
    
    if not re.fullmatch(r"[A-Z]{3}", sigla):
        console.print("[bold red]Error: La sigla debe tener exactamente 3 letras.[/bold red]")
        return
    
    if sigla in pilotos:
        console.print("[bold red]Error: Ya existe un piloto con esa sigla.[/bold red]")
        return
    
    nombre = console.input("[bold red]Ingrese el nombre del piloto: [/bold red]")
    pais = console.input("[bold red]Ingrese el país del piloto: [/bold red]")
    
    esc_sigla = console.input("[bold red]Ingrese la sigla de la escudería (ej. RBR, FER): [/bold red]").upper()
    
    if esc_sigla not in escuderias:
        console.print("[bold red]Error: La escudería ingresada no existe en el sistema.[/bold red]")
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
    console.print("[bold red]Modificar Piloto:[/bold red]\n")
    sigla = console.input("[bold red]Ingrese la sigla del piloto a modificar: [/bold red]").upper()
    
    if sigla not in pilotos:
        console.print("[bold red]Error: No se encontró ningún piloto con esa sigla.[/bold red]")
        return
    
    piloto_actual = pilotos[sigla]
    console.print(f"[bold red]Modificando a: {piloto_actual['datos_personales'][0]}[/bold red]")
    
    nuevo_nombre = console.input("[bold red]Nuevo nombre (Deje en blanco para no modificar): [/bold red]")
    if nuevo_nombre.strip() == "":
        nuevo_nombre = piloto_actual["datos_personales"][0]
        
    nuevo_pais = console.input("[bold red]Nuevo país (Deje en blanco para no modificar): [/bold red]")
    if nuevo_pais.strip() == "":
        nuevo_pais = piloto_actual["datos_personales"][1]
        
    nueva_escuderia = console.input("[bold red]Nueva escudería (Deje en blanco para no modificar): [/bold red]").upper()
    if nueva_escuderia.strip() == "":
        nueva_escuderia = piloto_actual["escuderia"]
    elif nueva_escuderia not in escuderias:
        console.print("[bold red]Error: La escudería ingresada no existe. Se mantendrá la escudería anterior.[/bold red]")
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
    console.print("[bold red]Eliminar Piloto:[/bold red]\n")
    sigla = console.input("[bold red]Ingrese la sigla del piloto a eliminar: [/bold red]").upper()
    
    if sigla not in pilotos:
        console.print("[bold red]Error: No se encontró ningún piloto con esa sigla.[/bold red]")
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
    """Busca un piloto por su sigla y muestra sus datos en un panel."""
    console.print("[bold red]Buscar Piloto:[/bold red]\n")
    sigla = console.input("[bold red]Ingrese la sigla del piloto: [/bold red]\n").upper()
    
    if sigla not in pilotos:
        console.print("[bold red]Error: No se encontró ningún piloto con esa sigla.[/bold red]")
        return
    
    datos = pilotos[sigla]
    esc_sigla = datos['escuderia']
    if esc_sigla in escuderias:
        nombre_escuderia = escuderias[esc_sigla]['nombre']
    else:
        nombre_escuderia = "Escudería Eliminada/No existe"
    
    info_piloto = (
        f"[bold red]Sigla: {sigla} [/bold red]\n"
        f"[bold red]Nombre: {datos['datos_personales'][0]}[/bold red] \n"
        f"[bold red]Nacionalidad: {datos['datos_personales'][1]}[/bold red]\n"
        f"[bold red]Escudería: {datos['escuderia']} - {nombre_escuderia}[/bold red]\n"
        f"[bold red]Puntos Campeonato: {datos['puntos']}[/bold red]"
    )
    
    panel = Panel(info_piloto, title="[bold red]Información del Piloto[/bold red]", border_style="red",style="on white", expand=False)
    console.print(panel)

def listar_pilotos():
    """Muestra todos los pilotos registrados en formato de tabla (rich)."""
    if not pilotos:
        console.print("[bold yellow]No hay pilotos registrados en el sistema actualmente.[/bold yellow]")
        return

    # Crear la tabla de Rich
    tabla = Table(title=" Listado Oficial de Pilotos", border_style="bold red")
    
    # Definir las columnas
    tabla.add_column("Sigla", style="cyan", justify="center")
    tabla.add_column("Nombre", style="white")
    tabla.add_column("Nacionalidad", style="green")
    tabla.add_column("Escudería", style="magenta", justify="center")
    tabla.add_column("Puntos", style="yellow", justify="right")

    # Cargar los datos a la tabla
    for sigla, datos in pilotos.items():
        tabla.add_row(
            sigla,
            datos["datos_personales"][0],
            datos["datos_personales"][1],
            datos["escuderia"],
            str(datos["puntos"])
        )
        
    console.print(tabla)

def menu_pilotos():
    """Controlador del flujo del submenú de pilotos."""
    opcion = "-1"
    while opcion != "0":
        console.clear()
        mostrar_menu_pilotos()
        opcion = console.input("\n[bold red]Seleccione una opción: [/bold red]")
        print()
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
                console.print("[bold red]--> Volviendo al menú principal...[/bold red]")
            case _:
                console.print("[bold red]--> Opción no válida.[/bold red]")

        if opcion != "0":
            console.input("\n[bold red]Presione Enter para continuar...[/bold red]")