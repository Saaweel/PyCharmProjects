try:
    number = int(input("Ingresa un número entero: "))
    print(f"Has introducido un numero entero válido {number}")
except ValueError:
    print("Debes ingresar un número entero.")
