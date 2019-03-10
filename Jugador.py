

class Jugador:

    def __init__(self,nombre):
        self.nombre = nombre
        self.balance = 0

    def cambioBalance(self,resultado):
        self.balance = self.balance + resultado

    def __str__(self):
        return self.nombre