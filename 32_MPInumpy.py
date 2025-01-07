#===========================
# Chan Campos Ashanty Iyari
#===========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Enero 2025
#===========================
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#===========================================
# Se inidca el tipo de datos explícitamente
# Este ejemplo solo tiene dos procesos
#===========================================

#===========================
# EJEMPLO 1 USANDO ENTEROS
#==========================
if rank ==0:
    #===============================
    # Arreglo de enteros del 0 al 9
    #===============================
    data = numpy.atange(10, dtype='i')
    #================================================
    # Envío bloqueante especificando el tipo de dato
    # tag es un identificador del mensaje
    #================================================
    comm.Send([data, MPI.INT], dest=1, tag=77)

elif rank == 1:
    data = numpy.empty(10, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print(data)

#==========================================================
# También se puede sin decir el tipo de dato, pero deben
# coincidir el tipo de arreglos a los extremos del mensaje
#===========================================================

#============================
# EJEMPLO 2 USANDO FLOTANTES
#============================
if rank == 0:
    data = numpy.atange(10, dtype=numpy.float64)
    comm.Send(data, desnt=1, tag=13)
elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source=0, tag =13)
    print(data)