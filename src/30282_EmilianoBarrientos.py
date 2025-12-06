# CRUD en Python ;)

# Nombre: Barrientos Cardona Emiliano de Jesús

# Matricula: 2530282

# Grupo: IM 1-2

# Problema 6.1: Gestor CRUD usando diccionarios y/o listas con funciones.

# Descripción:
# Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. Cada ítem puede representar, por ejemplo, un producto de inventario con los siguientes campos sugeridos:

# - id (string o int, único)
# - name (string)
# - price (float)
# - quantity (int)

# El programa debe:

# 1) Definir una estructura de datos principal:
#   - Opción A: dict item_id -> dict con datos del ítem.
#   - Opción B: list de dicts, cada dict con campos id, name, price, quantity.
#  (En comentarios, explica cuál opción escogiste y por qué.)

# 2) Definir FUNCIONES separadas para cada operación CRUD:
#     - create_item(data_structure, item_id, name, price, quantity) -> bool o dict
#     - read_item(data_structure, item_id) -> dict o None
#     - update_item(data_structure, item_id, new_name, new_price, new_quantity) -> bool
#     - delete_item(data_structure, item_id) -> bool
#     - list_items(data_structure) -> list o simplemente imprime
#    Puedes ajustar nombres y parámetros, pero debe quedar claro qué hace cada función y qué regresa.

# 3) Implementar un MENÚ en el código principal (main loop):
#    Ejemplo de opciones:
#    - 1) Create item
#    - 2) Read item by id
#    - 3) Update item by id
#    - 4) Delete item by id
#    - 5) List all items
#    - 0) Exit

# 4) En el bucle principal:
#    - Mostrar el menú.
#    - Leer la opción.
#    - Según la opción, pedir los datos necesarios (id, name, price, quantity).
#    - Llamar a la función correspondiente.
#    - Mostrar mensajes claros de resultado.

# Entradas:
# - option (string o int; opción de menú).
# - item_id (string o int).
# - name (string).
# - price (float).
# - quantity (int).

# Salidas:
# - Mensajes tipo:
#   - "Item created"
#   - "Item updated"
#   - "Item deleted"
#   - "Item not found"
#   - "Items list:" y luego la lista de elementos (formato libre pero legible).

# Validaciones:
# - option debe ser una de las opciones definidas (por ejemplo 0–5).
# - item_id no vacío tras strip().
# - price y quantity deben ser números válidos:
#   - price >= 0.0
#   - quantity >= 0
# - Si falla alguna validación, mostrar "Error: invalid input" y NO realizar la operación.
# - En CREATE:
#   - Si el id ya existe, decide una política (por ejemplo, no permitir duplicados) y documenta tu elección.
# - En READ/UPDATE/DELETE:
#   - Si el id no existe, mostrar "Item not found".


# 1) Normal:
# 2) Border:
# 3) Error: 
