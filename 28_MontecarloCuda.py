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

#=======================================================
#  Kernel de cuda para simulación Montecarlo en el GPU
#=======================================================
@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out):
    ii = cuda.grid(1)
    #===========================================================
    # Calcular pi dibujando puntos (x, y) al azar y encontrando
    # la fracción de ellos que cae dentro del círculo unitario
    #===========================================================
    cae_adentro = 0
    for i in range(iteraciones):
        # Pares al azar diferentes en (-1,1) para cada proceso ii
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        # Contar los que caen dentro del círculo de radio 1
        if x**2 + y**2 <= 1.0:
            cae_adentro += 1
    #======================================
    #  Escribir resultado para proceso ii
    #======================================
    out[ii] = 4.0 * cae_adentro / iteraciones

#========
#  MAIN
#========
if __name__ == "__main__":
  #=======================
  #  Procesos para cuda
  #=======================
  N = 26214400
  hilosporbloque = 128
  bloques = int(N/hilosporbloque)

  #============
  #  Semilla
  #============
  seed = random.randint(-1000,1000)
  rng_states = create_xoroshiro128p_states(hilosporbloque*bloques, seed)

  #================================
  #  Arreglo de salida (escritura)
  #================================
  out = np.zeros(hilosporbloque*bloques, dtype=np.float64)
  out_d = cuda.to_device(out)

  #========================================
  #  Correr en paralelo el kernel de cuda
  #========================================
  iterar = 10000
  calcularpi_kernel[bloques, hilosporbloque](rng_states, iterar, out_d)
  out_d.copy_to_host(out)
  print("Muestras totales = ", iterar*N)
  print("pi =", out.mean())