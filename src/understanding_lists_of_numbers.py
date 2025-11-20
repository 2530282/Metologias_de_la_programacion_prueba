"""
    Las listas tambien pueden almacenar números y de echo son ideales para almacenarlos.

    Python ofrece cantidad de funciones integradas para trabajar con lists de números.

    Por ejemplo, función range() :

"""

# La función range() genera una secuencia de números en un rango especificado.
# Por ejemplo, para generar una lista de números del 0 al 9, podemos usar range(10):
numbers = list(range(10))
print("Números del 0 al 9:", numbers) # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers)) # Salida: <class 'list'>

# Podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num)  # Salida: Números del 0 al 9, uno por línea
    print(type(num))  # Salida: <class 'int'>
    #print(type(num))   Salida: <class 'int'>

print("\nNumeros del 1 al 4: ")
for num in range(1, 5):
    print(num)

numbers_1_to_4 = list(range(1, 5))
print(numbers_1_to_4) # Salida: [1, 2, 3, 4]

print("\nNumeros Impares")
for num in range(1, 10, 2): # Numeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) # Salida: [1, 3, 5, 7, 9]

print("\nNumeros Pares")
for num in range(2, 10, 2): # Numeros pares del 2 al 8
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers) # Salida: [2, 4, 6, 8]

## Podemos crear cualquier tipo de listas de números
## Utilizando range() y list()
print("\n Primeros 10 numeros cuadrados: ")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares) # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Metodos built-in para listas de números
print("\n Métodos built-in para listas de números")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lista de dígitos: {digits}")
print("Valor mínimo:", min(digits))  # Salida: 0
print("Valor máximo:", max(digits))  # Salida: 9
print("Suma de todos los dígitos:", sum(digits))  # Salida: 45

# Pasado al cuaderno