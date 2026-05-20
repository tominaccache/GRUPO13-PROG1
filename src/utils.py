from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


def mostrar_menu_generico(titulo, opciones, ancho=49):
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
        opciones_formateadas.append(f"[#a61b1b]{op}[/#a61b1b]")

    texto_menu = "\n".join(opciones_formateadas)

    panel = Panel(
        texto_menu,
        title=f"[bold white on #a61b1b] {
            titulo.upper()} [/bold white on #a61b1b]",
        box=box.DOUBLE,
        border_style="#a61b1b",
        padding=(
            1,
            4),
        expand=False,
        width=ancho,
    )

    console.print(panel)
    return console.input("\n[#a61b1b]Seleccione una opcion: [/#a61b1b]")


def mostrar_tabla_generica(titulo, columnas, filas, alineaciones=None):
    """
    Objetivo: Renderizar cualquier tabla del sistema de forma dinámica.
    Entradas:
        - titulo (str): El título superior de la tabla.
        - columnas (list): Lista de strings con los nombres de las columnas.
        - filas (list): Lista de listas con los datos de cada fila.
    Salida: Imprime la tabla en la consola.
    """
    # Creamos la tabla con el titulo
    tabla = Table(
        title=f"[bold white]{titulo.upper()}[/bold white]",
        box=box.DOUBLE_EDGE,
        border_style="red",
        header_style="bold yellow",
        row_styles=["none", "dim"],
        show_lines=False,
    )

    # Agregamos las columnas dinamicamente
    for i in range(len(columnas)):
        alig = alineaciones[i] if alineaciones and i < len(
            alineaciones) else "center"
        tabla.add_column(
            columnas[i],
            justify=alig,
            style="bold cyan" if alig == "center" else "cyan")

    # Agregamos las filas
    for fila in filas:
        # Convertimos cada dato de la fila a string por si hay numero
        fila_str = [str(dato) for dato in fila]
        # El asterisco (*) desempaqueta la lista para que add_row lo entienda
        tabla.add_row(*fila_str)

    console.print(tabla)
