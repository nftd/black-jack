from Mazo import Mazo
from Jugador import Jugador
import os

puntosA = [('A',1),('J',10),('Q',10),('K',10)]
puntosB = [('A',11),('J',10),('Q',10),('K',10)]
for i in range(2,11):
    puntosA.append((str(i),i))
    puntosB.append((str(i), i))

def chequearPerder(cartaJugador):
    global puntosA,puntosB
    sumaA = 0
    for i in cartaJugador:
        for j in puntosA:
            if i == j[0]:
                sumaA = sumaA + j[1]
                break
    if sumaA > 21:
        return True
    sumaB = 0
    for i in cartaJugador:
        for j in puntosB:
            if i == j[0]:
                sumaB = sumaB + j[1]
                break
    if sumaB > 21:
        return True
    return False


def chequear21(cartaJugador):
    global puntosA,puntosB
    sumaA = 0
    for i in cartaJugador:
        for j in puntosA:
            if i == j[0]:
                sumaA = sumaA + j[1]
                break
    if sumaA == 21:
        return True
    sumaB = 0
    for i in cartaJugador:
        for j in puntosB:
            if i == j[0]:
                sumaB = sumaB + j[1]
                break
    if sumaB == 21:
        return True
    return False

def mostrarMesa(turnoJugador = True):
    os.system('cls' if os.name == 'nt' else 'clear')
    if turnoJugador:
        print("Cartas de %s: %s" % (jugador.nombre, cartasA))
        print("Cartas de la casa: %s XX" % (cartasB[0]))
    elif turnoJugador == False:
        print("Cartas de %s: %s" % (jugador.nombre, cartasA))
        print("Cartas de la casa: %s" % (cartasB))


if __name__ == '__main__':
    #jugador = Jugador(input("Ingrese el nombre del jugador: "))
    jugador = Jugador('Nico')
    print("Hola {}".format(jugador))


    mazo = Mazo()
    mazo.nuevoMazo()

    #apuesta = input("Ingrese el monto a apostar: ")
    apuestas = 50
    cartasA = [mazo.sacarCarta(), mazo.sacarCarta()]
    cartasB = [mazo.sacarCarta(), mazo.sacarCarta()]
    #print("Cartas de %s: %s %s" % (jugador.nombre,cartasA[0],cartasA[1]))
    mostrarMesa()

    if chequear21(cartasA) == False:
        respuesta1 = 's'
        while respuesta1 == 's' and chequearPerder(cartasA) == False and chequear21(cartasA) == False:
            respuesta1 = input("Desea una carta mas? (s/n): ")
            if respuesta1 == 's':
                cartasA.append(mazo.sacarCarta())
                mostrarMesa()
                if chequearPerder(cartasA) or chequear21(cartasA):
                    break
                print(chequearPerder(cartasA))
                print(chequear21(cartasA))

        mostrarMesa(False)
        cartasB.append(mazo.sacarCarta())
        mostrarMesa(False)
        if chequearPerder(cartasA):
                jugador.cambioBalance(-apuestas)
                print("Casa gana, nuevo balance de %s: %s" %(jugador,jugador.balance))
        elif chequearPerder(cartasB):
            jugador.cambioBalance(apuestas)
            print("%s gana, nuevo balance: %s"%(jugador.nombre,jugador.balance))

