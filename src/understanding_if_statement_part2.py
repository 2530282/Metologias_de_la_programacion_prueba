"""

    Vamos a realizar un programa que pregunte al usuario por su edad y muestre un mensaje
    difentes segun el rango de edad en el que se encuentre:

"""
try:
    age = int(input("Por favor, ingresa tu edad: "))
    if age >= 18:
        print("Eres mayor de edad.")
    elif age < 18:
        print("Eres menor de edad.") 
except: 
    print("Tuviste un error al ingresar la edad.")

print("Hola Emiliano")


try:
    age = int(input("Por favor, ingresa tu edad: "))
except: 
    age = -1
    print("Tuviste un error, ingresaste un caracter no valido.")

if age > 100:
    print("Tienes más de un siglo de vida.")
elif age >= 18 and age <= 100:
    print("Eres mayor de edad.")
elif age < 18 and age >= 0:
    print("Eres menor de edad.") 
else:
    print("La edad ingresada no es válida.")

print("Hola Emiliano")

"""
    Hacer un programa que pregunte la edad de una persona y responda lo siguiente:
        - Si la edad es menor e igual a 4, entonces la entrada es gratuita.
        - Si la edad es menor e igual a 18, pero mayor que 4, entonces la entrada cuesta $200
        - Si la edad es mayor a 18, entonces la entrada cuesta $400.
"""

# Multiple if
guisos = ["deshebrada", " asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("Hay asado")
else:
    print("No hay asado")
if "tamales" in guisos:
    print("Hay tamales")
else:
    print("No hay tamales")
if "salsa verde" in guisos:
    print("Hay salsa verde")
else:
    print("No hay salsa verde")

# Actividad
age = int(input("Por favor, ingresa tu edad: "))
if age <= 4:
    print("La entrada es gratuita.")
elif age <= 18 and age > 4:
    print("La entrada cuesta $200.")
elif age > 18:
    print("La entrada cuesta $400.")