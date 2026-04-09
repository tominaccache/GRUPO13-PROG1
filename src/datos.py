# Matriz de pilotos: [sigla, nombre, nacionalidad, escudería, puntos]
pilotos = [ 
            ["VER","Max Verstappen","Holanda","RBR",0],
            [ "HAD","IHadjar","Francia","RBR",0],
            [ "HAM","Lewis Hamilton","Reino Unido","FER",0],
            [ "LEC","Charles Leclerc","Mónaco","FER",0],
            [ "RUS","George Russell","Reino Unido","MER",0],
            [ "ANT","Kimi Antonelli","Italia","MER",0],
            [ "NOR","Lando Norris","Reino Unido","MCL",0],
            ["PIA","Oscar Piastri", "Australia","MCL", 0],
            [ "ALO","Fernando Alonso","España","AST",0],
            [ "STR","Lance Stroll","Canadá","AST",0],
            [ "COL","Franco Colapinto","Argentina","ALP",0],
            [ "GAS","Pierre Gasly","Francia","ALP",0],
            [ "SAI","Carlos Sainz","España","WIL",0],
            [ "ALB","Alexander Albon","Tailandia","WIL",0],
            [ "LAW","Liam Lawson","Nueva Zelanda","RB",0],
            [ "LIN","Arvid Lindblad","Reino Unido","RB",0],
            [ "BEA","Oliver Bearman","Reino Unido","HAAS",0],
            [ "OCO","Esteban Ocon","Francia","HAAS",0],
            [ "BOR","Gabriel Bortoleto","Brasil","AUD",0],
            [ "HUL","Nico Hülkenberg","Alemania","AUD",0],
            ["BOT","Valtteri Bottas", "Finlandia","CAD", 0],
            ["PER","Sergio Pérez","México","CAD",0]
        ]

# Matriz de escuderías: [sigla, nombre, país, puntos]
escuderias=[
            ["RBR","Oracle Red Bull Racing", "Austria",0],
            ["MER","Mercedes-AMG Petronas", "Alemania",0],
            ["FER","Scuderia Ferrari", "Italia",0],
            ["MCL","McLaren F1 Team", "Reino Unido",0],
            ["ALP","Alpine F1 Team", "Francia",0],
            ["AST","Aston Martin Aramco", "Reino Unido",0],
            ["WIL","Williams Racing", "Reino Unido",0],
            ["HAAS","Haas F1 Team", "Estados Unidos",0],
            ["CAD","Cadillac Racing", "Estados Unidos",0],
            ["RB","Racing Bulls","Italia",0],
            ["AUD","Audi Revolut","Alemania",0]
            ]

# Lista de carreras del campeonato
carreras= ["Australia","China","Japon","Miami","Canadá","Monaco","Barcelona","Austria","Gran Bretaña","Belgica","Hungria",
           "Paises Bajos","Italia","España","Azerbaijan","Singapur","Estados Unidos","Mexico","Brasil","Las Vegas","Qatar""Abu Dhabi"]

puntos= [25,18,15,12,10,8,6,4,2,1]

# Matriz de resultados: 

cantidad_carreras = len(carreras)
cantidad_pilotos = len(pilotos)

matriz_resultados = []
for fila in range(cantidad_pilotos):
    fila_vacia = []
    for columna in range(cantidad_carreras):
        fila_vacia.append(0) 
    matriz_resultados.append(fila_vacia)   
    