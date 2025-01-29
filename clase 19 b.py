def add (a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divided (a,b):
    return a/b

def calclator():
    while True:
        print("seleccione una operación:")
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicación")
        print("4.División")
        print("5. Salir")
        option=input("Ingrese su opción(1,2,3,4,5): ")

        if option=="5":
            print("saliendo de la calculadora")
            break
        if option in ["1","2","3","4"]:
            num1= float(input("ingrese el primer  número: "))
            num2= float(input("ingrese el segundo número: "))

            if option== "1":
                print("La suma es: ", add(num1,num2))
            elif option== "2":
                print("La resta es: ", substract(num1,num2))
            elif option== "3":
                print("La multiplicación es: ", multiply(num1,num2))
            elif option== "4":
                print("La división es: ", divided(num1,num2))
        else:
            print("opcion no valida intenta de nuevo")
calclator()