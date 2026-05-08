from rich.console import Console
from rich.panel import Panel

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
    
    