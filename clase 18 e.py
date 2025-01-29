#numeros fibonacci
#  0,1,1,2,3,5,8,13 resultan de sumar los 2 numero anteriores
def fibonacci(limit):
    a,b=0,1
    #  es lo mismo que escribir que a=0 y b=1 pero se hace en una sola linea
    while a<limit:
        yield a
        a,b = b,a+b
for num in fibonacci(15):
    print(num)