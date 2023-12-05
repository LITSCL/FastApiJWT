from fastapi import HTTPException

from models.usuario import Usuario
from helpers.encriptacion_helper import encriptar_clave, validar_clave
from helpers.autorizacion_helper import codificar_token

usuarios: list = []

async def save_usuario(usuario: Usuario) -> dict:
    usuario_obtenido: dict = dict(usuario)
    if (any(usuario["nombre"] == usuario_obtenido["nombre"] for usuario in usuarios)):
        raise HTTPException(status_code = 400, detail = "SERVIDOR: El usuario ya existe")
    clave_encriptada: str = encriptar_clave(usuario_obtenido["clave"])
    usuarios.append({
        "nombre": usuario.nombre,
        "clave": clave_encriptada
    })
    return usuarios[len(usuarios) - 1]

async def iniciar_sesion(usuario: Usuario) -> dict:
    usuario_obtenido: dict = dict(usuario)
    usuario_almacenado: dict = None
    for i in usuarios:
        if (i["nombre"] == usuario_obtenido["nombre"]):
            usuario_almacenado = i
            break
    if (not usuario_almacenado):
        if (not validar_clave(usuario_obtenido["clave"], usuario_almacenado["clave"])):
            raise HTTPException(status_code = 401, detail = "SERVIDOR: Credenciales de acceso incorrectas")
    token: str = codificar_token(usuario_obtenido["nombre"])
    return {
        "token": token
    }

async def acceso_sin_proteccion() -> dict:
    return {
        "mensaje": "SERVIDOR: Bienvenido"
    }

async def acceso_con_proteccion() -> dict:
    return {
        "mensaje": "SERVIDOR: Bienvenido"
    }