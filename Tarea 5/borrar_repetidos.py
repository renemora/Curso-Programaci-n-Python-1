# Programa para borrar los repetidos de una lista numérica.
# el usuario ingresa una lista de números.
# Vamos a usar tres formas funcionales distintas.
# Traté de usar funciones filter y lambda pero no me funcionó.
# Consultamos la siguiente página:
# https://geekflare.com/es/remove-duplicate-items-from-python-lists/

# al inicio las listas están vacías
lista1 = []
lista2 = []

# Método #1 - usando los que se llama "comprensiones"
# Los paréntesis cuadrados permiten usar for, if dentro de una sola línea! 
# Se obtiene el resultado esperado. 

print("Método 1")
numeros = input("Dame una lista de números, separados por comas: ")
for num in numeros.split(","):
    lista1.append(int(num))
    
print("Lista original: ", lista1)

[lista2.append(num) for num in lista1 if num not in lista2]

print("Lista depurada: ", lista2)
print()


# Método 2, usando una sola lista y la función remove
# No da los resultados esperados, hay que hacer la depuración dos o más veces.
# Lo probamos con: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5
# Lo probamos con 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

lista1 = []

print("Método 2")
numeros = input("Dame una lista de números, separados por comas: ")
for num in numeros.split(","):
    lista1.append(int(num))
    

print("Lista original: ", lista1)

# Lo tiene que hacer dos o más veces para que funcione (???)
[lista1.remove(num) for num in lista1 if lista1.count(num) > 1]
print("Lista depurada, primera vez: ", lista1)

[lista1.remove(num) for num in lista1 if lista1.count(num) > 1]
print("Lista depurada, segunda vez: ", lista1)

[lista1.remove(num) for num in lista1 if lista1.count(num) > 1]
print("Lista depurada, tercera vez: ", lista1)
print()


# Método 3: convertimos a un conjunto y luego de nueva a una lista.
# Los conjuntos no pueden tener elementos repetidos.
# Se obtiene el resultado esperado.

lista1 = []

print("Método 3")
numeros = input("Dame una lista de números, separados por comas: ")
for num in numeros.split(","):
    lista1.append(int(num))
    
print("Lista original: ", lista1)

lista1 = list(set(lista1))

print("Lista depurada: ", lista1)
print()

# Programa original, Tarea 2

# al inicio la lista está vacía
lista1 = []

# valor inicial de la variable numero
numero = 1

print("Programa original Tarea 2")

# ingresar la lista de números
while numero != -1:
    numero = int(input("Ingresa un número entero positivo, escribe -1 para finalizar: "))
    # el "if" es para que no incluya el -1 en la lista
    if numero != -1:
        lista1.append(numero)
    
print("Lista original: ", lista1)

# depurar la lista de números

longitud = len(lista1)

for i in range (longitud):
    j = i + 1
    while j < longitud:
        if lista1[j] == lista1[i]:
            lista1.remove(lista1[j])
            longitud -= 1
        else:
            j += 1
    
print("Lista depurada: ", lista1)