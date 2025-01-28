squares=[x**2 for x in range (1,11)]
#print ("Cuadrados: ",squares)
celcius=[0,10,20,30,40]
farenheit = [(temp * 9/5)+32 for temp in celcius]
#print("Temperatura en grados Farenheit: ",farenheit)

#números pares
events = [x for x in range(1,21) if x%2 == 0]
#print(events)
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

transposed=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)