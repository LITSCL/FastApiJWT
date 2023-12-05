from fastapi import HTTPException
from datetime import datetime, timedelta
import jwt

GLOBAL_SECRET = "SECRET"
GLOBAL_ALGORITHM = "HS256"

def codificar_token(usuario_nombre: str) -> str:
	payload: dict = {
		"exp": datetime.utcnow() + timedelta(days = 0, minutes = 1, seconds = 0),
		"iat": datetime.utcnow(),
		"sub": usuario_nombre
	}
	token: str = jwt.encode(payload, GLOBAL_SECRET, algorithm = GLOBAL_ALGORITHM)
	return token

def decodificar_token(token: str) -> str:
	try:
		payload: dict = jwt.decode(token, GLOBAL_SECRET, algorithms = [GLOBAL_ALGORITHM])
		return payload
	except jwt.ExpiredSignatureError:
		raise HTTPException(status_code = 401, detail = "SERVIDOR: El token ha expirado")
	except jwt.InvalidTokenError:
		raise HTTPException(status_code = 401, detail = "SERVIDOR: El token no es válido")