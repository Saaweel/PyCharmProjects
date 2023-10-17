class Empleado:
    def __init__(self, name, payment, join_day):
        self.name = name
        self.payment = payment
        self.join_day = join_day

    pass

    def actualizar_salario(self, payment):
        self.payment = payment

    pass

    def get_name(self):
        return self.name

    pass

    def __str__(self):
        return f"Nombre: {self.name} Salario: {self.payment} Fecha de entrada: {self.join_day}"

    pass


class Empresa:
    def __init__(self):
        self.employees = []

    pass

    def agregar_empleado(self, employee):
        self.employees.append(employee)

    pass

    def eliminar_empleado(self, name):
        for employee in self.employees:
            if employee.get_name() == name:
                self.employees.remove(employee)

    pass

    def buscar_empleado(self, name):
        for employee in self.employees:
            if employee.get_name() == name:
                print(employee)
                return employee

    pass

    def mostrar_empleados(self):
        for employee in self.employees:
            print(employee)

    pass


empresa = Empresa()

empleado1 = Empleado("Juan Pérez", 50000, "2023-01-15")
empleado2 = Empleado("María González", 60000, "2022-11-20")
empleado3 = Empleado("Carlos López", 55000, "2023-03-05")

empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)
empresa.agregar_empleado(empleado3)

print("Lista de empleados en la empresa:")
empresa.mostrar_empleados()

print("\nEliminar empleado 'María González'")
empresa.eliminar_empleado("María González")

print("\nLista de empleados en la empresa después de eliminar a María González:")
empresa.mostrar_empleados()

print("\nBuscar empleado 'Carlos López'")
empleado_buscado = empresa.buscar_empleado("Carlos López")
if empleado_buscado:
    print(f"Empleado encontrado: {empleado_buscado}")

print("\nActualizar salario de 'Juan Pérez'")
empleado_juan = empresa.buscar_empleado("Juan Pérez")
if empleado_juan:
    empleado_juan.actualizar_salario(55000)

print("\nLista de empleados en la empresa después de actualizar el salario de Juan Pérez:")
empresa.mostrar_empleados()
