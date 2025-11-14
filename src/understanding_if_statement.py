cars = ['audi', 'bwm', 'subaru', 'toyota']

for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car)

# El condicional es el corazón de un if
# Condicional True
car = 'bwm'
print(car == 'bwm')  # True 

# Condicional False
car = 'Audi'
print(car == 'audi')  # False


# Posible solución a entradas del usuario
car = 'Audi'
print(car.lower() == 'audi')  # True

# Operador relacional != para determinar desigualdad
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # True
    print("Hold the anchovies")   

# Comparaciones numéricas
age = 18
print(age == 18)  # True

answer = 17
if answer != 42:  # True
    print("Esa no es la respuesta correcta. Intenta otra vez")

age = 17
print(age < 21)  # True
print(age <= 21)  # True
print(age > 21)  # False
print(age >= 21)  # False

# Multiples condiciones
age_0 = 22
age_1 = 18
# Operación and
print( age_0 >= 21 and age_1 >= 21 ) # False
print( age_0 >= 21 and age_1 >= 18 ) # True

# Operación or
print( age_0 >= 21 or age_1 >= 21 ) # True
print( age_0 >= 25 or age_1 >= 21 ) # False

"""

    Para preguntarnos si un valor específico esta en una lista, podemos utilizar el siguiente
    comparador:

"""
motocycles = ['honda', 'yamaha', 'suzuki']
moto_Emi = 'ducati'
print(moto_Emi in motocycles)  # False
print ('honda' in motocycles)  # True

"""

    Para preguntarnos si un valor específico no esta en una lista, podemos utilizar el siguiente
    comparador:

    value not in list
"""

banned_users = ['carlos', 'moyra', 'luz', 'hots']
user = 'mauro'
print(user not in banned_users)  # True
print('luz' not in banned_users)  # False

# Variable del tipo booleano
game_active = True
can_edit = False

"""
    if statement

    sintax:

    if condition:
        do something

    FORMA COMPLETA:
    if condition:
        do something
    else:
        do something
"""

age = int(input("\n \n ¿Dime cual es tu edad?")) # Convertir la variable age a un entero
print(age)
if age >= 18:
    print("Tu tienes la edad suficiente para votar")
else:
    print("Tu eres menor de edad, no puedes votar")