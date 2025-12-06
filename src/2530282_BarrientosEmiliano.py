# Manejo de funciones en Python

# Nombre: Barrientos Cardona Emiliano de Jesús

# Matricula: 2530282

# Grupo: IM 1-2

# Resumen ejecutivo
# Las funciones son bloques de código diseñados para realizar una tarea especifica.
# Los parametros se usan en la definición de la función, mientras que los argumentos 
# son los valores reales que se pasan cuando se llama a esa función.
# Es util separar la lógica en funciones reutilizables para la organizacion, facil de manejar y eficiente. 
# El valor de retorno es la información que una función entrega a la parte del código que la llamó
# permitiendo reutilizar ese resultado para otros cálculos o acciones.
# En esto ejercicios veremos como utilizar def (funciones), return (reutilizar una perte del código), 
# y como vamos a utilizar cada una en distintos eventos.


# Problem 1: Rectangle area and perimeter (basic functions)

# Descripción:
# Define dos funciones:
# - calculate_area(width, height): regresa el área de un rectángulo.
# - calculate_perimeter(width, height): regresa el perímetro.
# El código principal debe leer (o definir) los valores, llamar a las funciones
#  y mostrar los resultados.

# Entradas:
# - width (float)
# - height (float)

# Salidas:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>

# Validaciones:
# - width > 0
# - height > 0
# - Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = float(input("Writing width: "))
height = float(input("Writing height: "))    

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", area)
    print("Perimeter:", perimeter)
else:
    print("Error: invalid input")
# 1) Normal:
#    Input: width=5, height=3
#    Expected: Area=15, Perimeter=16
#
# 2) Border:
#    Input: width=0.01, height=0.01
#    Expected: Area=0.0001, Perimeter=0.04
#
# 3) Error:
#    Input: width=-4, height=2
#    Expected: "Error: invalid input"

# Problem 2: Grade classifier (function with return string)

# Descripción:
# Define una función classify_grade(score) que reciba una calificación numérica (0–100) 
# y regrese una categoría:
# - "A" si score >= 90
# - "B" si 80 <= score < 90
# - "C" si 70 <= score < 80
# - "D" si 60 <= score < 70
# - "F" si score < 60
# El código principal debe llamar la función y mostrar el resultado.

# Entradas:
# - score (float o int)

# Salidas:
# - "Score:" <score>
# - "Category:" <grade_letter>

# Validaciones:
# - 0 <= score <= 100
# - Si no se cumple, mostrar "Error: invalid input" y no clasificar.
def classify_grade(score):
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


score = float(input("Enter the score: "))

if 0 <= score <= 100:
    category = classify_grade(score)
    print("Score:", score)
    print("Category:", category)
else:
    print("Error: invalid input")

# 1) Normal:
#    Input: score=85
#    Expected: Category="B"
#
# 2) Border:
#    Input: score=90
#    Expected: Category="A"
#
# 3) Error:
#    Input: score=150
#    Expected: "Error: invalid input"

# Problem 3: List statistics function (min, max, average)

# Descripción:
# Define una función summarize_numbers(numbers_list) que reciba una lista de números 
# y regrese un diccionario con:
# - "min": mínimo
# - "max": máximo
# - "average": promedio (float)
# El código principal debe construir la lista (por ejemplo, a partir de texto separado 
# por comas), llamar la función y mostrar los valores.

# Entradas:
# - numbers_text (string; por ejemplo, "10,20,30")
# - Internamente: numbers_list (list of float o int)

# Salidas:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>

# Validaciones:
# - numbers_text no vacío tras strip().
# - Lista no vacía después de la conversión.
# - Todos los elementos deben poder convertirse a números; si alguno falla, mostrar
#  "Error: invalid input".


