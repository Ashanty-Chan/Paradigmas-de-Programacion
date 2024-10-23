== == == == == == == == == == == == == == == == == == == == == == == ==
# Chan Campos Ashanty Iyari
# ESFM IPN Licenciatura en Matemática Algorítmica
# Octubre 2024
# ================================================

from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario


# ==============================================
# Implementa la interface RepositorioDeUsuarios
# ==============================================
class SistemaDeArchivos(REpositorioDeUsuarios):
    __directorio: str

    def __init__(mi, directorio: str):
        mi.__directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi.__directorio}")

    def guardar(mi, usuario: Usuario) -> None:
        xml = f"</root></name>{usuario.getNOmbre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"GUardando usuario en el archivo :{mi.__directorio}/{usuario.getNOmbre()}")
        print(xml)

        def cerrar(mi) -> NOne:
            print("Cerrando el archivo")