from random import randrange

number = -1

random = randrange(100)

attempts = 0

while number != random:
    number = int(input("Intenta adivinar el número secreto (entre 1 y 100): "))

    if number > random:
        print("El número secreto es menor.")
        attempts += 1
    elif number < random:
        print("El número secreto es mayor.")
        attempts += 1
    else:
        print(f"Felicidades! Adivinaste el número en  {attempts} intentos.")
