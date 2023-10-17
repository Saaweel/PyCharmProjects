class DividedByZero(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
    pass


def divide(n1, n2):
    if n2 == 0:
        raise DividedByZero("No se puede dividir entre 0")
    else:
        print(f"El resultado es { n1 / n2 }")


num1 = int(input("Dividendo: "))
num2 = int(input("Divisor: "))

try:
    divide(num1, num2)
except DividedByZero:
    print("El divisor no puede ser 0")
