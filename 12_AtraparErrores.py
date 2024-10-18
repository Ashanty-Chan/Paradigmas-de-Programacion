#===========================
# Chan Campos Ashanty Iyari
#===========================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN octubre 2024
#===========================

#==================================================
# La clase ClienteBancario está en el subdirectorio
# aplicación/banco/
#==================================================
from aplicacion.banco.cliente_bancario import ClienteBancario

#===========================================
# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#===========================================

#=========================================
# Error por sacar más dinero del que tiene
#=========================================
try:
    cliente = ClienteBancario("Emiliano Iván","Nava Flores", 22, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
#=============================================
# EXception es el objeto más general del error
#=============================================
except Exception as e:
    print("Error: " + str(e))

#==================================
#Error por usar un atributo privado
#==================================
try:
    print(cliente._nombres)
except Exception as ex:
    print("Error: " + str(ex))

#===============
# Forma correcta
#===============
print(cliente.nombres)