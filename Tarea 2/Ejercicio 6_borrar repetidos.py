# Ejercicio #6 - depurar una lista de números enteros.
# No fue tan fácil, tuve que probar y modificar a partir de una idea inicial.
# Investigué un poco cómo ingresar una lista de números.

# al inicio la lista está vacía
lista1 = []

# valor inicial de la variable numero
numero = 1

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