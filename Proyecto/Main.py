# Programa principal
# Opciones del juego:
# 1. Crear un usuario (si no lo ingresas, te llamarás Popeye).
# 2. Jugar una partida.
# 3. Mostrar las estadísticas Jugador.
# 4. Mostrar estadísticas de la Casa.
# 4. Salir.


import Jugador as J
import Juego as JJ


Salir = False
Jugador = "Popeye"
# Si por alguna razón no ingresan nombre del jugador, se llamará Popeye.

while not Salir:
    print("BIENVENIDO AL JUEGO DE BLACK JACK!")
    print("Opciones del juego:")
    print("1: Crear un (nuevo) usuario o jugador.")
    print("2. Jugar una partida.")
    print("3. Mostrar las estadísticas del jugador.")
    print("4. Mostrar las estadísticas de la Casa.")
    print("5. Salir.")

    opcion_de_juego = int(input("Ingresa una opción:"))

    if opcion_de_juego == 1:
        Jugador = str(input("Ingrese nombre del jugador: "))

    if opcion_de_juego == 2:
        Player = J.Jugador(Jugador)
        Casa = "La Casa"
        Dealer = J.Jugador(Casa)

        Game = JJ.Juego(Player, Dealer)
        Game.iniciar_juego()

    if opcion_de_juego == 3:
        archivo_1 = open("registro_jugadores.txt", 'r')
        salida_1 = archivo_1.readlines()
        print(salida_1[-5], end="")
        print(salida_1[-4], end="")
        print(salida_1[-3], end="")
        print(salida_1[-2], end="")
        print(salida_1[-1], end="")
        archivo_1.close()
        print()

    if opcion_de_juego == 4:
        archivo_1 = open("registro_casa.txt", 'r')
        salida_1 = archivo_1.readlines()
        print(salida_1[-5], end="")
        print(salida_1[-4], end="")
        print(salida_1[-3], end="")
        print(salida_1[-2], end="")
        print(salida_1[-1], end="")
        archivo_1.close()
        print()

    if opcion_de_juego == 5:
        Salir = True
        print("Adiós!")
        print()