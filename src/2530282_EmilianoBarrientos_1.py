# Manejo de strings en Python

# Nombre: Barrientos Cardona Emiliano de Jesús

# Matricula: 2530282

# Grupo: IM 1-2

# En esta practica se explicara el manejo de strings en Python, incluyendo
# la creación, lectura, indexación, slicing, concatenación, búsqueda, 
# reemplazo, división, unión y formato de texto. Tambien se veran elementos que nos permitan quitar
# espacios en blanco y formas de identificar si una palabra es identica a otra.


# Problem 1: Full name formatter (name + initials)

# Este programa pide el nombre y al menos un apellido para asi 
# sacar las iniciales de tu nombre en mayusculas.

# Entradas:
# -full_name

# Salidas:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"

# Validaciones:
# - full_name no debe estar vacío después de strip().
# - Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
# - No aceptar cadenas que sean solo espacios.

full_name = input("Escribir tu nombre completo: ").title() # Los strings son inmutables: cualquier cambio genera una nueva cadena.

if len(full_name) > 0: 
    name_parts = full_name.split()
    if len(name_parts) >= 2:
        print("Formatted name: <Name In Title Case>")
        initial_1 = ".".join([name[0] for name in full_name.split()])
        print(f"Initials: <", initial_1, ">")
    else:
        print("Por favor, ingresa al menos un nombre y un apellido.")
# 1) Normal:
# Escribir tu nombre completo: emiliano barrientos cardona
# Formatted name: <Name In Title Case>
# Initials: < E.B.C >
# 2) Border:
# Escribir tu nombre completo: emiliano barrientos
# Formatted name: <Name In Title Case>
# Initials: < E.B >
# 3) Error:
# Escribir tu nombre completo: emi
# Por favor, ingresa al menos un nombre y un apellido.

# Problem 2: Simple email validator (structure + domain)

# Valida si una dirección de correo tiene un formato básico correcto:
# - Contiene exactamente un '@'.
# - Después del '@' debe haber al menos un '.'.
# - No contiene espacios en blanco.
# Si el correo es válido, también muestra el dominio (la parte después de '@').

# Entradas:
# - email_text

# Salidas:
# - "Valid email: true" o "Valid email: false"
# - Si es válido: "Domain: <domain_part>"

# Validaciones:
# - email_text no vacío tras strip().
# - Contar cuántas veces aparece '@'.
# - Verificar que no haya espacios (no debe haber " " en email_text).

email_text = input("Escribir un correo electrónico: ").strip()

if "@" in email_text and "." in email_text:
    At_sign_part = email_text.count("@")
    print(f"At sign: <{At_sign_part}>")
    print("Domain:", email_text.split("@")[-1].split("."))
    print("Valid email: true")
else:
    print("Valid email: false")
# 1) Normal:
# Escribir un correo electrónico: e.bar@gmail.com
# At sign: <1>
# Domain: ['gmail', 'com']
# Valid email: true
# 2) Border:
# Escribir un correo electrónico: emiliano@gmail.com
# At sign: <1>
# Domain: ['gmail', 'com']
# Valid email: true
# 3) Error:
# Escribir un correo electrónico: e@h
# Valid email: false

# Problem 3: Palindrome checker (ignoring spaces and case)

# Descripción:
# Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

# Entradas:
# - phrase (string).

# Salidas:
# - "Is palindrome: true" o "Is palindrome: false"
# - (Opcional) Mostrar también la versión normalizada de la frase.

# Validaciones:
# - phrase no vacía tras strip().
# - Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

phrase = input("Escribir una frase: ").strip() # Es buena práctica normalizar entrada con strip() 

if len(phrase) > 0:
    if len(phrase) >= 3:
        phrase_1 = phrase.lower() # y lower() antes de compararla.
        phrase_2 = phrase_1[::-1]
        if phrase_1 == phrase_2:
            print("Is palindrome: true")
            print(f"Palindromo: <{phrase_1}>")
        else:
            print("Is palindrome: false")
else:
     print("Is palindrome: false") # Escribir código legible: nombres de variables claros y mensajes de error entendibles.
# 1) Normal:
# Escribir una frase: amar rama
# Is palindrome: true
# Palindromo: <amar rama>
# 2) Border:
# Escribir una frase: otto
# Is palindrome: true
# Palindromo: <otto>
# 3) Error:
# Escribir una frase: morir
# Is palindrome: false

# Problem 4: Sentence word stats (lengths and first/last word)

# Descripción:
# Dada una oración, el programa debe:
# 1) Normalizar espacios (quitar espacios al principio y al final).
# 2) Separar las palabras por espacios.
# 3) Mostrar:
#    - Número total de palabras.
#    - Primera palabra.
#    - Última palabra.
#    - Palabra más corta y más larga (por longitud).

# Entradas:
# - sentence (string).

# Salidas:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"

# Validaciones:
# - Oración no vacía tras strip().
# - Debe contener al menos una palabra válida después de split().

