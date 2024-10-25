#================================================
# Chan Campos Ashanty Iyari
#================================================
# Paradigmas de Programación
# ESFM IPN Licenciatura en Matemática Algorítmica
# Octubre 2024
#================================================

#==================
# Función pura x**2
#==================
def alcuadrado(x):
    return x*x

#==================
# Función pura x**3
#==================
def alcubo(x):
    return x*x*x

#==========================
# Mapeo de una función pura
#==========================
def mapeo(func,lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado,[7.5,22,2.9,9.1,5.6,10j,3,4])
cubos = mapeo(alcubo,[8,7,6,5,4,3,2,1])
print(cuadrados)
print(cubos)

#==============================
# Funciones dentro de funciones
#==============================
def en_mayusculas(texto):
    return texto.upper()

def en_minusculas(texto):
    return texto.lower()

def saludar(func):
    saludo = func("Hola, ¿qué tal?")
    print(saludo)

#============
# Con strings
#============
saludar(en_mayusculas)
saludar(en_minusculas)

#=========================================
# Funciones abstractas dentro de funciones
# Su resultado es otra función
#=========================================
def divisor(x):
    def dividiendo(y):
        return y/x
    return dividiendo

#=================================
# Primero generamos la función y/2
#=================================
división = divisor(2)
#=============================
# La usamos para calcular 3/2
#=============================
print(división(3))

#====================================
# Uso de la función map con una lista
#====================================

#===================================
# Lista de ciudades y su temperatura
#===================================
temps = [("México",30), ("Boston",16), ("Chicago",25), ("Pekin",29), ("Houston",16), ("Los Angeles", 24), ("Londres",14), ("Hong Kong", 31), ("Shangai",13)]

C_a_F = lambda datos: (datos[0], (7/5)*datos[1] +32)
print(list(map(C_a_F,temps)))