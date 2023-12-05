from passlib.context import CryptContext

def encriptar_clave(clave: str) -> str:
	encriptador: object = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
	return encriptador.hash(clave)

def validar_clave(clave: str, clave_encriptada: str) -> bool:
	encriptador: object = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
	return encriptador.verify(clave, clave_encriptada)