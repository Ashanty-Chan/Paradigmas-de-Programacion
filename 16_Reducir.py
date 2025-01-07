#================================================
# Chan Campos Ashanty Iyari
# IPN ESFM Licenciatura en Matemática Algorítmica
# Octubre 2024
#================================================

#=========================================
# Uso de reducciones (colapsar resultados)
#=========================================

#================================================
# Multiplicación de todos los números en la lista
#================================================
from functools import reduce
bigdata = [7,10,9,22,12,6,4,19,1,45]

#=============
# Función x*y
#=============
multiplicar = lambda x,y: x*y

#=============
# Función x+y
#=============
suma = lambda x,y: x+y # Define the 'suma' function for addition


print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#=========================================================
# Reduce le aplica la función por pares a los resultados y
# el siguiente elemento comenzando con los dos primeros
# elementos
#==========================================================