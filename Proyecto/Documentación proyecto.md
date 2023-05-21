### UNIVERSIDAD DE COSTA RICA  
### ACADEMIA DE TECNOLOGÍA  
### CURSO PROGRAACIÓN EN PYTHON, NIVEL BÁSICO  

### PROYECTO FINAL DEL CURSO  
### Prof. Arturo Zamora  
### Estudiante: René Mora Casal  
### 22 de mayo de 2023  

### DESCRIPCIÓN DEL PROGRAMA ELABORADO (DOCUMENTACIÓN EXTERNA)  

**Qué hace el programa**  

El programa implementa una versión básica del juego de Black Jack, para un  
jugador y la casa (la computadora). Se debe usar programación orientada a  
objetos, lo que implica definir las clases que sean necesarias. También se  
debe llevar registro de los puntajes del jugador y de la casa en unos  
archivos de texto que deben crearse y luego mantenerse actualizados. Hay que  
generar un deck de 52 cartas, y en cada jugada hay que sacar una carta  
aleatoria. Se debe crear un menú que de la opción de crear un jugador o  
usuario, jugar una partida de Black Jack, mostrar estadísticas o salir.

**Pseudocódigo del programa elaborado**

*Paso 1: Definir las clases*

Necesitamos definir las clases que serán necesarias para el juego. Definimos  
cuatro: **Carta**, **Deck**, **Jugador**, **Juego**.

- Clase **Carta**: representa una carta individual con tres atributos, que  
son el valor ("A", "2", "3", ..., "Q", "K"), el palo ("Corazones", "Oros",  
"Tréboles", "Bastos") y el puntaje (usualmente el valor de la carta, excepto  
10 si es figura, 11 si es As). No se intentó darle dos valores al As.  

- Clase **Deck**: contiene una lista de 52 objetos Carta; se definen métodos  
para mezclar aleatoriamente las cartas y sacar una carta aleatoria del mazo.  

- Clase **Jugador**: esta clase representa un jugador en el juego. Tiene dos  
atributos, que son el nombre y el puntaje. Se definen métodos para recibir  
cartas y actualizar el puntaje total. Decimos "actualizar" porque resultó  
mejor calcular el puntaje cada vez que se añade una carta, sino contaba doble.  

- Clase **Juego**: se decidió crear esta clase, que controla las acciones  
principales de una partida de Black Jack, tales como repartir dos cartas,  
permitir que los jugadores tomen decisiones (como pedir más cartas),  
determinar el ganador y guardar los resultados en unos archivos texto. Con  
esto se consigue que el programa princila sea muy corto (cinco líneas).   

*Paso 2: Definir lor parámetros y los métodos:*  

- Clase **Carta**: se define con tres parámetros. El valor y el palo forman  
parte de unas listas predefinidas. Se creó una función interna llamada  
obtener_puntaje(self), que permite calcular el puntaje de la carta y asignarlo.  

- Clase **Deck**: no tiene parámetros (solo "self"). Se define una función  
interna generar_mazo(self) que genera el mazo o baraja de 52 cartas. Se  
definen dos funciones externas -es decir, que son llamadas en otros módulos-  
muy importantes: mezclar_cartas(self) que mezcla aleatoriamente las cartas,  
y sacar_carta(self) que saca la última carta de la lista, esta carta se borra  
del mazo o baraja y la carta se "retorna" para ser usada por otro módulo.  

- Clase **Jugador**: esta clase tiene un parámetro que es un objeto con tres  
parámetros, que son el nombre del jugador -una cadena-, la lista de cartas  
que el jugador tiene en una partida -inicialmente vacía- y el puntaje de la  
partida. Se definen dos importantes funciones, la función externa  
recibir_carta(self, carta) que recibe una carta del mazo, y la función  
interna actualizar_puntaje(self) que calcula el puntaje de las cartas que  
tiene el jugador, y que se actualiza cada vez que se agrega una carta.  

