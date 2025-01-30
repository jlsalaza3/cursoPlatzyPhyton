class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.available=True

    def borrow(self):
        if self.available:
            self.available=False
            print(f"El libro {self.title} ha sido prestado con exito")
        else:
            print(f"El libro {self.title} no se encuentra disponible, está prestado")
    def return_book(self):
        self.available=True
        print(f"El libro {self.title} fue devuelto satisfactoriamente")
class User:
    def __init__(self, nombre, identificacion):
        self.name=nombre
        self.user_ID=identificacion
        self.borrowed_books=[]
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} No está disponible")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No está en la lista de prestados")
class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} fue agregado a la lista de libros de la biblioteca de manera satisfactoria")
    def registrer_user(self,user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido agregado satisfactoriamente a la lista de miembros de la biblioteca")
    def show_available_books(self):
        print("Libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f" {book.title} por {book.author}")

#Crear los libros
book1 = Book("La María","Jorge Isaacs")
book2= Book("La Bruja","German Castro")

#Crear Usuario
user1=User("Jorge Salazar","001")

#Crear la biblioteca
library=Library()
library.add_book(book1)
library.add_book(book2)
library.registrer_user(user1)

#Mostrar Libros
library.show_available_books()

#Realizar un prestamo
user1.borrow_book(book1)

#Mostrar Libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar Libros
library.show_available_books()