# Se define la clase Jugador.
# El jugador puede recibir cartas y el puntaje se actualiza.
# Las cartas se guardan en una lista, al inicio vacía.


import Carta as C
import Deck as D


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
        self.cartas = []

    def recibir_carta(self, carta):
        self.cartas.append(carta)
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        # Cuenta todas las cartas y suma los puntajes.
        # Para no sumar dos o más veces lo mismo, reinicia puntaje cada vez.
        # No es lo óptimo pero es como lo resolví.
        self.puntaje = 0
        for carta in self.cartas:
            puntos = C.obtener_puntaje(carta)
            self.puntaje += puntos 

    def __str__(self): # ¿se ocupa?
        # Da error al imprimir Player si no lo incluyo.
        cadena = f"Jugador: {self.nombre}, Puntaje: {self.puntaje}"
        return cadena
# Fin dle módulo.


#Esto es una prueba
Player = Jugador("Juan")
print("El nombre del jugador es ", Player.nombre)
Mazo = D.Deck()
D.Deck.mezclar_cartas(Mazo)
naipe1 = D.Deck.sacar_carta(Mazo)
Player.recibir_carta(naipe1)
print(naipe1, Player.puntaje)
naipe2 = D.Deck.sacar_carta(Mazo)
Player.recibir_carta(naipe2)
print(naipe2, Player.puntaje)
print("Quedan ", len(Mazo.cartas), "cartas")
print(Player)
