# Manejo de números y booleanos en Python

# Nombre: Barrientos Cardona Emiliano de Jesús

# Matricula: 2530282

# Grupo: IM 1-2

# Resumen:
# Los int son numeros enteros y los float son numeros decimales
# Los booleanos se sacan a travez de la comparacion de un valor (==)
# EL validar rangos nos permite que el codigo identifique que es un valor que se
# va calcular y no un texto y se tiene que evitar la divicion entre cero 
# porque provoca fallos en nuestro programa.
# Mi documento cubira que son los booleanos, int, float, los signos y como utilizarlos
# tambien veremos como ponerles rango y evitar dividir entre 0.

# Problem 1: Temperature converter and range flag

# Descripción:
# Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, 
# determina un valor booleano is_high_temperature que sea true si la temperatura en 
# Celsius es mayor o igual que 30.0 y false en caso contrario.

# Entradas:
# - temp_c (float; temperatura en °C).

# Salidas:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false

# Validaciones:
# - Verificar que temp_c pueda convertirse a float.
# - No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

temp_c = input("Insertar temperatura en grados Celsius: ")
if float(temp_c):
    if float(temp_c) >= -273.15:
        temp_k = float(temp_c) + 273.15
        print(f"Kelvin:",temp_k)
        float(temp_c) >= 30.0
        temp_f = (((9 * float(temp_c))/5) + 32)
        print(f"Fahrenheit: ", temp_f)
        print("High temperature:", float(temp_c))
    else:
        print("Mistake")

# 1) Normal: 
# Insertar temperatura en grados Celsius: 34.6
# Kelvin: 307.75
# Fahrenheit:  94.28
# High temperature: 34.6
# 2) Border: 
# Insertar temperatura en grados Celsius: 30
# Kelvin: 303.15
# Fahrenheit:  86.0
# High temperature: 30.0
# 3) Error:
# Insertar temperatura en grados Celsius: -273.15
#  Mistake

# Problem 2: Work hours and overtime payment

# Descripción:
# Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

# Entradas:
# - hours_worked (float; horas trabajadas en la semana).
# - hourly_rate (float; pago por hora).

# Salidas:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false

# Validaciones:
# - hours_worked >= 0
# - hourly_rate > 0
# - Si alguno no cumple, mostrar "Error: invalid input".

hours_worked = input("Insertar horas trabajadas: ")
hourly_rate = input("Insertar el pago por hora: ")
float(hourly_rate)
float(hours_worked)

if float(hours_worked) > 0: #  Validar datos antes de 
# operar (por ejemplo, que horas y salarios no sean negativos).
    if float(hourly_rate) > 0:
        regular_pay_1 = float(hourly_rate) <= 40
        regular_pay = regular_pay_1 * float(hourly_rate)
        overtime_pay_1 = float(hours_worked) - 40
        overtime_pay = overtime_pay_1 * float(hourly_rate)
        total_pay = regular_pay + overtime_pay
        print("Regular pay: <", {regular_pay},">")
        print("Overtime pay: <", {overtime_pay},">" )
        print("Total pay: <", {total_pay},">")
        has_overtime = float(hours_worked) > 40
        print("Has overtime: ", {has_overtime > 0})
    else:
        print("Error: invalid input")
# 1) Normal: 
# Insertar horas trabajadas: 234
# Insertar el pago por hora: 543
# Regular pay: < {0.0} >
# Overtime pay: < {105342.0} >
# Total pay: < {105342.0} >
# Has overtime:  {True}
# 2) Border: 
# Insertar horas trabajadas: 490
# Insertar el pago por hora: 450
# Regular pay: < {0.0} >
# Overtime pay: < {202500.0} >
# Total pay: < {202500.0} >
# Has overtime:  {True}
# 3) Error:
# Insertar horas trabajadas: 0
# Insertar el pago por hora: 0 
# Error: invalid input

# Problem 3: Discount eligibility with booleans

