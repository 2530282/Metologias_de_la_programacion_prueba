"""
    Docstring para understanding_while_centinel_104

    Vamos a realizar un programa que sume pesos mexicanos hasta que el usuario escriba 
    la palabra "salir"
    
    El programa tambien debe decirme cuantos números ingreso el usuario, 
    cual fue el minimo y cual fue el máximo.

"""
sum_numbers = 0.0
counter = 0
minimum = None # Inicializamos el mínimo como None para poder compararlo después
maximum = None

while True:

    print("Ingresa la palabra 'salir' para terminar")
    user_input = input("Ingresa una cantidad (MXN): ")

    # Centinel
    if user_input.lower() == "salir":
        break

    try:
        quantity = float(user_input)
    except ValueError:
        print("Cantidad inválida, ingresa nuevamente.")
        continue # Salta a la siguiente iteración del ciclo
    except KeyboardInterrupt:
        break

    counter += 1 # counter = counter + 1 # Estructura contadora
    sum_numbers += quantity # sum_numbers = sum_numbers + quantity # Estructura acumuladora

    if minimum is None or quantity < minimum: # Verifica si es el primer número o si es menor que el actual
        minimum = quantity  # Actualiza el mínimo si es el primer número o si es menor que el actual
    
    if maximum is None or quantity > maximum:
        maximum = quantity  # Actualiza el máximo si es el primer número o si es mayor que el actual

print("SUM", sum_numbers)
print("CONTADOR", counter)
print("MINIMO", minimum)
print("MAXIMO", maximum)