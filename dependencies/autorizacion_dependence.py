from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from helpers.autorizacion_helper import decodificar_token

class AutorizacionDependence():

    def get_dependencia(self, token: HTTPAuthorizationCredentials = Security(HTTPBearer())) -> str:
        payload: dict = decodificar_token(token.credentials)
        suscriptor: str = payload["sub"]
        return suscriptor
