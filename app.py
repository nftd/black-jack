from Mazo import Mazo
from Jugador import Jugador

puntosA = [('A',1),('J',10),('Q','10'),('K',10)]
puntosB = [('A',11),('J',10),('Q','10'),('K',10)]
for i in range(2,11):
    puntosA.append((str(i),i))
    puntosB.append((str(i), i))

def chequearPerder(cartaJugador):


if __name__ == '__main__':
    jugador = Jugador(input("Ingrese el nombre del jugador: "))
    print("Hola {}".format(jugador))

    mazo = Mazo()
    mazo.nuevoMazo()

    apuesta = input("Ingrese el monto a apostar: ")
    cartasA = [mazo.sacarCarta(), mazo.sacarCarta()]
    cartasB = [mazo.sacarCarta(), mazo.sacarCarta()]
    print("Cartas de %s: %s %s" % (jugador.nombre,cartasA[0],cartasA[1]))
    print("Cartas de la casa: %s XX" % (cartasB[0]))

    sumaA = 0
    for i in cartasA:
        for j in puntosA:
            if i == j[0]:
                sumaA = sumaA + j[1]
                break
    if sumaA > 21:
        True
    sumaB = 0
    for i in cartasA:
        for j in puntosB:
            if i == j[0]:
                sumaB = sumaB + j[1]
                break
    if sumaB > 21:
        True

