# Programa que quita un elemento de una lista
# Se proporciona una lista de prueba
# el usuario define cuál elemento se quita.
# Usamos lambda y filter.
# De nuevo, un poco de prueba y error.

lista1 = ["mama", "papa", "1234", "qwerty"]

print("La lista de prueba es esta: ", lista1)
print()

quitar_elemento = str(input("Nombra el elemento que quieres quitar: "))

lista2 = list(filter(lambda x: x not in quitar_elemento, lista1))

print("La lista depurada es: ", lista2)
print()


# Programa original, Tarea 4
def borrar_con_repeticiones(lista, elemento):
    for x in lista:
        if x == elemento:
            lista.remove(elemento)
        continue

lista1 = ["mama", "papa", "1234", "qwerty"]
print("La lista de prueba es esta: ", lista1)
print()

quitar_elemento = str(input("Nombra el elemento que quieres quitar: "))

borrar_con_repeticiones(lista1, quitar_elemento)
print("La lista modificada es: ", lista1)
print()
