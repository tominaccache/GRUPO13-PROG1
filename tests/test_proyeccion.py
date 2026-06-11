from proyeccion import puede_alcanzar_lider_recursivo, obtener_lider, analizar_piloto

# ==========================================
# TESTS PARA: puede_alcanzar_lider_recursivo
# ==========================================


def test_alcanzar_lider_recursivo_imposible():
    resultado = puede_alcanzar_lider_recursivo(10, 2, 100, 25)
    assert resultado is False


def test_alcanzar_lider_recursivo_posible_exacto():
    resultado = puede_alcanzar_lider_recursivo(50, 2, 100, 25)
    assert resultado is True


def test_alcanzar_lider_recursivo_ya_superado():
    resultado = puede_alcanzar_lider_recursivo(120, 5, 100, 25)
    assert resultado is True


def test_alcanzar_lider_recursivo_sin_carreras():
    resultado = puede_alcanzar_lider_recursivo(80, 0, 100, 25)
    assert resultado is False, "Debería ser False porque no quedan carreras"
