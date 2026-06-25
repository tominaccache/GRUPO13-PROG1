from registrar_resultado import (
    tiempo_a_segundos,
    validar_tiempo,
    validar_vuelta_perdida,
    clave_orden
)
# =============================================
# TESTS PARA: registrar_resultado.py
# =============================================


def test_tiempo_a_segundos():
    """
    Objetivo: Verificar la conversión matemática exacta
              de cadenas HH:MM:SS.mmm a segundos.
    """
    # 01h (3600s) + 24 m(1440s) + 30.500s = 5070.5
    assert tiempo_a_segundos("01:24:30.500") == 5070.5
    # 00h (0s) + 60m (3600s) + 12.567  = 3.612.567
    assert tiempo_a_segundos("00:60:12.567") == 3612.567


def test_validar_tiempo():
    """
    Objetivo: Validar el comportamiento de la Regex frente a
              formatos de tiempo válidos e inválidos.
    """
    # Formato correcto: HH:MM:SS.mmm
    assert validar_tiempo("01:25:21.500") is True

    # Formato incorrecto
    assert validar_tiempo("1:25:30.500") is False   # Falta un digito en hora
    assert validar_tiempo("01-25-30.500") is False  # Separador incorrecto
    assert validar_tiempo("01:25:30,500") is False  # Coma en lugar de punto
    assert validar_tiempo("DNF") is False           # No es un tiempo numerico


def test_validar_vuelta_perdida():
    """
    Objetivo: Comprobar el reconocimiento estricto del patrón de
              vueltas perdidas (+N).
    """
    assert validar_vuelta_perdida("+1") is True   # 1 vuelta por detras
    assert validar_vuelta_perdida("+12") is True  # 12 vueltas atras
    assert validar_vuelta_perdida("1") is False   # Falta el mas
    assert validar_vuelta_perdida("-1") is False  # Signo incorrecto
    assert validar_vuelta_perdida("+A") is False  # No es un número


def test_clave_orden():
    """
    Objetivo: Evaluar el criterio de ordenamiento por tuplas de
              prioridad (Pilotos, +N y DNF).
    """
    # 1. Caso DNF (debe retornar prioridad 2)
    assert clave_orden(("HAM", "DNF")) == (2, 0)

    # 2. Caso Vuelta Perdida (debe retornar prioridad 1 y la cantidad de vuelta)
    assert clave_orden(("BOR", "+2")) == (1, 2)

    # 3. Caso Tiempo Normal (Debe retornar prioridad 0 y el tiempo en segundos)
    # 01:00:00.456 = 3600.546
    assert clave_orden(("VER", "01:00:00.456")) == (0, 3600.456)
