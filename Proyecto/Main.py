# Programa principal
# Opciones del juego:
# 1. Crear un usuario.
# 2. Jugar una partida.
# 3. Mostrar las estadísticas.
# 4. Salir.


import Jugador as J
import Juego as JJ


print("BIENVENIDO AL JUEGO DE BLACK JACK!")
print("Opciones del juego:")
print("1: Crear un (nuevo) usuario o jugador.")
print("2. Jugar una partida.")
print("3. Mostrar las estadísticas.")
print("4. Salir.")

opcion_de_juego = int(input("Ingresa una opción:"))

while opcion_de_juego != 4:
    if opcion_de_juego == 1:
        Jugador = str(input("Ingrese nombre del jugador: "))
    elif opcion_de_juego == 2:
        Player = J.Jugador(Jugador)
        Casa = ["La Casa"]
        Dealer = J.Jugador(Casa)

        print(Player)
        print(Dealer)

        Game = JJ.Juego(Player, Dealer)
        Game.iniciar_juego()