# Tests básicos del sistema

from src.usuario import Usuario
from src.gestor import GestorUsuarios

def test_crear_usuario():
    u = Usuario("brandon", "pass123", "brandon@test.com")
    assert u.nombre == "brandon"
    assert u.activo == True

def test_verificar_password_correcto():
    u = Usuario("brandon", "pass123", "brandon@test.com")
    assert u.verificar_password("pass123") == True

def test_gestor_registrar():
    gestor = GestorUsuarios()
    gestor.registrar("ana", "1234", "ana@test.com")
    resultado = gestor.listar()
    assert "ana" in resultado

def test_to_dict():
    u = Usuario("carlos", "secret", "carlos@test.com")
    d = u.to_dict()
    assert "nombre" in d
