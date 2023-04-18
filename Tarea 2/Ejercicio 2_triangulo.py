# Ejercicio #2: hacer un programa que genere un triángulo de números.
# El usuario debe ingresar un número entero.
# No debe ser negativo ni cero.
# Busqué cómo decirle a "print" que no cambie de línea (parámetro end).

num = int(input("Ingresa un número entero positivo, no cero: "))

if num < 0:
    print("El número no puede ser negativo")

if num == 0:
    print("El número no puede ser cero")

i = 1
while i <= num:
    j = 1
    while j <= i:
        print(j, end = " ")
        j += 1
    i += 1
    print("")


