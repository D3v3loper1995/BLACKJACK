import random

colorNormal = '\033[0;m'
rojo, negro = '\033[0;31m', '\033[0;30m'


def set_cartas():
    puntos = 0
    # Colores
    colorcarta = '\033[0;30m', '\033[0;31m'
    cartas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14)
    palos = (colorcarta[1] + '♥'), (colorcarta[1] + '♦'), (colorcarta[0] + '♠'), (colorcarta[0] + '♣')
    carta, palo = random.choice(cartas), random.choice(palos)

    if carta == 1:
        puntos = 11
        carta = 'AS'

    # J Q K = 10
    elif carta == 12 or carta == 13 or carta == 14:
        if carta == 12:
            carta = 'J'
            puntos = 10

        elif carta == 13:
            carta = 'Q'
            puntos = 10

        else:
            carta = 'K'
            puntos = 10

    else:
        puntos = carta

    return carta, palo, puntos


opcion, puntosTotalesJug, op2, pCru = 0, 0, 0, 0
cartasExtras = ''
menor, primera, a = False, False, False

# Al inicio del juego se debe solicitar al jugador su nombre y que indique el monto que desea tener de pozo para
# poder jugar al Blackjack, no pudiendo ser este monto mayor a $100000.
print('*' * 60)
print('\t\t\t\t', rojo, '♥', colorNormal, negro, '♠', colorNormal, 'BLACKJACK', rojo, '♦', colorNormal, negro, ' ♣', colorNormal)
print('*' * 60)
nombre = input('Ingrese el nombre del jugador: ')
pozo = float(input('Ingrese el monto que va a tener de pozo: $ '))
print('*' * 60)

if pozo <= 100000:
    menor = True

    if pozo:
        """
        Y luego se pide implementar un programa controlado por menú de opciones en el que las opciones sean:
        """
        while opcion != 3:
            print('1-Apostar')
            print('2-Jugar una Mano')
            print('3-Salir')
            print('*' * 60)
            opcion = int(input('Ingrese la opcion a ejecutar: '))

            if opcion == 1:
                """
                Apostar: En esta opción del menú el jugador puede sumar dinero a su pozo. El valor a sumar no puede ser 
                negativo ni cero. Puede volver a esta opción del menú las veces que quiera.
                """
                if pozo == 100000:
                    print('*' * 60)
                    print('Pozo maximo')
                    print('*' * 60)

                else:
                    print('*' * 60)
                    canSumar = float(input('Ingrese el dinero a cargar en su pozo: $ '))
                    pozo += canSumar
                    if pozo <= 100000:
                        if 0 < canSumar < 100000:
                            print('Saldo Actual: $', pozo)

                    else:
                        print('*' * 60)
                        print('El pozo esta lleno')
                        print('*' * 60)

            if opcion == 2:
                """
                Jugar una Mano: En esta opción del menú se debe realizar el juego tanto del jugador como del crupier. 
                Inicialmente debe definir el monto a apostar por la mano."""
                print('*' * 60)
                print('Atencion el monto de la apuesta debe ser multiplo de 5.')
                print('*' * 60)
                apuesta = float(input('Ingrese el monto a apostar: $ '))
                print()
                """Si el jugador no tuviera suficiente dinero para realizar una apuesta, no podrá jugar pero el programa 
                no finaliza porque tiene la opción de apostar en el menú principal.
                
                La apuesta debe ser múltiplo de 5 y menor o igual al dinero que posee en su pozo. 
                Las reglas nuevas que aplican en este práctico son (Sin Split ni Rendición, para quienes averigüen del juego):"""
                if apuesta % 5 == 0 and apuesta <= pozo:

                    print('Cartas', nombre, ':')
                    # cartas jugador
                    for i in range(2):
                        """El jugador recibe dos cartas inicialmente"""
                        cartaJugador, paloJugador, puntosJugador = set_cartas()

                        if i == 0 and puntosJugador == 11:
                            primera = True
                            puntosTotalesJug += puntosJugador
                        elif primera and puntosJugador == 11:
                            puntosTotalesJug = puntosJugador + 1
                        else:
                            puntosTotalesJug += puntosJugador

                        print(' |', cartaJugador, paloJugador + colorNormal, end='|')
                    print(' Puntos', nombre, ':', puntosTotalesJug)
                    primera = False

                    # carta del crupier
                    cartaCrupier, paloCrupier, puntosCrupier = set_cartas()
                    print('\nCartas Crupier:\n', '|', cartaCrupier, paloCrupier + colorNormal, end='|')
                    print(' Puntos Crupier: ', puntosCrupier)
                    print('\n' + '*' * 60)
                    """ y a partir de ese momento puede seguir pidiendo cartas hasta que 
                    decida frenar o bien logre 21 o se pase."""
                    while op2 != 2 or puntosTotalesJug > 21:
                        if puntosTotalesJug != 21:
                            print(nombre)
                            op2 = int(input('Desea otra carta 1- Si / 2- No: '))
                            if op2 == 1:
                                carta1Jugador, palo1Jugador, puntosJugador = set_cartas()

                                if puntosJugador == 11 and 12 > puntosTotalesJug < 21:
                                    puntosTotalesJug += 11

                                elif puntosJugador == 11:
                                    puntosTotalesJug += 1

                                else:
                                    puntosTotalesJug += puntosJugador

                                print(' |', carta1Jugador, palo1Jugador + colorNormal, end='|')
                                print(' nombre: ', puntosTotalesJug)

                            if puntosTotalesJug >= 21:
                                print('*' * 60)
                                break

                    # sigue juego del crupier
                    """
                    Su juego continúa cuando el jugador termina. Debe pedir cartas mientras tenga
                    16 o menos de puntaje y plantarse con 17 o más, siendo indefinida la cantidad de cartas
                    hasta lograrlo.
                    """
                    while pCru != 2:
                        pass

                    # PROCESO DEL CRUPIER
                    print('*' * 60)
                    print('\t\t\t\t\t\t RESULTADOS')
                    print('*' * 60)
                    print('Monto inicial del pozo: $', pozo)
                    print('Monto de la apuesta: $', apuesta)

                    print()
                    puntosTotalesJug, op2, pCru = 0, 0, 0

                else:
                    print('El monto de la apuesta es mayor al saldo actual del pozo, porfavor ingrese mas dinero.')
                    print('*' * 60)
else:
    print('El monto ingresado es superior al limite establecido por el Casino.')
