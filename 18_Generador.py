#============================
# Chan Campos Ashanty Iyari
#============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Noviembre 2024
#============================

#=======================================
# yield transforma la función a iterador
#=======================================
def migenerador():
    print("Primero")
    yield 20
    print("Segundo")
    yield 70
    print("Tercero")
    yield "hello"

#===================
# gen es un iterador
#===================
gen = migenerador()
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)