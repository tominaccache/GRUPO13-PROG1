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
    opciones_formateadas = list(
        map(lambda opcion: f"[#a61b1b]{opcion}[/#a61b1b]", opciones))

    texto_menu = "\n".join(opciones_formateadas)

    panel = Panel(
        texto_menu,
        title=f"[bold white on #a61b1b] {titulo.upper()} [/bold white on #a61b1b]",
        box=box.DOUBLE,
        border_style="#a61b1b",
        padding=(1, 4),
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
    tabla = Table(
        title=f"[bold white]{titulo.upper()}[/bold white]",
        box=box.DOUBLE_EDGE,
        border_style="red",
        header_style="bold yellow",
        row_styles=["none", "dim"],
        show_lines=False,
    )

    for i in range(len(columnas)):
        alig = alineaciones[i] if alineaciones and i < len(
            alineaciones) else "center"
        tabla.add_column(
            columnas[i], justify=alig, style="bold cyan" if alig == "center" else "cyan"
        )

    for fila in filas:
        fila_str = list(map(str, fila))
        tabla.add_row(*fila_str)

    console.print(tabla)


def mostrar_panel_generico(titulo, contenido, ancho=None):
    """
    Objetivo: Renderizar cualquier recuadro
              de información (Panel) de forma dinámica.
    Entradas:
        - titulo (str): El titulo superior del panel.
        - contenido (str): El texto formateado que irá dentro.
        - ancho (int, opcional): Fija un ancho específico si se necesita.
    Salida: Imprime el panel por consola.
    """
    panel = Panel(
        contenido,
        title=f"[bold white on #a61b1b]{titulo.upper()} [/bold white on #a61b1b]",
        box=box.DOUBLE,
        border_style="#a61b1b",
        padding=(1, 4),
        expand=False,
        width=ancho,
    )

    console.print(panel)
