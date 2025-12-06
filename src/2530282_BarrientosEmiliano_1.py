# CRUD en Python ;)

# Nombre: Barrientos Cardona Emiliano de Jesús

# Matricula: 2530282

# Grupo: IM 1-2

# Resumen Ejecutivo

# CRUD es un acrónimo de las 4 operaciones fundamentales para gestionar datos
# persistentes en informática: Crear(Create), Leer(Read), Actualizar(Update),
# y Emilinar(Delete). Se utiliza una estructura de diccionario anidada para 
# almacenar cada tipo de pan. Cada clave del diccionario principal representa
# un identificador de producto, y su valor es otro diccionario que contiene 
# campos como nombre, precio y cantidad restante. El programa incluye: Crear nuevos
# tipos de pan, eliminar los exitentes, actualizar precios y cantidad, procesar pedidos,
# reducir cantidades y calcular totales.

# Problema: Gestor CRUD usando diccionarios y/o listas con funciones.

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

def adding_bread_type(key:str,name:str,price:float,quantity:int):
    """
    Docstring for adding_bread_type:
    this function adds a new index to the main dictionary
    :param key: main index's main identifier
    :type key: str
    :param name: name of the type of product(bread) this index contains
    :type name: str
    :param price: cost per piece
    :type price: float
    :param quantity: units in existence
    :type quantity: int
    """
    if key in products or name.strip()=="" or price<0 or quantity<0:
        print("error: invalid input")
        return
    products[key]={
          "name":name,
         "price":price,
         "quantity remaining":quantity,
         }
    print(f"your product {name} has been added under the key {key}")

def deleting_obsolete(key:str,):
        """
        Docstring for deleting_obsolete
        :this function is used to delete an index from our main dictionary
        :param key: Description
        :type key: str
        """
        if key not in products:
             print("error:the key is not in the dictionary")
             return(False)
        else:
            products.pop(key)
            print(f"{key} deleted succesfully")
            return(True)
        
def updating_quantity_or_price(key:str,price:float=None,quantity:int=None):
     """
     Docstring for updating_quantity_or_price:
     this function updates the price or quantity of a product in the dictionary
     
     :param key: product which we want to actualize
     :type key: str
     :param price: price to which we want to adjust our price
     :type price: float
     :param quantity: quantity in existance
     :type quantity: int
     """
     
     if key not in products:
            print("please set a valid input")
            return(False)
     if key in products and price is not None:
        if price>=0:
            products[key]["price"]=price
        else:
          print("you cant have a negative value")
          return(False)
     if key in products and quantity is not None:
        if quantity>=0:
            products[key]["quantity remaining"]=quantity
        else:    
            print("your quantity must not be less than 0")
            return(False)
     return(True)

def finalization(ans:str,):
    """
    Docstring for listing:
    this function allows us to exit a loop and finish the program:
    :param ans: a simple YES or NO
    :type ans: str
    """
    ans=ans.strip().upper()
    if ans=="YES":
        return False
    elif ans=="NO":
        return True
    else:
        print("please set a valid input")

def listing():
     """
     Docstring for listing
     this function allows us to view the description of every product:
     """
     for key, data in products.items():
          print(f"product: {key}")
          for attr, value in data.items():
               print(f" {attr}: {value}")

def order(bread:dict,):
     """
     Docstring for order
     this function receives a dictionary containing
     types of bread we want to buy and the quantity
     of bread we need and calculates the price we'd
     need to pay to get that order.
     :param bread: dictionary containing our information.
     :type bread: dict
     """
     total=0
     for key, quantity in bread.items():
        if key in products:
            existence=products[key]["quantity remaining"]
            if quantity <= existence:
                total=total+quantity*products[key]["price"]
                products[key]["quantity remaining"]-= quantity
                    
            else:
                print(f"sorry we don't have enough {key} in inventory")
                print(f"currently we only have {existence} pieces of {key}")
        else:
            print(f"currently we don't have {key}")                         
     return(total)

def menu (option:str):
     """
     Docstring for menu:
     this function help us to select an option
     from the menu and discard invalid inputs
     :param option: Description
     :type option: str
     """
     if option not in options and option not in options.values():
          print("please set a valid input")
          return None
     for key,data in options.items():
        if key == option or data == option :
            function=data
            return(function)

def input_validation(price, quantity):
        """
        Docstring for input_validation
        this function is used to verify that our inputs are
        valid to process in the rest of our problem
        :param price: Description
        :param quantity: Description
        """
        if not price.strip()=="":
            try:
                price=float(price)   
            except:
                print("please set a valid price")
                return False , None, None
        else:
            price=None
        if not quantity.strip()=="":
                 try:
                     quantity=int(quantity)
                 except ValueError:
                     print("please set a valid quantity")
                     return False, None, None
        
        return True, price, quantity
                
products={
    "mexican sweet bread":{"name":"mexican sweet bread",
                            "price":10.5,
                            "quantity remaining": 20},
    "donut":{"name":"donut",
            "price":8.50,
            "quantity remaining": 30,},
    "biscuit":{"name":"biscuits",
            "price":7.50,
            "quantity remaining": 10,},
    "mexican bread roll":{"name":"mexican bread roll",
            "price":3.50,
            "quantity remaining": 98,},
    "croissant":{"name":"croissant",
            "price":12.00,
            "quantity remaining": 98,},
    "lovers bread":{"name":"lovers bread",
            "price":20.00,
            "quantity remaining": 50,},
    "piggy cookies":{"name":"piggy cookies",
            "price":15.00,
            "quantity remaining": 54,},
    "cup cakes":{"name":"cupcake",
            "price":20.00,
            "quantity remaining": 28,},
    "palmiers":{"name":"palmiers",
            "price":17.50,
            "quantity remaining": 94,},
    "brioche bread":{"name":"brioche bread",
            "price":25.00,
            "quantity remaining": 67,},
}

