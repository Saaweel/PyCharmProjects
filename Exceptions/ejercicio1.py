num1 = int(input("Dividendo: "))
num2 = int(input("Divisor: "))

try:
    print(f"El resultado es { num1 / num2 }")
except ZeroDivisionError:
    print("No se pude dividir entre 0")
