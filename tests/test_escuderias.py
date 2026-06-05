from menu_escuderias import validar_sigla

# =============================================
# TESTS PARA: menu_escuderias.py
# =============================================


def test_validar_sigla():
    """
    Objetivo: Validar que el formato de siglas
              acepte solo 3 letras mayúsculas (ABM Escuderías).
    """
    # Casos de exito
    assert validar_sigla("RBR") is True
    assert validar_sigla("FER") is True

    # Casos de Fallo
    assert validar_sigla("rbr") is False
    assert validar_sigla("RB") is False
    assert validar_sigla("RBRR") is False
    assert validar_sigla("R12") is False
