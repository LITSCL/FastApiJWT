from fastapi import APIRouter, Depends

from dependencies.autorizacion_dependence import AutorizacionDependence
from controllers.usuario_controller import save_usuario, iniciar_sesion, acceso_sin_proteccion, acceso_con_proteccion

dependencia_autorizacion: object = Depends(AutorizacionDependence().get_dependencia)

router: object = APIRouter()

router.add_api_route("/save-usuario", save_usuario, methods = ["POST"], response_model = dict, tags = ["modelo_usuario"])
router.add_api_route("/iniciar_sesion", iniciar_sesion, methods = ["POST"], response_model = dict, tags = ["modelo_usuario"])
router.add_api_route("/acceso-sin-proteccion", acceso_sin_proteccion, methods = ["GET"], response_model = dict, tags = ["modelo_usuario"])
router.add_api_route("/acceso-con-proteccion", acceso_con_proteccion, methods = ["GET"], response_model = dict, dependencies = [dependencia_autorizacion], tags = ["modelo_usuario"])

rutas_usuario: object = router