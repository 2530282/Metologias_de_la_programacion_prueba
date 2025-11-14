"""

    Una list comprenhenson combina el for loop y la creación de nuevos elementos en una sola linea
    de codigo y tambien, automaticamente agrega el nuevo elemento a la lista es decir sin utilizar 
    el append

"""
# List Comprehensions
squares_list_comprehensions = [value**2 for  value in range(1, 11)]
print(squares_list_comprehensions)

# Numeros pares con el range
even_number_0_100_range = list(range(0,101,2))
print(even_number_0_100_range)

# Numeros pares utilizando list comprehension
even_list_compre = [value for  value in range(0, 101)if value%2 == 0]
print(even_list_compre)