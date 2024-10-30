#===========================
# Chan Campos Ashanty Iyari
#===========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Octubre 2024
#===========================

#===============
# Uso de filtros
#===============

#=======================================================
# Hacer una lista de los números por arriba del promedio
#=======================================================

# Módulo de estadística
import statistics

bigdata = [7.5,2.6,0.2,9.3,1.5,-0.8]
promedio = statistics.mean(bigdata)
print(promedio)

#===================================================================
# Hazme una lista de elementos que cumplan la condición x > promedio
# filter(condición,datos)
#===================================================================
print(list(filter(lambda x: x > promedio, bigdata)))

#==================
# Limpiar los datos
#==================
paises = ["", "México", "", "Cuba", "", " Colombia", "España","", "Brasil", "","","Estados Unidos", "Holanda"]

#===============================
# Filtra lo que no contiene nada
#===============================
print(list(filter(None, paises)))