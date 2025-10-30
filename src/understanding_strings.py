""" 
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples '' o dobles "" es considerado un string.

        "Esto es un string"
        'Esto también es un string'

        'Le dije aun amigo, "¡Python es mi lenguaje favorito!"'
        "El lenguaje 'Python' lleva el nombre por Monty Python,
          no por la serpiente."


"""

Name = "clase de programacion"
print(Name)
print(Name.title())
print(Name)

"""

Un metodo es una accion que python puede realizar en eun fraagmento de datos o sobre una variable.

El punto . despues de una variable seguida del metodo title () dice que se tiene que ejecutar el metodo title() en la variable Name.

Todos los metodos van seguidos de parentesis porque en ocasiones necesitan informacion adicional para funcionar, lo cual iria dentro de los paréntesis.
"""

print(Name.upper())
print(Name.lower())

# concatenacion de strings
print("CONCATENACIÓN DE STRINGS")
first_name = "Emiliano"
last_name = "Barrientos"
full_name = first_name + " " + last_name
print(full_name) 

print("Hola, " + full_name.title() + "!")