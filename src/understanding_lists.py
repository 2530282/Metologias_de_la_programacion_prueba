# LISTAS
# Una lista es una colección ordenada y mutable de elementos.
# Se definen utilizando corchetes [] y los elementos están separados por comas.
# Ejemplo de creación de una lista
fruits = ["manzana", "banana", "cereza"]
print(fruits)  # Salida: ['manzana', 'banana', 'cereza']

# Acceso a elementos
print(fruits[0].upper())  # Salida: manzana (acceso al primer elemento)
print(fruits[1])  # Salida: banana (acceso al segundo elemento)
print(fruits[2].title())  # Salida: cereza (acceso al tercer elemento)

# print(fruits[3])  # Esto generaría un error IndexError porque no hay cuarto elemento

# Acceder al último elemento
print(fruits[-1])  # Salida: cereza (acceso al último elemento)
print(fruits[-2])  # Salida: banana (acceso al penúltimo elemento)
print(fruits[-3])  # Salida: manzana (acceso al antepenúltimo elemento)

message = f"Mi fruta favorita es {fruits[0].title()}."
print(message)  # Salida: Mi fruta favorita es Manzana.

"""
    Agregar elementos a una lista
    - append(): Agrega un elemento al final de la lista.
"""
print("\nAgregar elementos a una lista:Metodo append()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
    Agregar elementos a una lista
        - insert(): Inserta un elemento en una posición específica de la lista.
    El metodo insert(index, element) toma dos argumentos:
         el índice donde se desea insertar el elemento y el elemento mismo.

    (index, element*)           *(elementos aqui se ocupan para funcionar el metodo)
"""
print("\nAgregar elementos a una lista:Metodo insert()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)  # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles[0])  # Salida: ducati
"""
                Experimento mio.
"""
print(motorcycles.append("ducati")) 

"""
    Eliminar elementos de una lista
    - del: Elimina un elemento en una posición específica de la lista. 
    La declaración del index elimina el elemento en esa posición especifica.
"""
print("\nEliminar elementos de una lista:Declaración del\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # Salida: ['yamaha', 'suzuki']
"""
    Eliminar elementos de una lista
    - pop(): Elimina y devuelve el último elemento de la lista.
    El método pop() no requiere argumentos y elimina el ultimo elemento de la lista.
"""
print("\nEliminar elementos de una lista:Metodo pop()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
firts_motorcycle = motorcycles.pop() # Sin nada entre las comillas es el ultimo dato de la lista.
print(motorcycles)  # Salida: ['honda', 'yamaha']
print(firts_motorcycle)  # Salida: suzuki
print(f"La primera motocicleta eliminada es: {firts_motorcycle.title()}.")

"""
    Eliminar elementos de una lista por valor
    - remove(): Elimina la primera aparición de un valor específico en la lista.
    El método remove() toma un argumento: el valor del elemento que se desea eliminar.
"""
print("\nEliminar elementos de una lista por valor:Metodo remove()\n")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]  
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("ducati")
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki'] 

names = ['anna', 'bob', 'charlie', 'david']
print(names)
deleted_name = input("\n \nIngrese el nombre que desea eliminar de la lista: ")
"Salto de pagina = \n"
names.remove(deleted_name.strip().lower())
"strip()= borrar espacios en blanco al inicio y al final"
print(names)

"""
    Ordenar listas

    Metodo de las listas: sort()
"""
cars = ["bmw", "audi", "ford", "kia"]
print(cars)  # Salida: ['bmw', 'audi', 'ford', 'kia']
cars.sort()
print(cars)  # Salida: ['audi', 'bmw', 'ford    
cars.sort(reverse=True) # Ordenar en orden descendente
print(cars)  # Salida: ['kia', 'ford', 'bmw', 'audi']

"""
    Método reverse()
    Invierte el orden de los elementos en la lista.
"""
motorcycles = ["mortalica", "honda", "ducati"]
print(motorcycles)  # Salida: ['mortalica', 'honda', 'ducati']
motorcycles.reverse()  # Invierte el orden de la lista
print(motorcycles)  # Salida: ['ducati', 'honda', 'mortalica']

"""
    Cantidad de elementos en una lista
    Metodo built-in len()
"""

Caricatures = ["one pice", "naruto", "bleach", "dragon ball"]
print("\n Metodo built-in len()\n")
print(len(Caricatures))  # Salida: 4

"""
    Método built-in

    sorted():
        Ordena una lista temporalmente sin modificar la lista original.

"""

favorite_students = ["jorge" , "jose" , "carlos", "emiliano"]
print(favorite_students)  # Salida: ['jorge', 'jose', 'carlos', 'emiliano']
print("Lista ordenada temporalmente",sorted(favorite_students))  # Salida: ['carlos', 'emiliano', 'jorge', 'jose']
print("Lista original: ", favorite_students)  # Salida: ['jorge', 'jose', 'carlos', 'emiliano']
print("Lista ordenada temporalmente",sorted(favorite_students, reverse = True))  # Salida: ['jose', 'jorge', 'emiliano', 'carlos']
print("Lista original: ", favorite_students)  # Salida: ['jorge', 'jose', 'carlos', 'emiliano']

