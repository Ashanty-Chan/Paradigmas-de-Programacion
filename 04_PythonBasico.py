#==========================
# Chan Campos Ashanty Iyari
#==========================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN Septiembre 2024
#==========================

#==========================
# Conjunto en Python
#==========================
even_nums = {2, 4, 6, 8, 10}   # conjunto de números pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1, 'Jonathan', 2205, True}  # conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 4, 4, 5, 7, 7}
print(nums)

#===================================
# Convertir secuencia a conjunto
# No lo genera en orden
#===================================
s = set('Hola')
print(s)
s = set(5,4,3,2,1))    # tupla a conjunto
print(s)

#=============================================
# De diccionario a conjuto: conjunto de llaves
#=============================================
d = {2:'dos',4:'cuatro'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(num,s)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1s2  # Unión
print(su)

si = s1&s2   # Intersección
print(si)

sr = s1-s2  # Diferencia de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2   # Diferencia simétria
print(ss)

#========================
# Uso de diccionarios
#========================

