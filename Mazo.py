import random

class Mazo:

    def __init__(self):
        self.cartas = []


    def nuevoMazo(self):
        for i in range(1,5):
            self.cartas.append('A')
            self.cartas.append('J')
            self.cartas.append('Q')
            self.cartas.append('K')
            for j in range(2,11):
                self.cartas.append(str(j))
        random.shuffle(self.cartas)

    def sacarCarta(self):
        return self.cartas.pop()
