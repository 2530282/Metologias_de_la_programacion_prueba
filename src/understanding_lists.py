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
"""
print("\nAgregar elementos a una lista:Metodo insert()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)  # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles[0])  # Salida: ducati