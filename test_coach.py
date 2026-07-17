# test_coach.py
import pytest
from coach import CoachAI

def test_usuario_inicializacion():
    """Prueba que un nuevo usuario empiece de forma correcta."""
    user = CoachAI("Marcus", "Basketball")
    assert user.username == "Marcus"
    assert user.sport == "Basketball"
    assert user.level == "Amateur"
    assert user.streak_points == 0

def test_registro_entrenamiento_puntos():
    """Prueba que entrenar calcule bien los puntos (10 fijos + 1 cada 5 min)."""
    user = CoachAI("Marcus", "Basketball")
    puntos = user.registrar_entrenamiento(20) # 10 fijos + (20 // 5) = 14 puntos
    
    assert puntos == 14
    assert user.streak_points == 14

def test_subir_de_nivel_pro():
    """Prueba que el usuario suba a nivel 'Pro' al alcanzar los 100 puntos."""
    user = CoachAI("Marcus", "Basketball")
    # Registramos un entrenamiento de 450 minutos para sumar suficientes puntos
    # 10 fijos + (450 // 5) = 100 puntos en total
    user.registrar_entrenamiento(450)
    
    assert user.streak_points >= 100
    assert user.level == "Pro"

def test_error_minutos_negativos():
    """Prueba que el sistema no permita minutos negativos y lance un error."""
    user = CoachAI("Marcus", "Basketball")
    
    # Verificamos que se levante la excepción ValueError
    with pytest.raises(ValueError):
        user.registrar_entrenamiento(-10)
        
def test_subir_de_nivel_semi_pro():
    """Prueba que el usuario suba a nivel 'Semi-Pro' al alcanzar entre 50 y 99 puntos."""
    user = CoachAI("Marcus", "Basketball")
    # Registramos un entrenamiento de 200 minutos
    # 10 fijos + (200 // 5) = 50 puntos exactos
    user.registrar_entrenamiento(200)
    
    assert user.streak_points == 50
    assert user.level == "Semi-Pro"