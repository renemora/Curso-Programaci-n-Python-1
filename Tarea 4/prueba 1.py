# Función que cuenta las letras, los números y los caracteres especiales en una string.
# Se utiliza un ciclo FOR y las funciones isalpha e isdigit.
# El detalle fue aplicarlas a un caracter por vez.
# Referencia: https://www.w3schools.com/python/ref_string_isalpha.asp
# Referencia: https://www.w3schools.com/python/ref_string_isdigit.asp
 
def contar_caracteres(string):
    # valores iniciales
    letras = 0
    numeros = 0
    caracteres_especiales = 0
    
    # ciclo FOR, revisa un caracter por vez
    for caracter in string:
        # print(caracter), esto fue para ver los caracteres individuales
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        # si no es letra o dígito, es caracter especial
        else:
            caracteres_especiales += 1
    
    print(f"Letras = {letras}")
    print(f"Números = {numeros}")
    print(f"Caracteres especiales = {caracteres_especiales}")


# programa principal
string1 = "a1!b2c*+%"
print("Si string1 = ", string1, "entonces:")
contar_caracteres(string1)
print()

string1 = "P@#yn26at^&i5ve"
print("Si string1 = ", string1, "entonces:")
contar_caracteres(string1)
print()

string1 = input("Ingrese una cadena de caracteres: ")
contar_caracteres(string1)
print("Adiós!")