numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers)
information={"Nombres":"Jorge Luis",
             "Apellidos":"Salazar Ramírez",
             "Altura": 1.68,
             "Edad":51}
print(information)
del information["Edad"]
print(information)

claves= information.keys()
print(claves)
print(type(claves))
valores= information.values()
print(valores)
pairs= information.items()
print(pairs)
contactos={"jorge luis":{"Apellidos":"Salazar Ramírez",
             "Altura": 1.68,
             "Edad":51},
             "camilo andrés":{"Apellidos":"Gutiérrez Pérez",
             "Altura": 1.80,
             "Edad":26}
}
print(contactos)
print(contactos["jorge luis"])
