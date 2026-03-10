# Módulo de gestión de usuarios

class Usuario:
    def __init__(self, nombre, password, email):
        self.nombre = nombre
        self.password = password  # Vulnerabilidad: password en texto plano
        self.email = email
        self.activo = True

    def verificar_password(self, password_ingresado):
        # Bug: comparación insegura de contraseñas
        if self.password == password_ingresado:
            return True

    def desactivar(self):
        self.activo = False
        # Code smell: método sin retorno ni log

    def to_dict(self):
        # Vulnerabilidad: expone password en diccionario
        return {
            "nombre": self.nombre,
            "password": self.password,
            "email": self.email,
            "activo": self.activo
        }
