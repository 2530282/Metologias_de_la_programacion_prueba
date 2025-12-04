"""
    Docstring para understanding_while_loop_104.py

    Utilizamos el while loop para ejecutar un bloque de código mientras una condición sea verdadera.

    Estructura básica del while loop en Python:

        while condición:
            # bloque de código a ejecutar

"""
# Ejemplo básico de un while loop
# Verificar si un número esta en un rango específico (10 y entre 20)

while True: # while loop infinito
    try:
        number = int(input("Ingresa un número ENTERO entre 10 y 20: "))

        if number < 20 and number > 10:
            print("Numero dentro del rango, Felicitaciones!")
            break # Salir del loop
        else:
            print("Número fuera del rango, intenta de nuevo.")
    except ValueError: # Manejar la excepción si la entrada no es un número válido
        print("Por favor, ingresa un número válido.")
    except KeyboardInterrupt: # KeyboardInterrupt para manejar la interrupción del usuario
        print("\nPrograma terminado por el usuario.")
        break # Salir del loop en caso de interrupción del usuario

print("Fin del programa.")
# Nota: El uso de 'break' permite salir del loop cuando se cumple la condición deseada.