options={
    "1": "new type of bread",
    "2": "delete type of bread",
    "3":"update inventory",
    "4":"calculate order",
    "5":"itiems",
    "6": "exit",
}

print("welcome to the inventory interface")
keep_going=True
while keep_going:
    print("main menu\n")
    for key, data in options.items():
        print(f"{key}- {data}\n")
    print("indicate by their name or number")
    option=input("which action would you like to do?\n").strip().lower()
    operation=menu(option)
    if operation == None:
        ans=input("do you wish to try again?")
        keep_going=finalization(ans)
    elif operation == "new type of bread":
         print("welcome to the addition menu")
         key=input("please set your new product's identifier\n")
         name=input("please now set your products name \n")
         valid=False
         while not valid:
            quantity=input("please set your product's inventory\n")
            price=input("please now set your products price\n")
            touple=input_validation(price, quantity)
            if touple [0] != False:
                 valid=touple[0]
                 price=touple[1]
                 quantity=touple[2]
                 adding_bread_type(key, name, price, quantity)
                 listing()
         
    elif operation == "delete type of bread":
         print("welcome to the deleting menu.\n here you can delete a product of your choice")
         print(f"we currently have \n")
         listing()
         valid=False
         while not valid:
            key = input("please set the type of bread you need to delete:\n")
            valid=deleting_obsolete(key)
         listing()

    elif operation == "update inventory":
         print("welcome to the updating menu.\n here you can update the price and quantity of our products")
         print(f"we currently have \n")
         listing()
         print("if you  only wish to update one aspect just leave the other blank")
         valid=False
         while valid==False:
            key= input("write the name of the product you'd like to update\n")
            price=input("set the new price\n")
            quantity= input("set the current existence of the product\n")
            touple=input_validation(price, quantity)
            if touple[0] != False:
                price=touple[1]
                quantity=touple[2]
                valid=updating_quantity_or_price(key, price, quantity)
                for index, datum  in products[key].items():
                     print(index,datum)
    elif operation == "calculate order":
         print ("welcome to the order menu")
         print("our current products are")
         listing()
         print("set your products specifying type and quantity\n IMPORTANT:set values one by one")
         ans=True
         bread ={}
         total_order={}
         total=0
         while ans:
            key=input("please set your type of bread\n")
            quantity=input("set how many pieces do you need?")
            try:
                quantity=int(quantity)
            except ValueError:
                 print("error invalid quantity")
                 continue
            if quantity>=0:
                bread={key:quantity}
                total_order.update(bread)
                price=order(bread)
                total=total+price
                ans2=None
                while ans2==None:
                    decision= input("is that your total order?\n YES or NO")
                    ans=finalization(decision)
                    ans2=ans
         for key,data in total_order.items():
              print(key,data)
         print(total)

    elif operation == "itiems":
         listing()
    elif operation == "exit":
         ans=input("are you sure you want to exit the program?\n" \
         "YES OR NO\n")
         keep_going=finalization(ans)
         print("have a nice day")


# TEST CASE 1 — NORMAL 
# User selects: 1 (new type of bread)
# Inputs:
#   key = "banana bread"
#   name = "banana bread"
#   quantity = "15"
#   price = "22"
# Expected program behavior:
#   - input_validation() converts price→22.0, quantity→15
#   - adding_bread_type() adds the new dictionary entry
# Program Output:
#   "your product banana bread has been added under the key banana bread"
#   Then listing() prints all products including the new one:
#       product: banana bread
#        name: banana bread
#        price: 22.0
#        quantity remaining: 15

# TEST CASE 2 — BORDER CASE 
# User selects: 3 
# Inputs:
#   key = "donut"
#   price = ""     (empty → means do not update)
#   quantity = "100"
# Expected program behavior:
#   - input_validation() returns price=None, quantity=100
#   - updating_quantity_or_price() updates only "quantity remaining"
# Program Output:
#   (prints donut's updated fields)
#    name donut
#    price 8.5
#    quantity remaining 100

# TEST CASE 3 — ERROR CASE 
# User selects: 1 (new type of bread)
# Inputs:
#   key = "badbread"
#   name = "bad bread"
#   quantity = "5"
#   price = "abc"
# Expected program behavior:
#   - input_validation() detects price cannot convert to float
# Program Output:
#   "please set a valid price"
#   Item is NOT added

# Conclusiones

# La estuctura CRUD organizo todo el inventario, separando la creación,
# la eliminación, la actualización y la ordenación en funciones propias.
# Los diccionarios permitieron administrar de mejor manera la información,
# permitiendo acceder cada tipo de pan y ver cuantos hay actualmente. Lo mas 
# dificil fue la validación de entradas, en especial al convertir el precio y
# la cantidad a partir de la entrada sin procesar del usuario. La función de
# validación ayudó a prevenir conversiones no válidas y mejoró la seguridad 
# del programa.Se puede extender al almacenamiento persistente guardando el diccionario en un archivo JSON

# Referencias 

# https://github.com/albertorc87/crud-python
# https://www.geeksforgeeks.org/python/crud-operation-in-python-using-mysql/
# https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/leccion6/crud_app.html
# https://realpython.com/crud-operations/