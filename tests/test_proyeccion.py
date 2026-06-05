import datos
from proyeccion import puede_alcanzar_lider_recursivo, obtener_lider, analizar_piloto
import pytest
import sys
import os

# Asegurar que pytest encuentre la carpeta src
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


# ==========================================
# TESTS PARA: puede_alcanzar_lider_recursivo
# ==========================================

def test_alcanzar_lider_recursivo_imposible():
    resultado = puede_alcanzar_lider_recursivo(10, 2, 100, 25)
    assert resultado is False, "Debería ser False porque es matemáticamente insalvable"


def test_alcanzar_lider_recursivo_posible_exacto():
    resultado = puede_alcanzar_lider_recursivo(50, 2, 100, 25)
    assert resultado is True, "Debería ser True porque lo alcanza con los puntos justos"


def test_alcanzar_lider_recursivo_ya_superado():
    resultado = puede_alcanzar_lider_recursivo(120, 5, 100, 25)
    assert resultado is True, "Debería ser True porque ya tiene más puntos que el líder"


def test_alcanzar_lider_recursivo_sin_carreras():
    resultado = puede_alcanzar_lider_recursivo(80, 0, 100, 25)
    assert resultado is False, "Debería ser False porque no quedan carreras"

# ==========================================
# TESTS PARA: obtener_lider
# ==========================================


def test_obtener_lider():
    pilotos_mock = {
        "VER": {"puntos": 350},
        "NOR": {"puntos": 280},
        "LEC": {"puntos": 351}
    }
    lider, puntos = obtener_lider(pilotos_mock)

    assert lider == "LEC", "Leclerc debería ser el líder"
    assert puntos == 351, "Los puntos del líder deberían ser 351"

# ==========================================
# TESTS PARA: analizar_piloto (NUEVO)
# ==========================================


def test_analizar_piloto_eliminado(capsys):
    """Prueba de integración verificando la salida por consola (Capsys)"""
    # 1. Preparar el entorno (Mocks)
    datos.pilotos.clear()
    datos.pilotos.update({
        "VER": {"puntos": 300},
        "COL": {"puntos": 10}
    })
    datos.carreras.clear()
    datos.carreras.extend(["GP1", "GP2"])  # 2 carreras en total
    datos.tiempos_carreras.clear()         # 0 disputadas, faltan 2

    # 2. Ejecutar la función
    analizar_piloto("COL")

    # 3. Capturar la consola y realizar Asersiones
    captured = capsys.readouterr()
    assert "MATEMÁTICAMENTE ELIMINADO" in captured.out
    assert "VER" in captured.out
    assert "COL" in captured.out


def test_analizar_piloto_en_carrera(capsys):
    """Prueba verificando un escenario donde el piloto sí puede ganar"""
    datos.pilotos.clear()
    datos.pilotos.update({
        "VER": {"puntos": 300},
        "NOR": {"puntos": 280}
    })
    datos.carreras.clear()
    datos.carreras.extend(["GP1", "GP2"])
    datos.tiempos_carreras.clear()

    analizar_piloto("NOR")

    captured = capsys.readouterr()
    assert "MATEMÁTICAMENTE POSIBLE" in captured.out
