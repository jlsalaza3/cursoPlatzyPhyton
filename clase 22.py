try:
    divisor=int(input("ingresa un número divisor: "))
    result=100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error, el divisor no puede ser Cero")
    print("Ha ocurrido un error", e)
except ValueError as e:
    print("Error, debes introducir un número valido")
    print("Ha ocurrido un error", e)