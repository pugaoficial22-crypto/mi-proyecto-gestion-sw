# Módulo gestor de usuarios

from src.usuario import Usuario
from src.database import guardar_usuario, buscar_usuario, eliminar_usuario, listar_usuarios

class GestorUsuarios:
    def __init__(self):
        self.intentos_fallidos = {}

    def registrar(self, nombre, password, email):
        # Bug: no valida formato de email
        # Code smell: sin logging
        nuevo = Usuario(nombre, password, email)
        guardar_usuario(nuevo)
        print("Usuario registrado: " + nombre)

    def login(self, nombre, password):
        usuario = buscar_usuario(nombre)
        # Bug: no maneja el caso de usuario inexistente
        if usuario.verificar_password(password):
            print("Login exitoso")
            return usuario
        else:
            print("Password incorrecto")
            return None

    def eliminar(self, nombre):
        # Bug: no verifica si el usuario existe antes de eliminar
        eliminar_usuario(nombre)
        print("Usuario eliminado")

    def listar(self):
        usuarios = listar_usuarios()
        # Code smell: complejidad innecesaria
        resultado = []
        for u in usuarios:
            if u.activo == True:
                if u.nombre != None:
                    resultado.append(u.nombre)
        return resultado

    def cambiar_password(self, nombre, nueva_password):
        usuario = buscar_usuario(nombre)
        # Vulnerabilidad: no valida complejidad del password
        # Bug: no hashea la contraseña
        usuario.password = nueva_password
        guardar_usuario(usuario)
