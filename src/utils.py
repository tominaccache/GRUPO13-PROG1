from rich.console import Console
from rich.panel import Panel
from rich.table import Table
console = Console()

def mostrar_menu_generico(titulo, opciones,ancho = 49):
    """
    Objetivo: Renderizar cualquier menú del sistema de forma dinámica.
    Entradas:
        - titulo (str): El título que aparecerá en el borde del panel.
        - opciones (list): Lista de strings con las opciones a mostrar.
        - ancho (int): Ancho del panel (por defecto 49, como usabas).
    Salida: Retorna la opción ingresada por el usuario como string.
    """
    # Recorremos la lista de opciones y le agregamos el color rojo a cada una
    opciones_formateadas = []
    for op in opciones:
        opciones_formateadas.append(f"[bold red]{op}[/bold red]")
        
    texto_menu = "\n".join(opciones_formateadas)
    
    panel = Panel (
        texto_menu,
        title=f"[bold red] {titulo} [/bold red]",
        border_style="bold red",
        style="on white",
        padding=(1,4),
        expand= False,
        width=ancho
    )
    
    console.print(panel)
    return console.input("\n[bold red]Seleccione una opcion: [/bold red]")

def mostrar_tabla_generica(titulo,filas,columnas):
    """
    Objetivo: Renderizar cualquier menú del sistema de forma dinámica.
    Entradas:
        - titulo (str): El título que aparecerá en el borde del panel.
        - opciones (list): Lista de strings con las opciones a mostrar.
        - ancho (int): Ancho del panel (por defecto 49, como usabas).
    Salida: Retorna la opción ingresada por el usuario como string.
    """
    # Creamos la tabla con el titulo
    tabla = Table(
        title=f"{titulo}",
        border_style="bold red",
        style="on white"
    )
    
    # Agregamos las columnas dinamicamente
    for col in columnas:
        tabla.add_column(col,style="bold white",justify="center")
        
    # Agregamos las filas
    for fila in filas:
        # Convertimos cada dato de la fila a string por si hay numero 
        fila_str = [str[dato] for dato in fila]
        # El asterisco (*) desempaqueta la lista para que add_row lo entienda
        tabla.add_row(*fila_str)
        
    console.print(tabla)
        
    