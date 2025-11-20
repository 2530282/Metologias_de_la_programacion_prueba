message = "Viva Mexico!"
another_message = 'Hello, World!'

print(message)
print(another_message)

print(message, another_message, message)
print(another_message, message)

print(message)

"""

Los nombres de variables en Python deben nombrarse solo con:

    -letras, números y guión bajo (espacios)
    -deben comenzar con una letra o con guión bajo, pero NO con número:
        ejemplo correcto: mensaje_1 ( :) )
        ejemplo incorrecto: 1_mensaje
    -no utilizar espacios para separar palabras en los nombres de las variables
    -no utilizar palabras reservadas de Python para nombrar variables o archivos
    -deben ser cortos, pero descriptivos
    -deben ser en inglés
    -nombres de las variables en minúsculas 


"""

emiliano_message = "Hola, soy Charly y estoy aprendiendo Python!"
print(emiliano_message)
print(emiliano_mesage)

"""
traceback : Es un registro de donde el interpetre tuvo ploblemas al intentar ejecutar el código.

    Ejemplo:

    Traceback (most recent call last):
      File "C:/Users/ebarc/projects/Metologias_de_la_programacion_prueba/src/understanding_variables.py", line 31, in <module>
        print(emiliano_mesage)
              ^^^^^^^^^^^^^^^
        NameError: name 'emiliano_mesage' is not defined. Did you mean: 'emiliano_message'?

    NameError: Significa que olvidamos establecer el valor de una variable antes de utilizar o cometimos un error al ingresar el nombre de la variable.

"""

# Pasado al cuaderno