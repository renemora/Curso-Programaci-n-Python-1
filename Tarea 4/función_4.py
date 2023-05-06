# Función que convierte una lista en una tupla
# Para ingresar una lista separada por comas consulté esta página:
# https://es.stackoverflow.com/questions/121275/ingresar-m%c3%baltiples-datosnumeros-y-obtener-una-sola-lista
# Convertimos los números de string a enteros.

def convertir_a_tupla(lista):
    tupla = tuple(lista)
    return tupla


# Programa principal.
# Se probó con 1,2,3,4,5,6 y otras secuencias, incluyendo negativos y cero.

# Lista de prueba
lista1 = [1,2,3,4,5,6]
print("Si la lista es ", lista1)
print()

# Convertimos la lista en tupla
tupla1 = convertir_a_tupla(lista1)

# Imprimir resultados
print("lista = ", lista1)
print("tupla = ", tupla1)
print()

# Vaciar lista1 y tupla1.
lista1 = []
tupla1 = ()

# Ingresar números.
numeros = input("Dime los numeros: ")
for num in numeros.split(","):
    lista1.append(int(num))
print()

# Convertimos la lista en tupla
tupla1 = convertir_a_tupla(lista1)

# Imprimir resultados
print("lista = ", lista1)
print("tupla = ", tupla1)
print("Adiós!")