sentence = input("Escribir una oración: ").strip()
if len(sentence) > 0: # Diseñar validaciones claras: primero que no esté vacío, luego el formato.
    sentence_1 = len(sentence.split())
    sentence_words = sentence.split()
    words = ", ".join(sentence_words)
    min_word = min(sentence_words, key=len)
    max_word = max(sentence_words, key=len)
    print(f"Word count: <", {sentence_1} ,">")
    print(f"First word: <", {sentence.split(" ")[0]} ,">")
    print(f"Last word: <", {sentence.split(" ")[-1]} ,">")
    print(f"Shortest word: <", {min_word} ,">")
    print(f"Longest word: <", {max_word} ,">")
else:
    print("Mistake")

# 1) Normal:
# Escribir una oración: Vamos a buscar esferas
# Word count: < {4} >
# First word: < {'Vamos'} >
# Last word: < {'esferas'} >
# Shortest word: < {'a'} >
# Longest word: < {'esferas'} >
# 2) Border:
# Escribir una oración: mexico
# Word count: < {1} >
# First word: < {'mexico'} >
# Last word: < {'mexico'} >
# Shortest word: < {'mexico'} >
# Longest word: < {'mexico'} >
# 3) Error:
# Escribir una oración:
# Mistake

# Problem 5: Password strength classifier

# Descripción:
# Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

# Ejemplo de reglas:
# - Weak: longitud < 8 o todo en minúsculas o muy simple.
# - Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
# - Strong: longitud >= 8 y contiene al menos:
#   - una letra mayúscula,
#   - una letra minúscula,
#   - un dígito,
#   - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

# Entradas:
# - password_input (string).

# Salidas:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"

# Validaciones:
# - No aceptar contraseña vacía.
# - Verificar longitud con len().

password_input = input("Escribir una contraseña: ").strip()

if len(password_input) < 8 and password_input.islower():
        print(password_input)
        print("Password strength: weak")  

        if len(password_input) >= 8 and password_input.isupper():
            print(password_input)
            print("Password strength: medium")
  
            if len(password_input) >= 8 and password_input.isdigit() and password_input.isalnum():
                print(password_input)
                print("Password strength: strong") 
            else:
               print("Mistake")
# 1) Normal:
# Escribir una contraseña: emiliano27
# emiliano27
# Password strength: medium
# 2) Border:
# Escribir una contraseña: juan
# juan
# Password strength: weak
# 3) Error:
# Escribir una contraseña: 
# Mistake

# Problem 6: Product label formatter (fixed-width text)

# Descripción:
# Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

# Product: <NAME> | Price: $<PRICE>

# La cadena completa debe tener exactamente 30 caracteres:
# - Si es más corta, rellena con espacios al final.
# - Si es más larga, recorta hasta 30 caracteres.

# Entradas:
# - product_name (string).
# - price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

# Salidas:
# - "Label: <exactly 30 characters>"
# (Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

# Validaciones:
# - product_name no vacío tras strip().
# - price_value debe poder convertirse a un número positivo.

product_name = input("Escribir un producto: ")
price_value = input("Escribir el precio: ")

number_1 = len(product_name) # Evitar "números mágicos" en índices; documentar qué extrae cada slice.
number_2 = len(price_value)
number_4 = number_1 + number_2

label_1 = product_name + " " + price_value
label = label_1.center(30)
label[:30]

if number_1 > 0:
    print("Label: <", {label}, ">") # Usar métodos de string en lugar de reescribir lógica básica.
    price_value.replace("-","")
    print(f"Product: < ", {product_name}," > | Price: $<", {price_value} ,">")
else:
    print("Mistake")

# 1) Normal:
# Escribir un producto: electrolit
# Escribir el precio: 20
# Label: < {'        electrolit 20         '} >
# Product: <  {'electrolit'}  > | Price: $< {'20'} >
# 2) Border:
# Escribir un producto: lala
# Escribir el precio: 34
# Label: < {'           lala 34            '} >
# Product: <  {'lala'}  > | Price: $< {'34'} >
# 3) Error:
# Escribir un producto:
# Escribir el precio:
# Mistake

# CONCLUSIONES
# Gracias a estos programas nos damos cuenta de que cada cosa que escribimos en cada
# linea hace una funcion, ejemplo de ello son las strings que nos permite manejar la 
# información que colocamos y donde se mueve, hay funciones como lower(minusculas), 
# upper(mayusculas), join(busqueda de un valor), count(ver cuanto valores hay iguales)
# y cada una permiten modificar las strings pero todo debe ser igualitario ya que no se 
# pueden mezclar strings con integers, tambien las validaciones son necesarias para ver
# si se esta cumpliendo con los valores, y aprendi que las strings no se puede modificar 
# pero si sacar partes de las strings para hacer nuevas con ayuda de las slices.

# Referencias

# https://www.youtube.com/watch?v=L7rILGJBG4U&t=563
# https://ellibrodepython.com/cadenas-python 
# http://programminghistorian.org/es/lecciones/manipular-cadenas-de-caracteres-en-python
# https://developers.google.com/edu/python/strings?hl=es-419 
# https://docs.python.org/3/library/string.html 