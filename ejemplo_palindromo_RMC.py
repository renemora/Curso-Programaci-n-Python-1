string = input('Escriba una oración, no incluya tildes:')
input_min = string.lower()
input_min = input_min.replace(" ","")
string2 = input_min[0:5]
print(input_min)
print(string2)

if input_min != input_min[::-1]:
    print('es un palíndromo')
else:
    print('No es un palíndromo')

# if input_min[0] == input_min[-1]
#     print("Esta frase podría ser un palíndromo")
# else:
#     print("Esta frase NO es un palíndromo")

# i = 0
# is_palindromo = True
# while i < len(input_min) / 2 and is_palindromo:
#     if input_min[i] != input_min[-(i+1)]:
#         print('Esta frase NO es un palíndromo')
#         is_palindromo = False
#         break
#     else:
#         i += 1
# if is_palindromo: print('Esta frase SI es un palíndromo')