#===========================
# Chan Campos Ashanty Iyari
#===========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2024
#===========================

#=============================
# Importar numba, numpy y time
#=============================
from numba import jit
import numpy
import time

#===============================
# Loop cualquiera en Python puro
#===============================
def lento(a):
    t = 0.0
    # Para cada renglón
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

#====================
# Loop sin intérprete
#====================
@jit(nopython=True)
def rapido(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

#============================================
# Arreglo unidimensional lleno del 0 al 10000
# convertido en matriz de 100x100
#============================================
x = numpy.arange(10000).reshape(100,100)

#====================================================
# La primera llamada incluye el tiempo de compilación
#====================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo  incluyendo compilación = %s" % (end-start))

#==========================================================
# La segunda llamada es para obtener el tiempo de ejecución
#==========================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo de ejecución en numba =%s" %(end-start))

#========================================
# Tiempo para la función sin optimización
#========================================
start = time.time()
lento(x)
end = time.time()
print("Tiempo de ejecución en python puro= %a" %(end-start))