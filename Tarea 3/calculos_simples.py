# Aquí se definen las funciones que se usarán en la calculadora.

import math

def sumar_n_numeros(n, lista):
    lista = []
    suma = 0.0
    i = 0
    n = int(input("¿Cuántos números quieres sumar? "))
    for i in range(n):
        lista.append(float(input("Ingresa un número: ")))
        suma += lista[i]
        i += 1
    # devuelve = (lista, suma)
    # return devuelve
    return (lista, suma)


def restar_numeros(lista):
    lista = []
    resta = 0.0
    lista.append(float(input("Ingresa primer número: ")))
    lista.append(float(input("Ingresa segundo número: ")))
    resta = lista[0] - lista [1]
    return (lista, resta)

def multiplicar_n_numeros(n, lista):
    lista = []
    prod = 1.0
    i = 0
    n = int(input("¿Cuántos números quieres multiplicar? "))
    for i in range(n):
        lista.append(float(input("Ingresa un número: ")))
        prod *= lista[i]
        i += 1
    return (lista, prod)

def dividir_numeros(lista):
    lista = []
    cociente = 1.0
    lista.append(float(input("Ingresa primer número: ")))
    lista.append(float(input("Ingresa segundo número: ")))
    cociente = lista[0] / lista[1]
    return (lista, cociente)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
def raiz_cuadrada(n):
    return math.sqrt(n)