def summarize_numbers(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


numbers_text = input("Ingresa números separados por comas: ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    try:
        numbers_list = [float(x) for x in numbers_text.split(",")]

        if len(numbers_list) == 0:
            print("Error: lista vacía")
        else:
            stats = summarize_numbers(numbers_list)
            print("---- RESULTADOS ----")
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: invalid input")

# 1) Normal:
#    numbers_text = "3,5,8"
#    Expected:
#       Min: 3.0
#       Max: 8.0
#       Average: 5.3333333333...
#
# 2) Border:
#    numbers_text = "7"
#    Expected:
#       Min: 7.0
#       Max: 7.0
#       Average: 7.0
#
# 3) Error:
#    numbers_text = "" 
#    Expected: "Error: input vacío"

# Problem 4: Apply discount list (pure function)

# Descripción:
# Define una función apply_discount(prices_list, discount_rate) que:
# - reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
# - regrese una nueva lista con los precios ya descontados (no modificar la lista original).
# El código principal debe:
# - Crear una lista de precios.
# - Llamar a la función.
# - Mostrar la lista original y la nueva lista con descuento.

# Entradas:
# - prices_text (string; por ejemplo, "100,200,300")
# - discount_rate (float, entre 0 y 1)

# Salidas:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>

# Validaciones:
# - prices_text no vacío y lista resultante no vacía.
# - Todos los precios > 0.
# - 0 <= discount_rate <= 1; si no, "Error: invalid input".

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

prices_text = input("Ingresa precios separados por comas: ").strip()

try:
    discount_rate = float(input("Ingresa la tasa de descuento (0 a 1): "))
except ValueError:
    print("Error: la tasa debe ser numérica")
    discount_rate = -1 

if prices_text == "" or not (0 <= discount_rate <= 1):
    print("Error: invalid input")
else:
    try:
        prices_list = [float(p) for p in prices_text.split(",")]
        if any(p < 0 for p in prices_list):
            print("Error: invalid input")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)

            print("---- RESULTADOS ----")
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)
    except ValueError:
        print("Error: invalid input")
# 1) Normal:
#    prices_text = "100,200,300"
#    discount_rate = 0.2
#    Expected:
#       Original prices: [100.0, 200.0, 300.0]
#       Discounted prices: [80.0, 160.0, 240.0]

# 2) Border:
# Ingresa precios separados por comas: 0,8,7,9,57
# Ingresa la tasa de descuento (0 a 1): 1
# ---- RESULTADOS ----
# Original prices: [0.0, 8.0, 7.0, 9.0, 57.0]
# Discounted prices: [0.0, 0.0, 0.0, 0.0, 0.0]

# 3) Error:
#    prices_text = ""
#    discount_rate = 0.2
#    Expected: "Error: input inválido"


# Problem 5: Greeting function with default parameters

# Descripción:
# Define una función greet(name, title="") que:
# - Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
# - Regrese el mensaje: "Hello, <full_name>!"
# Si title está vacío, solo usar el nombre. El código principal debe llamar a la función 
# usando argumentos posicionales y nombrados.

# Entradas:
# - name (string)
# - title (string opcional)

# Salidas:
# - "Greeting:" <greeting_message>

# Validaciones:
# - name no vacío tras strip().
# - title puede estar vacío, pero si no lo está, también se normaliza con strip().

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"

print(greet("Alice"))
print(greet("Bob", "Dr."))
print(greet(name="Charlie", title="Eng."))

# 1) Normal:
#    greet("Alice")
#    Expected: "Hello, Alice!"

# 2) Border:
#    greet("") 
#    Expected: "Hello, !"

# 3) Error:
#    greet(None)
#    Expected: Error en ejecución (None no tiene método .strip())

# Problem 6: Factorial function (iterative or recursive)

# Descripción:
# Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de 
# forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. 
# El código principal debe:
# - Leer/definir n.
# - Validar n.
# - Llamar a factorial(n).
# - Mostrar el resultado.

# Entradas:
# - n (int)

# Salidas:
# - "n:" <n>
# - "Factorial:" <factorial_value>

# Validaciones:
# - n entero.
# - n >= 0.
# - Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar 
# números demasiado grandes; si no se cumple, mostrar "Error: invalid input".

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_input = input("Enter a non-negative integer: ")

if user_input.isdigit():  
    n = int(user_input)

    if 0 <= n <= 20:
        fact_value = factorial(n)
        print("n:", n)
        print("Factorial:", fact_value)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")

# 1) Normal:
#    Input: n=5
#    Expected: Factorial=120
#
# 2) Border:
#    Input: n=0
#    Expected: Factorial=1
#
# 3) Error:
#    Input: n=-3
#    Expected: "Error: invalid input"


# Conclusiones
# Las funciones nos ayudan a reciclar partes de los programas que podemos utilizar mas adelante,
# la funcion return nos permite repetir el programa en caso de que haya algun error en los valores
# establecidos, esto se vincula con los parametros y valores hacen que el codigo sea mas entendible
# y facil de manejar, me fue mas facil entenderlas dentro de los nombre y donde ubicarlos, al final
# lo que aprendi fue que la logica y las funciones son distintas, la logica permite trabajarse inmediatamente
# mientras que las funciones dividen la información para utilizarlas en otros lados.

# Referencias

# https://www.youtube.com/watch?v=g78juF9pB_w&t=98
# https://www.youtube.com/watch?v=Db43XBXlk7c&t=884
# https://ebac.mx/blog/funciones-de-python
# https://www.datacamp.com/es/tutorial/functions-python-tutorial
# https://www.codecademy.com/learn/flask-introduction-to-python/modules/learn-python3-functions/cheatsheet
