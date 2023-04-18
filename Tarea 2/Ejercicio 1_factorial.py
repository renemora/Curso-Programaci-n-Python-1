# Ejercicio 1: hacer un programa que calcule el factorial de un número
# Usé la opción de recursividad pues se presenta en la presentación de la clase.
# El usuario debe ingresar un número entero, puede ser cero.
# Tomé en cuenta si se ingresa un número negativo, da una advertencia y no error.
# Todavía no sé cómo evitar que se caiga el programa si ingreso un número con decimal. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    

# hay que dejar dos espacios entre la función y el programa.

num = int(input('Escriba un número entero, mínimo cero: '))
if num < 0:
    print("Has ingresado un número negativo")
if num >= 0:
    fact = factorial(num)
    print("El factorial de", num, "es", fact)