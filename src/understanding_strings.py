""" 
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples '' o dobles "" es considerado
     un string.

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

Un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable.

El punto . despues de una variable seguida del metodo title () dice que se tiene que ejecutar el
 metodo title() en la variable Name.

Todos los metodos van seguidos de parentesis porque en ocasiones necesitan informacion adicional 
para funcionar, lo cual iria dentro de los paréntesis.
En esta ocación el metodo .title() no requiere información adicional para ejecutarse.

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

# Whitespaces
"""
  Whitespace se refiere a cualquier caracter que no se imprime, es decir, un tabulador 
  y finales de línea. Los whitespaces se utilizan comúnmente para organizar las salidas (prints)
  de tal manera que sea más amigable de leer o ver para los usuarios.
"""
# Ejemplos tabulador
print("Python")
print("\tPython") #Tabulador
print("\t\tPython") #Tabulador

# Ejemplos salto de línea
print("Lenguajes de programación:  \nPython  \nJavaScript\nC  \nJavascript")
print("Emiliano")
print("Barrientos")

message = """

    por dios, callate ya un rato, que me estas volviendo loco
"""
#Eliminacion de espacios en blanco
programming_language = " Python Javascrip "
print(programming_language)
print(programming_language.lstrip()) 
""" Elimina espacios en blanco a la izquierda """
print(programming_language.rstrip()) 
""" Elimina espacios en blanco a la derecha """
print(programming_language.strip()) 
""" Elimina espacios en blanco a ambos lados """ 

# Syntax error con strings

message = "Una fortaleza de Python es su comunidad"
print(message)

message = "Una fortaleza de 'Python' es su comunidad"
print(message)

# Concatenación con f-strings
famous_person = "Charly Mercury"
quote = "Python is love"

#Concatenación convencional
message = famous_person + " una vez dijo " + quote 
print(message)

#Concatenación con f_string
"""
  () = parentesis
  [] = corchetes
  {} = llaves
"""

message_f_strings = f"{famous_person} una vez dijo {quote}"
print(message_f_strings)

# Actividad 
"""
  1) Elige un personaje famoso e igualarlo a una varisable del tipo string
  2) Elige una frase famosa que haya dicho e iguala a una variable del tipo string
  3) Generar un mesaje con las dos variable utilizando f-strings
  4) Imprime el mensaje
  """

Famous_person = "Sherlock Homes"
Quote = "Elemental, mi querido Watson"

message_f_strings = f"{Famous_person} dijo {Quote}"
print(message_f_strings)

# Pasado al cuaderno