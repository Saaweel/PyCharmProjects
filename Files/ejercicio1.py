import random


def createFile(filename, quantity):
    with open(filename, 'w') as file:
        for _ in range(quantity):
            number = random.randint(1, 100)
            file.write(str(number) + '\n')
    print(f'Archivo generado con {quantity} números aleatorios')


fileNameInput = input("Ingrese el nombre del archivo de salida: ")
quantityInput = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
createFile(fileNameInput, quantityInput)
