number = int(input("Ingresa un número entero positivo: "))

counter = 0

for x in range(number):
    if x % 2 == 0:
        counter += 1

print(f"Hay {counter} números pares entre 0 y {number}.")
