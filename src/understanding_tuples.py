"""
    Las tuplas son listas de elementos que no pueden cambiar su tamaño.
    Las tuplas son listas inmutables.

    Se utlizan los () para definir una tupla.

    Ejemplo:
"""

# Rectangulo (largo, ancho)
rectangle_dimensions = (200, 50) # Tupla
print(rectangle_dimensions)
print(f" largo: {rectangle_dimensions[0]} mm") # 200
print(f" largo: {rectangle_dimensions[1]} mm") # 50

# Vamos a intentar modificar una tupla
# rectangle_dimensions[0] = 250 # Error de tipo TypeError
# rectangle_dimensions[1] = 100 # Error de tipo TypeError

for dimension in rectangle_dimensions:
    print(rectangle_dimensions)

"""
    No podemos modificar una tupla, ni tampoco agregar/eliminar elementos. Lo que si podemos hacer es
    cambiar la  asignación a una variable que almacene una tupla.

"""
rectangle_dimensions = (300, 150) # Tupla