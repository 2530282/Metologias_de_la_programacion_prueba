magos = ["ron", "harry", "hermione", "draco"]
for mago in magos:
    print(mago)
    print(mago.upper())
    print(f"{mago.title()}, es un gran mago!")
    print("\n")  # Agrega una línea en blanco para separar la salida de cada mago
    "La identación son 4 espacios antes de cada accion"

    """
    
        Identación en Python

            Pyhton utiliza la identación para determinar cuando una linea de codigo esta conectada a la linea de codigo esta conectada a la linea de codigo anterior.

            Basicamente, se utilizan 4 espacios en blanco para obligarnos a escribir código ordenada y estructurado.

    """

# No olvidemos identificar (donde se necesita)
# Ejemplo:
magos = ["ron", "harry", "hermione", "draco"]
for mago in magos:
#print(mago) # Error - el for necesita al menos un elemento
    print(mago) #Solution

# Identation Error
# Logical error -
magos = ["ron", "harry", "hermione", "draco"]
for mago in magos:
    print(mago)
# print(f"Great {mago}!, I can´t wait to see you next trick!") Error
    print(f"Great {mago}!, I can´t wait to see you next trick!")


# Identación innecesaria
message = "Hello Python world!"
#print(message) # Error de identación innecesaria

# Logical error -
magos = ["ron", "harry", "hermione", "draco"]
for mago in magos:
    print(mago)
# print(f"Great {mago}!, I can´t wait to see you next trick!") Error
    print(f"Great {mago}!, I can´t wait to see you next trick!")
print("Thank you everyonre, that was a great magic show!") # Solución identar a la izquierda

# Error de syntaxis
magos = ["ron", "harry", "hermione", "draco"]
for mago in magos: # Error de syntaxis, falta el ":"
    print(mago) 