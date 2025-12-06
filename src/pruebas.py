
def area():
    area(f"Area: {calculate_area}")
def perimeter():
    perimeter(f"Perimeter: {calculate_perimeter}")

try:
    width = float(input("Insertar el ancho: "))
    height = float(input("Insertar el alto: "))
    if width > 0 and height > 0:
        calculate_area = height * width
        calculate_perimeter = height + height + width + width
except:
    print("Error: invalid input")