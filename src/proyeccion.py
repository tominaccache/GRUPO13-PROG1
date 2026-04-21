def obtener_lider(pilotos):
    lider = None
    max_puntos = -1

    for sigla, datos in pilotos.items():
        if datos["puntos"] > max_puntos:
            max_puntos = datos["puntos"]
            lider = sigla

    return lider, max_puntos


def analizar_piloto(pilotos, puntos_por_carrera):
    sigla = input("Ingrese sigla del piloto: ").upper()

    if sigla not in pilotos:
        print("Piloto no encontrado")
        return

    carreras_restantes = int(input("Carreras restantes: "))

    lider, puntos_lider = obtener_lider(pilotos)
    puntos_piloto = pilotos[sigla]["puntos"]

    max_por_carrera = max(puntos_por_carrera)

    maximo_posible = puntos_piloto + (carreras_restantes * max_por_carrera)

    print("\n--- RESULTADO ---")
    print(f"Lider: {lider} ({puntos_lider} pts)")
    print(f"{sigla}: {puntos_piloto} pts")
    print(f"Maximo posible: {maximo_posible}")

    if maximo_posible >= puntos_lider:
        print("Sigue en competencia")
    else:
        print("Ya no puede alcanzarlo")


def submenu_proyeccion(pilotos, puntos_por_carrera):
    opcion = ""

    while opcion != "0":
        print("\n--- PROYECCION DE CAMPEONATO ---")
        print("1. Analizar piloto")
        print("0. Volver")

        opcion = input("Opcion: ")

        if opcion == "1":
            analizar_piloto(pilotos, puntos_por_carrera)
        elif opcion == "0":
            print("Volviendo...")
        else:
            print("Opcion invalida")