# Descripción:
# Determina si un cliente obtiene un descuento en su compra. La regla es:
# - Tiene descuento si:
#   - is_student es true OR
#   - is_senior es true OR
#   - purchase_total >= 1000.0
# Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

# Entradas:
# - purchase_total (float; total de la compra).
# - is_student_text (string; "YES" o "NO").
# - is_senior_text (string; "YES" o "NO").

# Salidas:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>

# Validaciones:
# - purchase_total >= 0.0
# - Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, 
# is_senior.
# - Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

purchase_total = input("Total de la compra: ")
is_student_text = input("Usted es un estudiante: YES o NO: ").upper()
is_senior_text = input("Usted es un señor: YES o NO: ").upper()

if float(purchase_total) >= 0.0:
    if "NO" or "YES":
        if float(purchase_total) >= 1000.0:
            purchase_total_1 = float(purchase_total)%10
            purchase_total = float(purchase_total) - purchase_total_1
            is_senior_text = "YES"
            print(f"Discount eligible: ", {is_senior_text == "YES"})
            print(f"Final total: <",{type(purchase_total)},">")
            is_student_text = "YES"
            print(f"Discount eligible: ", {is_student_text == "YES"})
            print(f"Final total: <",{type(purchase_total)},">")
        else:
            print("Error: invalid input")
# 1) Normal: 
# Total de la compra: 876
# Usted es un estudiante: YES o NO: no
# Usted es un señor: YES o NO: yes
# Discount eligible:  {True}
# Final total: < {876.0} >
# Discount eligible:  {True}
# Final total: < {876.0} >
# 2) Border: 
# Total de la compra: 8765
# Usted es un estudiante: YES o NO: no
# Usted es un señor: YES o NO: yes
# Discount eligible:  {True}
# Final total: < {8760.0} >
# Discount eligible:  {True}
# Final total: < {8760.0} >
# 3) Error: 
# Total de la compra: 0
# Usted es un estudiante: YES o NO: ef
# Usted es un señor: YES o NO: re
# Error: invalid input

# Problem 4: Basic statistics of three integers

# Descripción:
# Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y 
# un booleano all_even que indique si los tres números son pares.

# Entradas:
# - n1 (int)
# - n2 (int)
# - n3 (int)

# Salidas:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false

# Validaciones:
# - Verificar que los tres valores se puedan convertir a int.
# - No se requieren restricciones adicionales (se permiten negativos).

