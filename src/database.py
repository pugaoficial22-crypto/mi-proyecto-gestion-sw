# Módulo de base de datos

import os

# Vulnerabilidad: credenciales hardcodeadas
DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "admin1234"
DB_NAME = "usuarios_db"

usuarios_db = {}

def guardar_usuario(usuario):
    # Bug: no valida si el usuario ya existe
    usuarios_db[usuario.nombre] = usuario
    return True

def buscar_usuario(nombre):
    # Code smell: variable declarada pero no usada
    resultado = None
    encontrado = False
    for key in usuarios_db:
        if key == nombre:
            return usuarios_db[key]

def eliminar_usuario(nombre):
    # Bug: no maneja KeyError si no existe
    del usuarios_db[nombre]

def consulta_sql(nombre):
    # Vulnerabilidad crítica: SQL Injection
    query = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"
    return query

def listar_usuarios():
    return list(usuarios_db.values())
