#Ejercicio 3 - combinar cadenas de caracteres.
#El usuario ingresa dos cadenas de caracteres, de la misma longitud.
#Si son de distinta longitud, se genera un mensaje de advertencia".
#Luego el programa genera un error.
#Traté de aplicar los statements break y continue, pero no los acepta (por ser un if).
#Si las cadenas son de la misma longitud, procede a combinarlas.

print("Ingrese dos cadenas de caracteres, de la misma longitud cada una")

string1 = input("Ingrese la primera cadena de caracteres: ")
string2 = input("Ingrese la segunda cadena de caracteres: ")

long1 = len(string1)
long2 = len(string2)

if long1 != long2:
    print("Las cadenas no tienen la misma longitud")
    
new_string = ""

if long1 == long2:
    for i in range (long1):
        new_string += string1[i]
        new_string += string2[i]
   
print(new_string)