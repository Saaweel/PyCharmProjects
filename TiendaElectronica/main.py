class NoFoundProduct(Exception):
    def __init__(self):
        super().__init__("No se ha encontrado el producto")
    pass

class InvalidQuantity(Exception):
    def __init__(self):
        super().__init__("La cantidad es inválida")
    pass

class ElectronicProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_information(self):
        print(f"Nombre: {self.name} / Precio: {self.price}€ / Stock: {self.stock}")


class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def show_products(self):
        for product in self.inventory:
            product.show_information()
            print("")

    def make_sale(self, selection, quantity):
        try:
            if quantity < 1:
                raise InvalidQuantity()

            for product in self.inventory:
                if product.name == selection:
                    if product.stock >= quantity:
                        print(f"Vendido correctamente {quantity} x {selection} por {(product.price * quantity)}€")
                        product.stock -= quantity
                        return
                    else:
                        raise InvalidQuantity()
            raise NoFoundProduct()
        except InvalidQuantity:
            print(f"La cantidad es inválida")
        except NoFoundProduct:
            print("No se ha encontrado el producto")


def main():
    store = Store()

    while True:
        try:
            print("\n1. Añadir producto")
            print("2. Ver productos")
            print("3. Realizar venta")
            print("4. Salir")

            option = input("Opción: ")

            if option == "1":
                name = input("Nombre: ")
                price = float(input("Precio: "))
                stock = int(input("Stock: "))
                store.add_product(ElectronicProduct(name, price, stock))
            elif option == "2":
                store.show_products()
            elif option == "3":
                store.show_products()
                selection = input("Producto: ")
                quantity = int(input("Cantidad: "))
                store.make_sale(selection, quantity)
            elif option == "4":
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Parámetro inválido")


main()

# TODO: Exceptions
