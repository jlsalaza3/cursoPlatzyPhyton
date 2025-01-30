# Programación orientada a objetos POO:

class Person:
    def __init__(self, nombre, edad):
        self.name=nombre
        self.age=edad
    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age} años")

person1=Person("Camilo",30)
person2=Person("Andrea",25)

person1.greet()
person2.greet()