#===========================
# Chan Campos Ashanty Iyari
#==========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Noviembre 2024
#============================

#============================
#       Tres listas
#============================
mi_lista = [5,4,3]
tu_lista = (100,200,300)
su_lista = (20,30,40)

#============================
# Función multiplicar por dos
#============================
def multiplicar_por2(elemento):
    return elemento*2

#=============================
# Función filtra pares
# % módulo != no es igual
# lo regresa solo si es impar
#=============================
def solo_impar(elemento):
    return elemento % 2 !=0

#===========================================
# Lista de pares de datos de las dos listas
# zip sirve para juntar listas
# list es para que haga toda la lista
#===========================================
print(list(zip(mi_lista, tu_lista, su_lista)))

una_lista = ["A", "B", "C", "D", "E", "M", "N", "L"]

#============================================
# Crear conjunto de elementos que se repiten
#============================================
duplicados = set([x for x in una_lista if una_lista.count(x) > 1])
print(duplicados)

#==================================
# Expresión generadora
# Contiene un iterador
# range(5) es un iterador de 0 a 4
# Utiliza ()
#==================================
cuadrados = (x*x for x in range(5))

#==================================================
# next llama a la siguiente evaluación del iterador
#==================================================
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

#=============================
# Pasar una función generadora
#=============================
import math

#================================
# suma los elementos del iterador
#================================
print(sum(x*x for x in range(5)))

#=========================================
# Lista de comprensión pasada como función
# Arma la lista para usar []
#=========================================
numeros_pares = [x for x in range(21) if x%2 == 0]
print([x for x in range(21) if x%2 == 0])
print(numeros_pares)