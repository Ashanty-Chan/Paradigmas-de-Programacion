#=================================
# Chan Campos Ashanty Iyari
# ESFM IPN Matemática Algorítmica
# Octubre del 2024
#=================================

#=========================================================
# Del directorio aplicacion, el subdirectorio repositotio,
# el archivo basededatos.py : trae el objeto Basededatos
#=========================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#=========================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo s3.py : trae elobjeto S3
#=========================================================
from aplicacion.repositorio.s3 import S3

#===================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#===================================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#======================================================
# Del directorio aplicacion, el subdirectorio modelos,
# el archivo usuario.py : trae elobjeto Usuario
#======================================================
from aplicacion.modelos.usuario import Usuario

#===========================================================================
# Del directorio aplicacion, el subdirectorio negocios,
# el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#===========================================================================
from aplicacion.negocio.manejodeinscripciones import ManejoDeInscripciones

#========================
# Crear el objeto Usuario
#========================
usuario = Usuario("Daniel","Dominguez",33)

#===================
# Crear el objeto s3
#===================
repositorioS3 = S3("543543543","mdft225689","MiComputadora")

#============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#==================================
# Crear el objeto sistemadearchivos
#==================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#============================
# Crear el objeto basededatos
#============================
repositorioBaseDeDatos = BaseDeDatos("besthost","subhost","subhost456")

#===========================================================
#Interface inscribirUsuario del objeto ManejoDeInscripciones
#===========================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

