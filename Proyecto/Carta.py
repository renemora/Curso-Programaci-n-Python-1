# Se define la clase Carta. Define una carta con palo, valor y puntaje.
# Los palos serían Corazones, Oros, Tréboles y Bastos.
# Los valores son A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q y K.
# El puntaje se calcula según las reglas del Blackjack.
# Puntaje del As se definió como 11 (en Blackjack puede ser 1 también).
# La función obtener_puntje no tiene parámetros (solo self).
# Para implementar el método especial __str__, consulté esta página:
# https://tutorialesprogramacionya.com/pythonya/detalleconcepto.php?codigo=49 

class Carta: 
    def __init__(self, valor, palo): 
        self.valor = valor 
        self.palo = palo
        self.puntos = obtener_puntaje(self)

    def __str__(self):
        cadena = self.valor + " de " + self.palo 
        return cadena


# Se define una función para obtener el puntaje de una carta.
# Se parece a una de las tareas.


def obtener_puntaje(self):
    if self.valor.isdigit():
        return int(self.valor)
    elif self.valor in ["J", "Q", "K"]:
        return 10
    elif self.valor == "A":
        return 11


# Esto es una prueba
# naipe = Carta("A", "Bastos")
# print(naipe)
# puntos = obtener_puntaje(naipe)
# print(puntos)
# print(naipe.puntos)
