#==============================================
# Chan Campos Ashanty Iyari
#==============================================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM-IPN sept-2024
#=============================================

'''ESTE ES UN SUPERCOMENTARIO
   DE INICIO A NUESTRO RESUMEN

'''

#============================================
# Operaciones Básicas
#===========================================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)  #raíz cuadrada
print (10%2)
print (10%0.1)  #exclusivo en python

#=========================================
# Para saber el tipo de objeto se usa type
#========================================
t=0
print(type(t))  #entero
t=3.6
print(type(t))  #real (flotante)
t=True
print(type(t))  #booleano (bool)

#=======================================
# Mensajes a pantalla
#======================================
print("ESte es un comando de python. ","ESte es otro enunciado.", t)
print('id: ', 1)
print('Nombres:', 'Steve')
print('Apellidos: ', 'Jobs')
print(("vamos a sumar esto"+" con esto otro")

#======================================
#Continuar una instrucción en varios renglones
#=============================================
if 100 > 99 and\
   200 <= 300 and \
   True != False:
       print('¡Hola a todos!')

#============================================
#Comandos diferentes en la misma línea
#===========================================
print("Hola "); print("tu")

#==========================================
# Usando paréntesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#===========================================
lista = [1, 2, 3, 4, 
        5, 6, 7, 8, 
        9, 10, 11, 12]

matriz = [ [1, 2, 3, 4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#==================================================================
# Identación estricta para procesos dependientes de : (dos puntos)
#=================================================================
if  10>2:
   print("diez es mayor que dos")
   print("otra identación")
for i in lista:
   print(i)
   print("ok")
if 10>2:
   print("verdadero")
   if 5<30:
      print("verdadero")
elif 7>2   # comienza segundo condicional, así mismo "elif" es para evaluar una cadena de múltiples condiciones
print("esto no se imprimira")
else: 
print("aquí nunca llega")

#==============
# Funciones
#==============
def saludar(nombre):
   print("Hola ", nombre)
   print("Bienvenido al tutorial de Python")

saludar("Ashanty")

   






 









 























 






















