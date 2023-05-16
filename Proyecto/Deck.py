# Se define la clase Deck. Esta clase genera un "deck" o baraja con 52 cartas.
# Se definen funciones para barajar (aleatoriamente) y para sacar una carta.
# Para esta última se usa la función "pop", saca última carta por defecto. 

import random
import Carta as C


class Deck:
    def __init__(self):
        self.cartas = [] 
        # esto es una lista, vacía al inicio, con 52 cartas al final.
        # cada carta con valor, palo y puntaje.
        self.generar_mazo()

    # Función que genera el mazo de 52 cartas. 
    def generar_mazo(self):
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        palos = ["Corazones", "Oros", "Tréboles", "Bastos"]

        for valor in valores:
            for palo in palos:
                carta = C.Carta(valor, palo) # Esta parte me daba error al inicio
                self.cartas.append(carta)
        
    # Función que mezcla aleatoriamente las cartas en el mazo o deck.
    def mezclar_cartas(self):
        random.shuffle(self.cartas)

    # Función que permite sacar la última carta, no se pierde por el "return".
    def sacar_carta(self):
        carta_arriba = self.cartas.pop() 
        return carta_arriba

    # def __str__(self): no le encontré utilidad
    # no puedo imprimir o desplegar el deck
        


# Esto es una prueba
# Mazo = Deck()
# Mazo.mezclar_cartas()

# naipe = Mazo.sacar_carta()
# print(naipe)
# print(f"Quedan {len(Mazo.cartas)} cartas en el deck")