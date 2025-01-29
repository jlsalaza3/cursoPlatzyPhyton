#crear un iterador para los numeros impares

#limite
limit=10
#crear iterador 
odd_itter=iter(range(1,limit+1,2))
#usar iterador
for num in odd_itter:
    print(num)