n1 = input("Number 1: ") # Usar nombres de variables descriptivos y mensajes 
# claros para el usuario.
n2 = input("Number 2: ")
n3 = input("Number 3: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if int(n1) and int(n2) and int(n3):
    sum_value = n1+n2+n3
    average_value = sum_value/3
    value = [n1,n2,n3]
    print("Sum:",{sum_value})
    print("Average: ", {average_value})
    print("Max: ",{max(value)})
    print("Min: ",{min(value)})
    all_even = n1 == n2 == n3
    print("All even: ", {all_even}) # Documentar 
# claramente cómo se interpretan los booleanos 
# (qué significa true y qué significa false en cada contexto)
else:
    print("Error")
# 1) Normal: 
# Number 1: 1
# Number 2: 2
# Number 3: 3
# Sum: {6}
# Average:  {2.0}
# Max:  {3}
# Min:  {1}
# All even:  {False}
# 2) Border: 
# Number 1: 3
# Number 2: 3
# Number 3: 3
# Sum: {9}
# Average:  {3.0}
# Max:  {3}
# Min:  {3}
# All even:  {True}
# 3) Error:
# Number 1: f
# Number 2: r
# Number 3: e
# Error  


# Problem 5: Loan eligibility (income and debt ratio)

# Descripción:
# Determina si una persona es elegible para un préstamo con base en:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
# La regla es:
# - debt_ratio = monthly_debt / monthly_income
# - eligible es true si:
#   - monthly_income >= 8000.0 AND
#   - debt_ratio <= 0.4 AND
#   - credit_score >= 650

# Entradas:
# - monthly_income (float; ingreso mensual).
# - monthly_debt (float; pagos mensuales de deuda).
# - credit_score (int; puntaje de crédito).

# Salidas:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false

# Validaciones:
# - monthly_income > 0.0 (evitar división entre cero).
# - monthly_debt >= 0.0
# - credit_score >= 0
# - Si no se cumple, mostrar "Error: invalid input".

monthly_income = input("Ingresar ingreso mensual: ")
monthly_debt = input("Ingresar pagos mensuales de deuda: ")
credit_score = input("Ingresar puntuaje de crédito: ")

float(monthly_debt)
float(monthly_income)
int(credit_score) # Usar tipos apropiados: int para contadores, 
# float para cantidades con decimales.

if int(credit_score) >= 0 and float(monthly_debt) >= 0.0:
    if float(monthly_income) > 0.0 :
        if float(monthly_income) >= 8000.0 and int(credit_score) >= 650:
            debt_ratio = float(monthly_debt) / float(monthly_income)
            print("Debt ratio: ",{debt_ratio <= 0.4})
        else:
            print("Error: invalid input")
# 1) Normal: 

# 2) Border: 

# 3) Error: 
# Ingresar ingreso mensual: 8000
# Ingresar pagos mensuales de deuda: 2000
# Ingresar puntuaje de crédito: 80
# Error: invalid input

# Problem 6: Body Mass Index (BMI) and category flag

# Descripción:
# Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
# - bmi = weight_kg / (height_m * height_m)
# Además, genera booleanos para indicar:
# - is_underweight (bmi < 18.5)
# - is_normal (18.5 <= bmi < 25.0)
# - is_overweight (bmi >= 25.0)

# Entradas:
# - weight_kg (float; peso en kilogramos).
# - height_m (float; estatura en metros).

# Salidas:
# - "BMI:" <bmi_redondeado>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false

# Validaciones:
# - weight_kg > 0.0
# - height_m > 0.0
# - Si no se cumple, mostrar "Error: invalid input".

weight_kg = input("Peso en kilogramos : ")
height_m = input("Estatura en metros: ")

if float(weight_kg) > 0.0 and float(height_m) > 0.0:
    bmi = float(weight_kg) / (float(height_m) * float(height_m))
    bmi_redondeado = round(bmi) #  Evitar duplicar expresiones 
# complejas: guardar resultados intermedios en variables.
    print("BMI:",{bmi_redondeado})
    print("Underweight:", {bmi < 18.5})
    print("Normal: ", {18.5 <= bmi < 25.0})
    print("Overweight: ", {bmi >= 25.0})

# 1) Normal: 

# 2) Border: 
# Peso en kilogramos : 43
# Estatura en metros: 1.54
# BMI: {18}
# Underweight: {True}
# Normal:  {False}
# Overweight:  {False}
# 3) Error: 

# Conclusion
# Los enteros y flotantes se utilizan para hacer calculos matematicos,
#  los cuales tienen la desventaja que no pueden ser 0 en algunos casos
#  por ello utilizamos las validaciones para asi poder evitar una falla 
# en el programa, tmabien hay que entender que validar los rangos nos 
# permite saber que numeros estamos usando y los operadores and, or y 
# not nos permitieron ahorrarnos tiempo al momento de realizarlo, estos
# nos permiten entender como funcionan las matematicas en la nomina, 
# descuentos, prestamos, etc.


# Referencias

# https://realpython.com/python-numbers/
# https://ellibrodepython.com/numeros-complejos 
# https://tenthousandmeters.com/blog/python-behind-the-scenes-8-how-python-integers-work/ 
# https://learn.microsoft.com/es-es/shows/intro-to-python-development/python-for-beginners-13-of-44-numeric-data-types
# https://realpython.com/python-variables/

