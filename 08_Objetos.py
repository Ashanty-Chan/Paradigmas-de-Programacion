#===========================
# Chan Campos Iyari Ashanty
#===========================
# Paradigmas de programación
# Matemática Algorítmica
# ESFM IPN  Octubre 2024
#==========================

#=================================
# PROGRAMACIÓN ORIENTADA A OBJETOS
#=================================

#===============================
# Una clase para un objeto vacío
# No está tan vacío, necesita
# la palabra pass = pasar
#==============================
class ObjetoVacio:
    pass

#=================================================
# nada es la instanciación de la clase ObjetiVacio
#=================================================
nada = ObjetoVacio()
print(type(nada))

#================
# La clase llanta
#================
class Llanta:
    #===================================
    # Variable cuenta es de toda la clase
    #===================================
    cuenta = 0
    #===================================
    # Función constructora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #==================================
    def __init__(mi,radio=50,ancho=30,presión=1.5):
        # variable de la estructura completa llanta
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión

#=======================
# Objetos (instanciados)
#=======================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#==================================
# Objeto que contiene otros objetos
#==================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4
micoche = Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas: ",Llanta.cuenta) #Variable global de la clase
print("Presión de llanta 4 = ",llanta4.presión) #Presión  de la llanta 4
print("Radio de llanta 4 = ",llanta4.radio)
print("Radio de la llanta 3 = ",llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta1.presión)

#================
# Encapsulamiento
#================

#====================================================================
# Uso de la función de python property para poner y obtener atributos
# a variable protegidas con __
#===================================================================
class Estudiante:
   def __init__(mi):
       mi.__nombre = ''
   def ponerme_nombre(mi, nombre):
       print('se llamó a ponerme_nombre')
       mi.__nombre = nombre
   def obtener_nombre (mi):
       print('se llamó a obtener_nombre')
       return mi.__nombre
   nombre=property(obtener_nombre,ponerme_nombre)

#===================================
# Crear objeto estudiante sin nombre
#===================================
estudiante = Estudiante()

#======================================================================
# Ponerle nombre usuando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explícitamente la función)
#======================================================================
estudiante.nombre = "Carlos"

#==================================================================
# Obtener el nombre con el método obtener_nombre
# _nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explucítamente a la función obtener_nombre)
#==================================================================
print(estudiante.nombre)

#Esto no funciona
# print(estudiante._nombre)

#===================
# Herencia de clases
#===================
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

def perimetro(mi):
    p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
    print("perimetro=",p)
    return p

#===================================
# Su hijo rectángulo
# Rectángulo es hijo de cuadrilátero
# Rectángulo(Cuadrilátero)
#===================================
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #========================
        # Constructor de su madre
        #========================
        super().__init__(a, b, a, b)

#===================
# Su nieto Cuadrado
# Hijo de rectángulo
#===================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area
     # def perímetro(self):
       # p = 4.0*self.lado1
       # print("perímetro =",p)
       # return p

#==================
# Crear un cuadrado
#==================
cuadrado1 = Cuadrado(5)

#=====================================================
# Llamar al método perímetro de su abuelo Cuadrílatero
#=====================================================
perimetro1 = cuadrado1.perimetro()

#===============================
# Llamar a su propio método área
#===============================
area1 = cuadrado1.area()

print("Perímetro = ", perimetro1)
print("Área = ", area1)

#============================================================
# Sobre-escribir un método de su madre o abuela o tatarabuela
# Es volver a definir una función ya existente
#============================================================