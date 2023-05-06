# Función que cuenta las apariciones de cada carácter en una string.
# Usa un ciclo for para moverse por cada caracter
# (similitudes con el ejercicio #1)
# No encontré funciones en w3schools de utilidad, o no supe usarlas (tal vez "update").
# Consulté la siguiente página: https://www.delftstack.com/es/howto/python/occurrences-of-a-character-in-a-string-in-python/ 
# También esta: https://es.stackoverflow.com/questions/181665/python-c%c3%b3mo-contar-palabras-de-un-diccionario-en-un-texto

def cuenta_apariciones(string):
    # Crea un diccionario llamado "contador"
    # Valores iniciales de 0
    # ¡Las claves dentro de un diccionario no pueden repetirse!
    contador = {caracter:0 for caracter in string}
    
    # Revisamos un caracter a la vez
    for caracter in string:
        # Si ya está almacenado... que lo estaría
        if caracter in contador:
            contador[caracter] += 1        
    print(contador)


# Programa principal
string1 = "murciélago"
print("Si string1 = ", string1, ", entonces:")
cuenta_apariciones(string1)
print()

string1 = "ornitorrinco"
print("Si string1 = ", string1, ", entonces:")
cuenta_apariciones(string1)
print()

string1 = input("Ingrese una cadena de caracteres: ")
cuenta_apariciones(string1)
print("Adiós!")