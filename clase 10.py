to_do=["Dirigirnos al hotel",
       "ir a almorzar",
       "visitar un museo",
       "volver al hotel"]
print(to_do)
numbers=[1,2,3,4, "cinco"]
print(numbers)
print(type(numbers))
mix=["uno", 2, 3.14, True, [1,2,3]]
print (mix)
print (len(mix))
print("primer elemento: ", mix[0])
print("último elemento: ", mix[-1])
print(mix[0:2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print (mix)
mix.insert(1,["c","d"])
print(mix)
print(mix.index(["c","d"]))
numbers=[1,2,100,90.45,3,4,5]
print(numbers)
print("mayor: ",max(numbers))
print("menor: ",min(numbers))
print(numbers)
del numbers[-1]
print (numbers)
del numbers[:2]
print(numbers)
del numbers
#print (numbers)
a=[1,2,3,4,5]
b=a
print (a)
print (b)
print( id(a))
print(id(b))
c= a[:]
print( id(a))
print(id(b))
print (id(c))
a.append(6)
print(a)
print(b)
print(c)
