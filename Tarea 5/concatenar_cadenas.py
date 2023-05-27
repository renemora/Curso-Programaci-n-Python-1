# Programa que concatena tres caadenas, basado en la Tarea #2
# Usamos función lambda
# Tuvimos que usar un poco de "prueba y error" para escribir la función.
# La presentación del curso no es clara.

#Ejemplos de prueba, reemplazar

# st1 = "Hola"
# st2 = " "
# st3 = "Mundo"

# st1 = "Mamá "
# st2 = "amasa  "
# st3 = "la masa"

st1 = input("Ingrese cadena 1: ")
st2 = input("Ingrese cadena 2: ")
st3 = input("Ingrese cadena 3: ")

concatenar_cadenas = (lambda a, b, c: a+b+c)(st1, st2, st3)
print(concatenar_cadenas)

# La función original combinaba dos cadenas de la misma longitud.
# Aquí la adaptamos a tres cadenas y solo las sumamos.

lista_strings = ["", "", ""]
# Si definía una lista vacía me daba error, asociado al índice 0.
# No sé cómo arreglar ese error!

# lista_strings = ""
# print(len(lista_strings)) 
# Da longitud cero.

lista_strings[0] = input("Ingrese cadena 1: ")
lista_strings[1] = input("Ingrese cadena 2: ")
lista_strings[2] = input("Ingrese cadena 3: ")

new_string = ""

for i in range(3):
    new_string += lista_strings[i]
  
print(new_string)

