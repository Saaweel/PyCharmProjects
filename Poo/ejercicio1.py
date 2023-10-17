class Libro:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    pass

    def prestar(self):
        self.available = False

    pass

    def devolver(self):
        self.available = True

    pass

    def get_title(self):
        return self.title

    pass

    def __str__(self):
        return f"Nombre: {self.title} Autor: {self.author} Disponible: {(self.available and 'Si' or 'No')}"

    pass


class Biblioteca:

    def __init__(self):
        self.books = []

    pass

    def agregar_libro(self, libro):
        self.books.append(libro)

    pass

    def eliminar_libro(self, titulo):
        for book in self.books:
            if book.get_title() == titulo:
                self.books.remove(book)

    pass

    def buscar_libro(self, titulo):
        for book in self.books:
            if book.getTitle() == titulo:
                print(book)
                return book

    pass

    def mostrar_libros(self):
        for book in self.books:
            print(book)

    pass


biblioteca = Biblioteca()

libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("Matar un ruiseñor", "Harper Lee")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

print("Lista de libros en la biblioteca:")
biblioteca.mostrar_libros()

print("\nPrestar 'El Gran Gatsby'")
libro_prestado = biblioteca.buscar_libro("El Gran Gatsby")
if libro_prestado and libro_prestado.prestar():
    print(f"{libro_prestado.titulo} ha sido prestado.")

print("\nLista de libros en la biblioteca después del préstamo:")
biblioteca.mostrar_libros()

print("\nDevolver 'El Gran Gatsby'")
if libro_prestado and libro_prestado.devolver():
    print(f"{libro_prestado.titulo} ha sido devuelto.")

print("\nLista de libros en la biblioteca después de la devolución:")
biblioteca.mostrar_libros()
