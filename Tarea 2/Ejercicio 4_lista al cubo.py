# Ejercicio 4 - generar lista de cubos.
# No requuiere input del usuario
# La longitud de la lista se genera al azar.
# Los números de la lista se generan al azar.
# En ambos casos, limitamos el rango numérico de 1 a 10, enteros.

import random

longitud = random.randint(1,10)

lista1 = []
lista2 = []

for i in range (longitud):
    lista1.append(random.randint(1,10))
    lista2.append(lista1[i]**3)

print(lista1)
print(lista2)