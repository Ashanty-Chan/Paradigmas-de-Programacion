#==========================
# Chan Campos Ashanty Iyari
#==========================
# Matemática ALgorítmica
# Paradigmas de Programación
# ESFM IPN Septiembre 2024
#==========================

#============================================
# Listas
# Las listas pueden ser de objetos diferentes
#=============================================
miprimeralista = []  # Lista vacía
print(miprimeralista)

#=======================
# Llenado de lista
#=======================
miprimeralista = [1,"Laura",2.36,"Bosco","Daniel","Carmen",True]
print(miprimeralista)

#====================================
# list: hacer una lista
# range(i,j): secuencia de i hasta j-1
#=====================================
nums = list(range(1,65))

for i in nums: 
    print(i)

#======================================
# Incluir nuevos elementos en una lista
#======================================
nums.append(65)
nums.append(22)
nums.append(18)
print(nums)

#=============================
# Quitar elementos de la lista
#=============================
nums.remove(65)
print(nums)

#==============================
# Quitar elemento con índice i
#==============================
i = 65
del nums[i]
print(nums)

#================
# Borrar la lista
#================
del nums

#===============
# Sumar listas
#===============
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#============================
# Llenado a mano
#============================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#================================
# Generar una tupla con una lista
#=================================
potencial = tuple(potencial)
print(potencial[100])