- Clase **Juego**: este es el módulo más extenso por la cantidad de métodos  
y porque hace uso de métodos de los otros módulos. El objeto Juego tiene dos  
parámetros tipo Jugador, que son el Jugador o Player y la Casa o Dealer.  
Además tiene como parámetro interno el objeto Deck, el mazo de cartas.  
Se definen varias funciones importantes, la primera repartir_cartas(self)  
que reparte dos cartas a Jugador y Casa y despliega las cartas, en el caso  
de la Casa solo muestra una carta. La siguiente función es jugar_turno(self,  
jugador) donde el jugador puede pedir cartas o plantarse -si se pasa de 21 el  
programa "lo planta"-. La siguiente función es jugar_turno_casa(self, dealer)  
donde la Casa juega su turno, mientras la suma sea menor que 17. Sigue la  
función Mostrar_resultados(self), muy importante porque muestra los resultados  
de la partida y define quien gana y quien pierde, o bien si hay empate.  Se  
definieron gran cantidad de casos, tratando de cubrir todas las posibilidades  
y también para incluir algunos casos especiales (As y Figura, Tres Sietes y  
Cinco Menores). La penúltima función es actualizar_registros(self) que escribe  
el nombre y puntaje del Jugador en un archivo "registro_jugador.txt" y el  
nombre y puntaje de la casa en un archivo "registro_casa.txt", los archivos  
son creados la primera vez. La última función, no menos importante, es  
iniciar_juego(self) que llama a las funciones anteriores así como a la  
función mezclar_cartas(self) para jugar una partida de Black Jack.

Cada módulo se probó por separado antes de pasar al siguiente, esto se dejó  
como comentarios al final. De hecho, la prueba del módulo Juego sirvió como  
base del programa principal, la opción 2.

**El programa principal**

El programa principal o "Main" despliega un menú de opciones:

1. Crear un usuario (si no lo ingresas, te llamarás Popeye).
2. Jugar una partida.
3. Mostrar las estadísticas Jugador.
4. Mostrar estadísticas de la Casa.
5. Salir.

La programación del menú se basó en la tarea de la calculadora. Se define una  
variable Salir, que al inicio es False y que solo se convierte en True si se  
escoge la opción 5.

Se incluyó un nombre por defecto para el jugador, en caso que se escoja  
directamente la opción 2, sin pasar por la opción 1. Esto se advierte.

La opción 3 contiene las instrucciones para jugar el juego de Black Jack, que  
como indicamos quedó de cinco líneas.

Las opciones 4 y 5 despliegan los cinco últimos registros del Jugador y de la  
Casa, respectivamente.

**Comentarios**  

El proyecto aplica casi todo lo que hemos visto en el curso. Creo que logramos  
implementar un 95% de lo solicitado en el proyecto.

Preliminarme estuvimos investigando sobre los temas de Clases y de Programación  
Orientada a Objetos, para poder entender lo que había que hacer. Luego busqué  
ejemplos de programas en Python que implementaran el juego de Black Jack, pude  
observar que no hay dos implementaciones iguales y la mayoría son muy complejas  
y avanzadas. Para ciertas tareas busqué información en línea para poder  
hacerlas, un ejemplo es la siguiente línea y función:

print(f"Cartas: {', '.join(str(carta) for carta in dealer.cartas)}")

que muestra las cartas de jugador.

El programa o compilador ayuda bastante para localizar y entender los errores.  
Sin embargo, después de escribir el programa y al ir viendo los errores, a  
veces siento que fue por "prueba y error". Por ejemplo, darme cuenta de la  
necesidad de poner "D.Deck.mezclar_cartas(self.deck)", lo inicial y lo de  
adentro. En forma similar con "Player = J.Jugador(Jugador)".  

Siento que faltó más práctica y hacer más ejemplos en clase, es decir que  
nosotros los estudiantes hagamos los ejemplos con la guía del profesor. 

Hubo cosas que no supe implementar, no hubo forma. Por ejemplo, al inicio lo  
traté de hacer para varios jugadores, con la instrucción "for jugador in  
self.jugadores". Sin embargo, el programa me decía que el objeto no era  
iterable, y no encontré una alternativa o solución.

En forma similar con el despliegue de los registros (opciones 3 y 4), lo tuve  
que hacer en una forma "poco eficiente", imprimiendo una por una las líneas  
-1, -2, -3, -4 y -5 pues no supe como hacerlo más corto.












