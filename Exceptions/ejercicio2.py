numbers = [1, 2, 3, 4, 5, 6, 7, 8]

selected = int(input(f"Selecciona un número entre el 1 y el {len(numbers)}: "))

try:
    print(f"El numero seleccionado es el {numbers[selected-1]}")
except IndexError:
    print("Ese valor no está comprendido entre los números propuestos")
