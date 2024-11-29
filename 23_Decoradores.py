# ===========================
# Chan Campos Ashanty Iyari
# ===========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN 2024
# ===========================

# =================================
# Función que regresa otra función
# =================================
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# ===============
# Función saludo
# ===============
def say_hi():
    return 'hello there'


# =========================
# Generar y correr función
# =========================
decorate = uppercase_decorator(say_hi)
print(decorate())


# ========================
# Utilizar como decorador
# ========================
@uppercase_decorator
def say_hi():
    return 'hello there'


# ====================================
# Correr función pasada por decorador
# ====================================
print(say_hi())
