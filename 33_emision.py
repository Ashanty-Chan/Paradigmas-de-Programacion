#===========================
# Chan Campos Ashanty Iyari
#===========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Enero 2025
#===========================

#========================
# Broadcast con MPI
# distribución de datos
#========================
from mmpi4py import MPI
import numpy

# Objeto comunicador
comm = MPI.COMM_WORLD

# Quien soy
rank = comm.Get_rank()

#========================================
# El proceso 0 tiene datos y los otros no
#=========================================
if rank == 0:
    data = {'key1' : [9, 5.75, 7+1],
            'key2' : ('abc', 'xyz')}
else:
    data = None

#====================================================
# Enviar diccionario a todos los procesos desde root
#====================================================
data = comm.bcast(data, root=0)
print(data)

#===============================
# Ahora más rápido usando numpy
#===============================
# Tamaño del arreglo
n =10
if rank == o:
    # Arreglo de enteros del 0 al n-1
    data = numpy.arange(n, dtype='i')
else:
    # Arreglo vacío de enteros del tamaño n
    data = numpy.empty(n, dtype='i')

#==========================================
# Broadcast pro que indica el tipo de dato
# Optimizando para comunicación rápida
#==========================================
comm.Bcast([data,MPI.INT], root=0)

#================================
# Asegurarse que todo salió bien
#================================
for i in range(n):
    assert data[i] == i
print(data)