# Programa que eleva una lista al cubo, de la Tarea 2.
# El usuario ingresa una lista de números separados por comas.
# El método para separar los números lo usé en la Tarea 4.
# Usamos función map y función lambda.
# Nos basamos en la presentación y un poco de "prueba y error".

import random # Para la función original


# Lista de prueba
# lista1 = [1, 2, 3, 4, 5]

# longitud = random.randint(1,10)

lista1 = []

numeros = input("Dame una lista de números, separados por comas: ")
for num in numeros.split(","):
    lista1.append(int(num))

#for i in range (longitud):
#    lista1.append(random.randint(1,10))

lista2 = list(map((lambda x: x**3),lista1))
# si no pongo list, me imprime un "object algo" en pantalla.

print(lista1)
print(lista2)
print()




# Programa original, usa dos listas, la primera se genera al azar

longitud = random.randint(1,10)

lista1 = []
lista2 = []

for i in range (longitud):
    lista1.append(random.randint(1,10))
    lista2.append(lista1[i]**3)

print(lista1)
print(lista2)
print("Adiós!")