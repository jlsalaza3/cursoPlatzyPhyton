numbers=[1,2,3,4,5,6]
for i in numbers:
    print("i es igual a:",i)

for i in range (3,10):
    print(i)

fruits= ["Manzana","Pera","Uva","Naranja","Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja Encontrada")
x=0
while x<5:
    if x==3:
        break
    print(x)
    x +=1

numbers=[1,2,3,4,5,6]
for i in numbers:
    if i==3:
        continue
    print("i es igual a:",i)