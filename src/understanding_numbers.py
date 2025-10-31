# Numbers

"""

    Integers - Enteros

    Son numeros sin punto decimal
    -infty, ..., -3, -2, -1, 0, 1, 2, 3, ..., infty

    Ejemplo:

        # Tipo dinamico
        age = 33

    Los podemos sumar (+), restar (-), multiplicar (*) y dividir (/)
    
    Potencia (**2, **3)

    Modulo (Dividiendo%Divisor)

"""

number_1 = 39
number_2 = 13

suma = number_1 + number_2
resta = number_1 - number_2
multiplicacion = number_1 * number_2   
division = number_1 / number_2
modulo = number_1 % number_2
potencia = number_1 ** 2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Modulo:", modulo)
print("Potencia:", potencia)

print("La suma es del tipo ", type(suma))
print("La resta es del tipo ", type(resta))
print("La multiplicacion es del tipo ", type(multiplicacion))
print("La division es del tipo ", type(division))
print("El modulo es del tipo ", type(modulo))  
print("La potencia es del tipo ", type(potencia))

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
