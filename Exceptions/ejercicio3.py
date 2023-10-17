import math

number = int(input("Selecciona un número mayor o igual a 0: "))

try:
    print(f"La raíz cuadrada de {number} es {math.sqrt(number)}")
except ValueError as ve:
    print("Los números negativos no tienen raíz cuadrada")
