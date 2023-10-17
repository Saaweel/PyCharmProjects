filename = input("Escribe la ruta a un archivo: ")

try:
    with open(filename, 'r') as file:
        content = file.readlines()

        print(f"{filename}: ")
        for i, line in enumerate(content, start=1):
            print(f'{i}. {line.strip()}')
except FileNotFoundError:
    print("El archivo no existe")