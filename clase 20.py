add = lambda a,b: a+b
print(add(4,5))

multiply = lambda a,b: a*b
print(multiply(5,5))

#obtener el cuadrado de cada numero de la lista:
numbers= range(0,10)
#o lo que es lo mismo numbers=range(11)
squared_numbers=list(map(lambda x: x**2, numbers))
print("Cuadrados: ", squared_numbers)

#obtener los numeros pares:
event_numbers= list(filter(lambda x:x%2==0, numbers))
print ("Pares: ",event_numbers)