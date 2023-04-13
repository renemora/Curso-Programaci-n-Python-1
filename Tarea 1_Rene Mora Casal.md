## UNIVERSIDAD DE COSTA RICA
## ACADEMIA DE TECNOLOGÍA
### Programación con Python Nivel 1 (IV-2023)
### Inst. Arturo Zamora 
### Alumno: René Mora Casal
### Fecha 30 marzo 2023  

### TAREA 1  

#### I Parte: Ambiente de desarrollo  

Instalamos Python, Visual Code Studio, GitHub Desktop.
Hicimos cuenta GitHub y creamos carpeta para el curso.
Hicimos programa Hola_mundo.py (en español para evidenciar que lo hice yo)
Estamos haciendo la tarea en Visual Code Studio (archivo texto)  

### II Parte: Resolución de problemas  

**Problema 1**  

Se necesita crear un programa que reciba del usuario una frase y decida si 
esa frase es un palíndromo o no. Un palíndromo se puede leer de igual forma de
izquierda a derecha, que de derecha a izquierda. Ejemplo: "Anita lava la tina".

*Paso 1: Leer y entender el problema*  

Necesito recibir del usuario una frase (una cadena de caracteres), luego debo
comparar de alguna manera para determinar si es un palíndromo.  

*Paso 2: Planear*  

Interfaz de usuario e inputs: Mi programa requiere hacer una pregunta al usuario: "Ingrese una frase para 
determinar si es un palíndromo. No incluya espacios ni caracteres especiales
como tildes o eñe".  

Resultado o output: indicar si la frase es o no es un palíndromo. 

Pasos necesarios:
- El usuario ingresa una frase (una cadena o string)  
- Debo contar el número de caracteres de la cadena, la guardo en variable entera N.
- Empiezo a comparar los caracteres así: 1 con N, 2 con N-1, 3 con N-2...
- Si todas las parejas de caracteres son iguales, la frase es un palíndromo.
- Si alguna de las parejas de caracteres no cumple con ser iguales, no es un palíndromo.
- Debo tomar en cuenta si el número de caracteres es par o impar. Esto se hace comparando
solamente hasta el caracter M, donde M es igual a la parte entera de N/2.

*Paso 3: Dividir y conquistar*  

Investigando, hay varias formas de resolver este problema. La mayoría ejecutan algún tipo de ciclo 
IF THEN ELSE.  Una opción interesante es comparar la primera y la última letra: si son iguales, se 
eliminan. El proceso continúa hasta que quede solo una letra o ninguna, si todas las comparaciones 
son igualdad, la palabra es un palíndromo.

*Pseudocódigo*  

Pregunta al usuario: "Ingrese una frase para determinar si es un palíndromo. No incluya espacios ni 
caracteres especiales como tildes o eñe".  

El usuario ingresa la frase, una cadena o string. Definir variable "frase", tipo cadena.  

Contar número de caracteres de la cadena, guardar en variable entera N.  

Definir variables:
- frase, tipo cadena
- i, variable entera
- p, variable entera
- q, variable entera
- M, variable entera
- palindromo, variable booleana  

Asignar valores iniciales:
- p = 1
- q = N
- M = parte entera de cociente N/2
- palindromo = True  

Definir un ciclo o loop FOR/IF/ELSE  

FOR i = 1 to M
IF caracter "p" frase NO IGUAL caracter "q" frase
THEN palindromo = False
p = p + 1
q = q - 1
FIN  

IF palindromo = True 
THEN print("La frase es un palindromo")
ELSE print("La frase no es un palindromo")
FIN

FIN DEL PSEUDOCÍDIGO

**Problema 2**  

Un servidor crea logs por cada acción que se realiza en él. El administrador desea
un programa que todos los días borre todos los logs excepto si el log contiene la
palabra "error"; si contiene esta palabra, se debe copiar el log al directorio "Errores"
y se debe enviar un correo al administrador.  

*Paso 1: Leer y entender el problema.  

A una misma hora todos los días, el programa debe leer cada log. Si la línea no contiene 
la palabra "error", se borra. Si contiene la palabra "error", copia la línea al directorio 
"Errores" y envía un correo al administrador.  

