"""
    Funcions

    Las funciones son bloques de código diseñados para realizar una tarea especifica.

    Cuando queremos realizar la tarea que se ha definido en una funcion, tenemos que llenar el 
    nombre de la funcion resposable de esto.

    Definición de una funcion (Syntax)

    def name_of_functions(paraments):
        actions
"""
def greeting_mauro():
    print("Hola Mauro, que gusto verte!!!")

def greet(username, msj):
    print(f"Hola {username}, {msj} !!!")

# Argumentos
greeting_mauro() # Llamado a la función
greet("Emiliano", "Se te pegaron las cobijas")

"""
    Vamos a realizar un programa que fenere el nombre completo de una persona.

    Vamos a pasarle primer nombre, el segundo y el apellido.

    La función debe generar el nombre completo y regresarlo.

"""
def create_full_name(firts_name, last_name, middle_name=" "): 
    """
    
        Docstrings - Jorge This function creates the fullname of a person give its three names.

    """

    full_name = f"{firts_name} {middle_name} {last_name}"
    return full_name

user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
user_last_name = input("Escribe tus apellidos: ").strip().lower()

# Argumentos Posicionales -> Positional Arguments
print(create_full_name(user_first_name, user_middle_name, user_last_name))

# Argumentos Posicionales -> Positional Arguments
full_name = create_full_name(
    user_first_name,
    user_last_name,
   user_middle_name,
)

print(full_name)

# Argumentos Clave -> Keyword Arguments
full_name_key = create_full_name(
    last_name=user_last_name,
    firts_name=user_first_name,
    middle_name=user_middle_name
)

print(full_name_key)

# Parámetros opcionales
profe = create_full_name(user_first_name, user_middle_name, user_last_name)
print(profe)

# Temas para estudiar a futuro
# funciones: args, kwargs
# manejo de datos: abrir archivos csv, .json, .yml, .txt, .xls, .doc, .pdf, etc
# argumentos por linea de comandos - sys
# cli - command line interface
# generadores, iteradores, yield
# testing -> 