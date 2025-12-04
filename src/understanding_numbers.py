# Numbers

"""

    Integers - Enteros

    Son numeros sin punto decimal
    -infty, ..., -3, -2, -1, 0, 1, 2, 3, ..., infty

    Ejemplo:

        # Tipo dinamico
        age = 33

    Los podemos sumar (+), restar (-), multiplicar (*) y dividir (/)
    
    Potencias (**2, **3)

    Modulo (Dividiendo%Divisor)

"""

number_1 = 39
number_2 = 13

suma = number_1 + number_2
difference = number_1 - number_2
multiplication = number_1 * number_2   
division = number_1 / number_2
modulo = number_1 % number_2 
power = number_1 ** 2

print("Suma:", suma)
print("Difference:", difference)
print("multiplication:", multiplication)
print("Division:", division)
print("Modulo:", modulo)
print("power:", power)

print("La suma es del tipo ", type(suma))
print("La difference es del tipo ", type(difference))
print("La multiplication es del tipo ", type(multiplication))
print("La division es del tipo ", type(division))
print("El modulo es del tipo ", type(modulo))  
print("La power es del tipo ", type(power))

# Floats

"""

    Floats - Enteros

    Son numeros con punto decimal, van desde
    -infty  infty

    Ejemplo:

        # Tipo dinamico
        age = 25.5

    Los podemos sumar (+), restar (-), multiplicar (*) y dividir (/)
    
"""

print(0.1 + 0.1)
print(0.1 - 0.1)
print(2* 0.1)
print(2* 0.2)

print(0.1 + 0.2)
print(3* 0.2)


## Imprimir la edad de alguien
age = 33
message = "Emiliano tiene " + str(age) + " años."
print(message)

"""
    TypeError: Python no puede reconocer el tipo de información que se está utilizando.

    Para convertir a string utilizo: str()
"""

message = f"Emiliano tiene {age} años."
print(message) 


# Pasado al cuaderno 