*Paso 2: Planear*  

Interfaz de usuario: mi programa debe verificar periódicamente la hora. Asimismo debe tener acceso 
a los directorios "Logs" y "Errores", y acceso a una interfaz de correo. No hay interacción directa 
con los usuarios.  

Inputs: tiempo (hora), archivos de "logs".  

Outputs: guardar logs con errores en un directorio, mandar correo al administrador.  

Pasos necesarios:  

A una hora determinada, el programa empieza a leer cada log. Supongo que un log es un archivo de 
caracteres.  

El programa busca la palabra "error", una cadena. ¿Incluir Error, ERROR? Depende de cómo aparezca.  

Si no aparece la palabra "error", se borra el log completamente.  

Si aparece la palabra "error", ocurren dos cosas: se copia el log en un directorio "Errores", y se 
manda un aviso al administrador.

*Paso 3: dividir y conquistar*

En este caso, considero que el programa debe leer un log a la vez.

No tengo claro cómo buscar una secuencia determinada ("error") en una cadena de caracteres, como 
para saber si puedo aplicar dividir y conquistar. Supongo que se puede hacer así.

La acción "default" sería borrar el log. También se borra si aparece la palabra "error", pero 
primero se hace lo solicitado (copiar log, mandar aviso).  

Se puede definir una función para cada paso del procedimiento.

*Pseudocódigo*

Leer tiempo.

Si tiempo = hora establecida, empezar programa.  

Empieza un ciclo de acciones:  
- Programa lee primer log de la lista, ubicada en directorio "Logs".
- Programa busca la palabra "error" dentro del archivo log. Puede ser "Error" o "ERROR".
- Si no aparece la palabra buscada, se borra el log.
- Si aparece la palabra buscada, se copia el log en un directorio "Errores", se borra del 
directorio"Logs" y se manda correo de aviso al administrador.  

El programa termina cuando ya no quedan logs en la lista o directorio.  

FIN DEL PSEUDOCÓDIGO.  

**Problema 3**  

Cree una solución que permita al usuario ingresar un número entero. Dado dicho
número, el programa debe determinar si los dígitos de este número se pueden
ordenar de forma tal que el resultado sea un múltiplo de 5.  

*Paso 1: Leer y entender el problema.*  

El programa pide al usuario ingresar un número entero.

¿Qué pasa si ingresa un número negativo, o un número con decimales? ¿Puede ser cero?

El programa reporta si el número se puede reacomodar -sus dígitos- para que sea divisible 
por 5. Se requiere conocer la regla de divisibilidad por 5 (si el número termina en 0 o 5).  

*Paso 2: Planear:*  

Inerfaz de usuario: el programa debe hacer una pregunta al usuario, tal como "ingrese un 
número entero positivo, mayor o igual a cero". Si se ingresa un número negativo o con 
decimales, el programa no hará nada, esto es una decisión de diseño.  

Inputs: un número entero mayor o igual a cero.  

Outputs: reportar si el número se puede reordenar para que sea dividible por 5, o si 
no se pueede hacer esto.  

Pasos necesarios:  

El usuario ingresa un número entero, mayor o igual a cero.  

El programa lee los digitos del número.  

Si uno de los dígitos es cero o cinco, entonces es posible hacer lo solicitado.  

Si la condición se cumple, responder que sí se puede reordenar el número para que sea 
divisible por 5.  

Si la codición no se cumple, responder que no se puede reordenar el número para que sea 
divisible por 5.  

*Pseudocódigo:*  

Definir variables:  
- número, string  
- i, entera  
- N, entera  
- divisible, booleana  

Pregunta al usuario: "ingrese un número entero positivo, mayor o igual a cero".  

IF int(número) mayor o igual que cero THEN  
N = longitud(número)  
Divisible = False  
FOR i = 1 to N  
IF (caracter "i" es igual a 0) OR (caracter "i" es igual a 5)  
THEN Divisible = True  

IF Divisible = True THEN print("el número se puede reordenar para que sea divisible por 5")  
ELSE print("el número NO se puede reordenar para que sea divisible por 5")  

FIN DEL PSEDOCÓDIGO.  