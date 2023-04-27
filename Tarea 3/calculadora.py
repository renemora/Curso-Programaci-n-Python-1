# Programa principal
# Despliega un menú de opciones, usuario ingresa un número
# Incluye la opción Salir
# Las funciones en archivo aparte

import calculos_simples as cs

print("Calculadora simple")
Salir = False
while Salir == False:
    lista1 = []
    lista2 = []
    n = 1
    print("¿Qué quieres hacer? introduce el número de la opción: ")
    print("1: sumar N números")
    print("2: restar dos números")
    print("3: multiplicar N números")
    print("4: dividir dos números")
    print("5: calcular el factorial de un número entero")
    print("6. calcular la raiz cuadrada de un número")
    print("7: salir")
    operacion = int(input("cuál es tu opción?: "))
    print(operacion)
    if operacion == 1:
        suma = cs.sumar_n_numeros(n, lista1)
        print("La suma de", suma[0], "es", suma[1])
    if operacion == 2:
        resta = cs.restar_numeros(lista2)
        print("La suma de", resta[0][0], "menos", resta[0][1], "es", resta[1])
    if operacion == 3:
        producto = cs.multiplicar_n_numeros(n,lista1)
        print("El producto de", producto[0], "es", producto[1])
    if operacion == 4:
        cociente = cs.dividir_numeros(lista2)
        print("El cociente de", cociente[0][0], "entre", cociente[0][1], "es", cociente[1])
    if operacion == 5:
        n = int(input("Ingresa un número entero mayor o igual a cero: "))
        resultado = cs.factorial(n)
        print("El factorial de", n, "es", resultado)
    if operacion == 6:
        n = float(input("Ingresa un número no negativo: "))
        if n < 0:
            print("Has ingresado un número negativo")
            continue
        raiz = cs.raiz_cuadrada(n)
        print("La raíz cuadrada de", n, "es", raiz)
    if operacion == 7:
        Salir = True
