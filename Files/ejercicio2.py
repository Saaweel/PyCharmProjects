def addTask(task):
    with open("lista_tareas.txt", 'a') as file:
        file.write(task + '\n')
    print(f'Se ha agregado la tarea: "{task}"')


def listTasks():
    try:
        with open("lista_tareas.txt", 'r') as file:
            tasks = file.readlines()

        if tasks:
            print("Lista de tareas:")
            for i, tarea in enumerate(tasks, start=1):
                print(f'{i}. {tarea.strip()}')
        else:
            print("No hay tareas en la lista.")
    except:
        print("No hay tareas en la lista.")


while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        addTask(input("Ingrese la nueva tarea: "))
    elif option == "2":
        listTasks()
    elif option == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
