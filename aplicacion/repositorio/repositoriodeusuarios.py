#============================================
# Chan Campos Ashanty Iyari
# ESFM Licenciatura en Matemática Algorítmica
# Octubre del 2024
#============================================

from aplicacion.modelos.usuario import Usuario

#=============================
# Este objeto es una interface
#=============================
class RepositorioDeUsuarios:
    def abrir(mi) -> None:
        pass
    def guardar(mi,usuario:Usuario) -> None:
        pass
    def cerrar(mi) -> None:
        pass
