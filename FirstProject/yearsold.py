name = input("Por favor, ingresa tu nombre: ")
age = int(input("Por favor, ingresa tu edad: "))

if age < 18:
    print(f"{name}, eres menor de edad")
else:
    print(f"{name}, eres mayor de edad")
