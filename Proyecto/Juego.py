# Se define la clase Juego.
# Aquí se definen las acciones principales durante una ronda de Black Jack.
# Esto determina que el programa principal sea muy conciso.
# Incluye seis funciones en los métodos.
# Quedó un poco largo.
# Traté de hacerlo para N jugadores, pero la frase "for jugador in self.jugadores"
# me daba el error "objetc not iterable", por lo que lo hice con un solo jugador.
# Traté de implementar unas variables status_jugadr y status_casa, con valores
# "Ganó", "Perdió", "Empate", pero a la hora de escribirlas en los archivos de
# registro no me la reconocía.  


import Deck as D
import Jugador as J
# import os


class Juego:
    # El juego incluye un jugador y la Casa, ambos clase Jugador, por aparte.
    # Me entra la duda de cómo Python reconoce a jugador y casa como clase "Jugador",
    # solo sé que funciona.
    def __init__(self, jugador, casa):
        self.jugador = jugador
        self.casa = casa
        self.deck = D.Deck()
   
    # Se reparten las cartas iniciales a jugadores y Casa.
    def repartir_cartas_iniciales(self):
        naipe1 = D.Deck.sacar_carta(self.deck)
        J.Jugador.recibir_carta(self.jugador, naipe1)
        print(self.jugador.nombre, "recibió", naipe1)
        naipe2 = D.Deck.sacar_carta(self.deck)
        J.Jugador.recibir_carta(self.jugador, naipe2)
        print(self.jugador.nombre, "recibió", naipe2)

        naipe1 = D.Deck.sacar_carta(self.deck)
        J.Jugador.recibir_carta(self.casa, naipe1)
        print(self.casa.nombre, "recibió X X")
        naipe2 = D.Deck.sacar_carta(self.deck)
        J.Jugador.recibir_carta(self.casa, naipe2)
        print(self.casa.nombre, "recibió", naipe2)        

    # Jugador juega su turno, pide cartas o se planta.
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
                naipe = D.Deck.sacar_carta(self.deck)
                J.Jugador.recibir_carta(jugador,naipe)
                print(f"Has recibido la carta: {naipe}")
                print(f"Puntaje actualizado: {jugador.puntaje}")
                print()

        print(jugador.nombre, "se planta")

    # La Casa juega su turno, pide cartas o se planta si puntaje >= 17.
    def jugar_turno_casa(self, dealer):
        print("Turno de ", dealer.nombre,":")
        print(f"Cartas: {', '.join(str(carta) for carta in dealer.cartas)}")
        print(f"Puntaje: {dealer.puntaje}")
        print()

        while dealer.puntaje < 17:
            naipe = D.Deck.sacar_carta(self.deck)
            J.Jugador.recibir_carta(dealer, naipe)
            print(f"La Casa ha recibido la carta: {naipe}")
            print(f"Puntaje actualizado: {dealer.puntaje}")
            print()

        print("La Casa se planta.")

    # Mostrar los resultados del jugador y de la Casa.
    def mostrar_resultados(self):
        print("----------------------------------")
        print("Resultados de la partida:")
        print()

        # Todos los posibles casos, incluidos casos especiales.
        if self.casa.puntaje == 21:
            print("La Casa tiene 21, ¡Pierdes!")
            print()
        elif self.jugador.puntaje > 21:
            print(f"{self.jugador.nombre}: Te pasaste de 21, ¡Pierdes!")
            print()
        elif self.casa.puntaje > 21:
            print("La Casa se pasó de 21, ¡Ganas!")
            print()
        elif self.jugador.puntaje == 21 and self.casa.puntaje == 21:
            print("Ambos obtuvieron 21. ¡Empate!")
            print()
        elif self.jugador.puntaje < 21 and self.jugador.puntaje > self.casa.puntaje:
            print(f"{self.jugador.nombre}: Superaste a la Casa, ¡Ganas!")
            print()
        elif self.jugador.puntaje == self.casa.puntaje:
            print(f"{self.jugador.nombre}: ¡Empate!.")
            print()
        elif self.jugador.puntaje > 21 and self.casa.puntaje > 21:
            print("Ambos se pasaron de 21, ¡Empate!.")
            print()
        elif len(self.jugador.cartas) == 3 and self.jugador.cartas.valor in [7]:
        # Esto implica tener tres sietes, igual a 21.
            if self.casa.puntaje != 21: 
                print(f"{self.jugador.nombre}:¡Tenés As y Figura! ¡Ganas!")
                print()
        elif len(self.jugador.cartas) == 2 and self.jugador.puntaje == 21:
        # Esto solo es posible con As y Figura.
            if self.casa.puntaje != 21: 
                print(f"{self.jugador.nombre}:¡Tenés As y Figura! ¡Ganas!")
                print()
        elif len(self.jugador.cartas) == 5 and self.jugador.puntaje < 21:
        # Caso de cinco menores.
            if self.jugador.cartas.valor in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print(f"{self.jugador.nombre}: ¡Tenés cinco  menores! ¡Ganas!")
                print()
        elif self.jugador.puntaje == 21 and self.casa.puntaje != 21:
        # Cualquier otro caso que sume 21.
            print(f"{self.jugador.nombre}:¡Tenés un Black Jack! ¡Ganas!")
            print()
        else:
            print(f"{self.jugador.nombre}: La Casa te supera, ¡Pierdes!.")
            print()

    # Anotamos los registros de los jugadores en un archivo de texto.
    def actualizar_registros(self):
        archivo_1 = open("registro_jugadores.txt", 'a')
        archivo_1.write(str(self.jugador.nombre)+", "+str(self.jugador.puntaje)+'\n')
        # Error inicial: TextIOWrapper.write() takes exactly one argument (4 given).
        # Procedemos a sumar todas las cadenas.
        archivo_1.close()
        print()
        
        archivo_1 = open("registro_casa.txt", 'a')
        archivo_1.write(str(self.casa.nombre)+", "+str(self.casa.puntaje)+'\n')
        archivo_1.close()
        print()

    # Mecánica básica del juego de Blackjack.
    def iniciar_juego(self):
        print("¡Bienvenido al juego de Blackjack!")
        print("----------------------------------")

        D.Deck.mezclar_cartas(self.deck)

        self.repartir_cartas_iniciales()

        self.jugar_turno(self.jugador)

        self.jugar_turno_casa(self.casa)

        self.mostrar_resultados()

        self.actualizar_registros()
# Fin del módulo.


# Esto es una prueba. Básicamente esto va al principal.
# Jugador = ["Juan"]
# Player = J.Jugador(Jugador)
# Casa = ["La Casa"]
# Dealer = J.Jugador(Casa)

# print(Player)
# print(Dealer)

# Game = Juego(Player, Dealer)
# Game.iniciar_juego()
