# Función que remueve un elemento de una lista.
# Uso las funciones append y remove.
# Para crear la lista, me basé en un ejercicio de la Tarea #2
# El uso de la función remove lo consulte aquí: https://entrenapython.com/eliminar-un-elemento-de-una-lista-en-python-clear-pop-remove-del/  

def borrar_con_repeticiones(lista, elemento):
    for x in lista:
        if x == elemento:
            lista.remove(elemento)
        continue


# Programa principal
lista1 = ["mama", "papa", "1234", "qwerty"]
print("La lista de prueba es esta: ", lista1)
print()

quitar_elemento = str(input("Nombra el elemento que quieres quitar: "))
borrar_con_repeticiones(lista1, quitar_elemento)
print("La lista modificada es: ", lista1)
print()

# vaciamos la lista
lista1 = []
print("Hemos vaciado la lista.")
print()

entrada = ""

# ingresar los componentes de la lista, en forma de cadenas o strings
while entrada != "fin":
    entrada = str(input("Ingresa un elemento a la lista de strings (fin para terminar): "))
    # el "if" es para que no incluya el "fin" en la lista
    if entrada != "fin":
        lista1.append(entrada)
    
print("Lista original: ", lista1)
print()

quitar_elemento = str(input("Nombra el elemento que quieres quitar: "))
borrar_con_repeticiones(lista1, quitar_elemento)
print("La lista modificada es: ", lista1)
print("Adiós!")