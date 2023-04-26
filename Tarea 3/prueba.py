import calculos_simples

print("Calculadora simple")
Salir = False
while Salir == False:
    print("¿Qué quieres hacer? introduce el número de la opción: ")
    print("1: sumar N números")
    print("2: restar dos números")
    print("3: multiplicar N números")
    print("4: dividir dos números")
    print("5: calcular el factorial de un número entero")
    print("6: salir")
    operacion = int(input("cuál es tu opción?: "))
    print(operacion)
    if operacion == 1:
        sumar_n_numeros()
    if operacion == 2:
        restar_numeros()
    if operacion == 3:
        multiplicar_n_numeros()
    if operacion == 4:
        dividir_numeros()
    if operacion == 5:
        factorial()
    if operacion == 6:
        Salir = True
