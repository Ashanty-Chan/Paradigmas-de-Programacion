#==========================
# Chan Campos Ashanty Iyari
#==========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2024
#===========================
from __future__ import print_function, absolute_import
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128p_uniform_float64
import numpy as np
import random 

#====================================================
# Kernel de cuda para simulación Montecarlo en el GPU
#====================================================
@cuda.jit
def calcularpi_kernel(rng_state, iteraciones, out):
    ii = cuda.grid(1)
    #===========================================================
    # Calcular pi dibujando puntos (x, y) al azar y encontranado 
    # la fracción de ellos que cae dentro del círculo unitario
    #===========================================================
    cae_dentro = 0
    for i in range(iteraciones):
        # Pares al azar diferentes en (-1,1) para cada proceso ii
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        # Contar los que caen dentro del círculo de radio 1 
        if x**2 + y**2 <= 1.0:
            cae_dentro += 1
        #===================================
        # Escribir resultado para proceso ii
        #===================================
        out[ii] = 4.0 * cae_dentro / iteraciones

#===================
# Procesos para Cuda
#===================
N = 222729
hilosporbloque = 128 
bloques = int(N/hilosporbloque)

#=========
# Semillas
#=========
seed1 = random.uniform(-1,1)
print(seed1)
seed2 = random.seed(seed1)
print(seed2)
seed = random.randint(-12000,12000)
print(seed)
rng_states = create_xoroshiro128p_states(hilosporbloque*bloques, seed)

#==============================
# Arreglo de salida (escritura)
#==============================
out = np.zeros(hilosórbloque*bloques, dtype=np.float64)

#=====================================
# Correr en paralelo el kernel de Cuda
#=====================================
calcularpi_kernel[bloques, hilosporbloque](rng_states, 500000, out)
print('pi:', out.mean())


