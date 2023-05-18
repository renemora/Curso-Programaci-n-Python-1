# Se define la clase Juego.
# Aquí se definen las acciones principales durante una ronda de Black Jack.
# Esto determina que el programa principal sea muy conciso.
# Incluye seis funciones en los métodos.
# Quedó un poco largo.

import Deck as D
import Jugador as J


class Juego:
    # El juego incluye una lista de jugadores, sin incluir la Casa.
    def __init__(self, jugadores, casa):
        self.jugadores = jugadores
        self.casa = casa
        self.deck = D.Deck()

    # Se reparten las cartas iniciales a jugadores y Casa.
    def repartir_cartas_iniciales(self):
        for jugador in self.jugadores:
            naipe1 = D.Deck.sacar_carta()
            J.Jugador.recibir_carta(jugador, naipe1)
            print(jugador.nombre, "recibió", naipe1)
            naipe2 = D.Deck.sacar_carta()
            J.Jugador.recibir_carta(jugador, naipe2)
            print(jugador.nombre, "recibió", naipe2)

        for dealer in self.casa:
            dealer.nombre = "la Casa"
            naipe1 = D.Deck.sacar_carta()
            J.Jugador.recibir_carta(dealer, naipe1)
            print(dealer.nombre, "recibió X X")
            naipe2 = D.Deck.sacar_carta()
            J.Jugador.recibir_carta(dealer, naipe2)
            print(dealer.nombre, "recibió", naipe2)        

    # Un jugador juega su turno, pide cartas o se planta.
    def jugar_turno(self, jugador):
        print(f"Turno de {jugador.nombre}:")
        print(f"Cartas: {', '.join(str(carta) for carta in jugador.cartas)}")
        # Ejemplo de programación funcional.
        # Uso de la función str.join(): 
        # https://es.stackoverflow.com/questions/300551/concatenar-y-convertir
        print(f"Puntaje: {jugador.puntaje}")
        print()

        pedir_carta = "s"
        while pedir_carta.lower() == "s" and jugador.puntaje < 21:
        # Uso de función str.lower():
        # https://www.w3schools.com/python/ref_string_lower.asp
            pedir_carta = input("¿Pedir una carta adicional? (s/n): ")
            if pedir_carta.lower() == "s":
                naipe = D.Deck.sacar_carta()
                J.Jugador.recibir_carta(jugador,naipe)
                print(f"Has recibido la carta: {naipe}")
                print(f"Puntaje actualizado: {jugador.puntaje}")
                print()

        print(jugador.nombre, "se planta")

    # La Casa juega su turno, pide cartas o se planta si puntaje >= 17.
    def jugar_turno_casa(self, dealer):
        dealer.nombre = "la Casa"
        
        print("Turno de ", dealer.nombre,":")
        print(f"Cartas: {', '.join(str(carta) for carta in dealer.cartas)}")
        print(f"Puntaje: {dealer.puntaje}")
        print()

        while dealer.puntaje < 17:
            naipe = D.Deck.sacar_carta()
            J.Jugador.recibir_carta(dealer, naipe)
            print(f"La Casa ha recibido la carta: {naipe}")
            print(f"Puntaje actualizado: {dealer.puntaje}")
            print()

        print("La Casa se planta.")

    def mostrar_resultados(self):
        print("----------------------------------")
        print("Resultados de la partida:")
        print()

        # Todos los posibles casos, incluidos casos especiales.
        for jugador in self.jugadores:
            if jugador.puntaje > 21:
                print(f"{jugador.nombre}: Te pasaste de 21, ¡Pierdes!")
            elif self.casa.puntaje > 21:
                print("La Casa se pasó de 21, ¡Ganas!")
            elif jugador.puntaje < 21 and jugador.puntaje > self.casa.puntaje:
                print(f"{jugador.nombre}: Superaste a la Casa, ¡Ganas!")
            elif jugador.puntaje == self.casa.puntaje:
                print(f"{jugador.nombre}: ¡Empate!.")
            elif jugador.puntaje > 21 and self.casa.puntaje > 21:
                print("Ambos se pasaron de 21, ¡Empate!.")
            elif jugador.puntaje == 21 and self.casa.puntaje != 21:
                print(f"{jugador.nombre}:¡Tenés un Black Jack! ¡Ganas!")
                # Esto cubre los casos de tres sietes y As + Figura.
            elif len(jugador.cartas) == 5:
                if jugador.cartas.valor in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print(f"{jugador.nombre}: ¡Tenés cinco  menores! ¡Ganas!")
            else:
                print(f"{jugador.nombre}: La Casa te supera, ¡Pierdes!.")
        print()

    # Anotamos los registros de los jugadores en un archivo de texto.
    def actualizar_registros(self):
        archivo_1 = open("registro_jugadores.txt", 'a')
        for jugador in self.jugadores:
            archivo_1.write(str(jugador.nombre), ", ", str(jugador.puntaje), '\n')
        archivo_1.close()
        
        archivo_1 = open("registro_casa.txt", 'a')
        archivo_1.write(str(self.casa.nombre), ", ", str(self.casa.puntaje), '\n')
        archivo_1.close()


    # Mecánica básica del juego de Blackjack.
    def iniciar_juego(self):
        print("¡Bienvenido al juego de Blackjack!")
        print("----------------------------------")

        D.Deck.mezclar_cartas()

        self.repartir_cartas_iniciales()

        for jugador in self.jugadores:
            self.jugar_turno(jugador)

        dealer = self.casa
        self.jugar_turno_casa(dealer)

        self.mostrar_resultados()

        self.actualizar_registros()
# Fin del módulo.


# Esto es una prueba.
Players = J.Jugador("Juan", "Pedro")
Dealer = J.Jugador("La Casa")

Game = Juego(Players, Dealer)

Game.iniciar_juego()
