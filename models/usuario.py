from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str = None
    clave: str = None
