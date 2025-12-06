# Fibonacci Series with Python ;)

# Nombre: Barrientos Cardona Emiliano de Jesús

# Matricula: 2530282

# Grupo: IM 1-2

# Resumen Ejecutivo:

# La serie de Fibonacci es una secuencia numerica infinita que comienza con 0 y 1, donde
# cada numero subsiguiente es la suma de los 2 anteriores. Calcular la serie hasta un 
# numero de términos n significa sumar los primeros n elementos de una sucesion numerica que
# sigue un patron, en este documento veremos como hacer una serie fibonacci con una lectura de n
# validacion basica y generación de la serie.

# Problem: Fibonacci series up to n terms

# Descripción:
# Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

# - Si n = 1 → salida: 0  
# - Si n = 2 → salida: 0, 1  
# - Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

# El programa debe:
# 1) Leer n desde la entrada estándar.  
# 2) Validar n.  
# 3) Generar la serie de Fibonacci con un bucle (for o while).  
# 4) Imprimir los términos en una sola línea, separados por espacios o comas.

# Entradas:
# - n (int; número de términos de la serie a generar).

# Salidas:
# - "Number of terms:" <n> (opcional)
# - "Fibonacci series:" <term_1> <term_2> ... <term_n>

# Validaciones:
# - n debe poder convertirse a entero.
# - n >= 1.
# - (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
# - Si la validación falla, NO calcular la serie.

user_input = input("Enter number of terms: ").strip()

if not user_input.isdigit():
    print("Error: invalid input (not an integer).")
    exit()

n = int(user_input)

if n < 1 or n > 50:
    print("Error: invalid input (must be between 1 and 50).")
    exit()
elif n == 1:
    print("Fibonacci series: 0")
    exit()
elif n == 2:
    print("Fibonacci series: 0 1")
    exit()

fibo = [0, 1] 

for i in range(2, n):
    next_term = fibo[i-1] + fibo[i-2]
    fibo.append(next_term)

fibo_text = " ".join(str(x) for x in fibo)

print("Fibonacci series:", fibo_text)

# 1. Normal case:
#   n = 7  
#    Expected output: "Fibonacci series: 0 1 1 2 3 5 8"

# 2. Border case:
#    n = 1  
#    Expected output: "Fibonacci series: 0"

# 3. Error case:
#    Enter number of terms: 0
# Error: invalid input (must be between 1 and 50).

# Conclusiones

# El buque permitio repetir la operacion o el programa hasta alcanzar 
# el objetivo indicado. Se debe tener cuidado en los casos de n=1 y n=2
# ya que son los resultados que deben dar: n=1 arroja 0 y n=2 arroja 0,1
# ya que si arroja otros resultados significa que el programa no esta bien 
# ejecutado, este programa podria utilizarse en el estudio de las finanzas
# en el estudio y comportamiento de la naturaleza (en patrones de crecimiento
# en plantas y conchas).

# Referencias

# https://ellibrodepython.com/while-python
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.mclibre.org/consultar/python/lecciones/python-while.html
# https://pythonscouts.com/python-while/