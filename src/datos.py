"""
Diccionario de Pilotos:
- Clave: Sigla de piloto(3 letras)
- Valor: Diccionario con tupla inmutable (Nombre, Nacionalidad), escuderia, puntos
"""

pilotos = {
    "VER": {
        "datos_personales": ["Max Verstappen", "Holanda"],
        "escuderia": "RBR",
        "puntos": 0,
    },
    "HAD": {
        "datos_personales": ["Isack Hadjar", "Francia"],
        "escuderia": "RBR",
        "puntos": 0,
    },
    "HAM": {
        "datos_personales": ["Lewis Hamilton", "Reino Unido"],
        "escuderia": "FER",
        "puntos": 0,
    },
    "LEC": {
        "datos_personales": ["Charles Leclerc", "Monaco"],
        "escuderia": "FER",
        "puntos": 0,
    },
    "RUS": {
        "datos_personales": ["George Russell", "Reino Unido"],
        "escuderia": "MER",
        "puntos": 0,
    },
    "ANT": {
        "datos_personales": ["Kimi Antonelli", "Italia"],
        "escuderia": "MER",
        "puntos": 0,
    },
    "NOR": {
        "datos_personales": ["Lando Norris", "Reino Unido"],
        "escuderia": "MCL",
        "puntos": 0,
    },
    "PIA": {
        "datos_personales": ["Oscar Piastri", "Australia"],
        "escuderia": "MCL",
        "puntos": 0,
    },
    "ALO": {
        "datos_personales": ["Fernando Alonso", "España"],
        "escuderia": "AST",
        "puntos": 0,
    },
    "STR": {
        "datos_personales": ["Lance Stroll", "Canada"],
        "escuderia": "AST",
        "puntos": 0,
    },
    "COL": {
        "datos_personales": ["Franco Colapinto", "Argentina"],
        "escuderia": "ALP",
        "puntos": 0,
    },
    "GAS": {
        "datos_personales": ["Pierre Gasly", "Francia"],
        "escuderia": "ALP",
        "puntos": 0,
    },
    "SAI": {
        "datos_personales": ["Carlos Sainz", "España"],
        "escuderia": "WIL",
        "puntos": 0,
    },
    "ALB": {
        "datos_personales": ["Alexander Albon", "Tailandia"],
        "escuderia": "WIL",
        "puntos": 0,
    },
    "LAW": {
        "datos_personales": ["Liam Lawson", "Nueva Zelanda"],
        "escuderia": "RBU",
        "puntos": 0,
    },
    "LIN": {
        "datos_personales": ["Arvid Lindbland", "Reino Unido"],
        "escuderia": "RBU",
        "puntos": 0,
    },
    "BEA": {
        "datos_personales": ["Oliver Bearman", "Reino Unido"],
        "escuderia": "HAS",
        "puntos": 0,
    },
    "OCO": {
        "datos_personales": ["Esteban Ocon", "Francia"],
        "escuderia": "HAS",
        "puntos": 0,
    },
    "BOR": {
        "datos_personales": ["Gabriel Bortoleto", "Brasil"],
        "escuderia": "AUD",
        "puntos": 0,
    },
    "HUL": {
        "datos_personales": ["Niko Hülkenberg", "Alemania"],
        "escuderia": "AUD",
        "puntos": 0,
    },
    "BOT": {
        "datos_personales": ["Valtteri Bottas", "Finlandia"],
        "escuderia": "CAD",
        "puntos": 0,
    },
    "PER": {
        "datos_personales": ["Sergio Perez", "Mexico"],
        "escuderia": "CAD",
        "puntos": 0,
    },
}
"""
Diccionario de Escuderias:
    - Clave: Sigla de la escuderia (3 letras)
    - Valor: Diccionario con nombre, pais, pilotos, puntos
"""

escuderias = {
    "RBR": {
        "nombre": "Oracle Red Bull Racing",
        "pais": "Austria",
        "pilotos": ["VER", "HAD"],
        "puntos": 0,
    },
    "MER": {
        "nombre": "Mercedes-AMG Petronas",
        "pais": "Alemania",
        "pilotos": ["RUS", "ANT"],
        "puntos": 0,
    },
    "FER": {
        "nombre": "Scuderia Ferrari",
        "pais": "Italia",
        "pilotos": ["HAM", "LEC"],
        "puntos": 0,
    },
    "MCL": {
        "nombre": "McLaren F1 Team",
        "pais": "Reino Unido",
        "pilotos": ["NOR", "PIA"],
        "puntos": 0,
    },
    "ALP": {
        "nombre": "Alpine F1 Team",
        "pais": "Francia",
        "pilotos": ["COL", "GAS"],
        "puntos": 0,
    },
    "AST": {
        "nombre": "Aston Martin Aramco",
        "pais": "Reino Unido",
        "pilotos": ["ALO", "STR"],
        "puntos": 0,
    },
    "WIL": {
        "nombre": "Williams Racing",
        "pais": "Reino Unido",
        "pilotos": ["SAI", "ALB"],
        "puntos": 0,
    },
    "HAS": {
        "nombre": "Haas F1 Team",
        "pais": "Estados Unidos",
        "pilotos": ["BEA", "OCO"],
        "puntos": 0,
    },
    "CAD": {
        "nombre": "Cadillac Racing",
        "pais": "Estados Unidos",
        "pilotos": ["BOT", "PER"],
        "puntos": 0,
    },
    "RBU": {
        "nombre": "Racing Bulls",
        "pais": "Italia",
        "pilotos": ["LAW", "LIN"],
        "puntos": 0,
    },
    "AUD": {
        "nombre": "Audi Revolut",
        "pais": "Alemania",
        "pilotos": ["BOR", "HUL"],
        "puntos": 0,
    },
}

# Lista de carreras del campeonato
carreras = [
    "Australia",
    "China",
    "Japon",
    "Miami",
    "Canadá",
    "Monaco",
    "Barcelona",
    "Austria",
    "Gran Bretaña",
    "Belgica",
    "Hungria",
    "Paises Bajos",
    "Italia",
    "España",
    "Azerbaijan",
    "Singapur",
    "Estados Unidos",
    "Mexico",
    "Brasil",
    "Las Vegas",
    "Qatar",
    "Abu Dhabi"
]

puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

# Matriz de resultados:

cantidad_carreras = len(carreras)
cantidad_pilotos = len(pilotos)

matriz_resultados = []
for fila in range(cantidad_pilotos):
    fila_vacia = []
    for columna in range(cantidad_carreras):
        fila_vacia.append(0)
    matriz_resultados.append(fila_vacia)
