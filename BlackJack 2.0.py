import random

normal = '\033[0;m'
rojo, negro, verde, amarillo = '\033[0;31m', '\033[0;30m', '\033[92m', '\033[93m'


def set_cartas():
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


def verificar_ganador(puntosjugador, apu, poz, nom, puntoscrupier):
    win_j, win_c = False, False
    if puntosjugador <= 21 and puntoscrupier <= 21:

        if puntosjugador > puntoscrupier:
            print(verde, 'El ganador es:', nom, normal)
            total = apu * 2 + poz
            win_j = True

        elif puntosjugador == puntoscrupier:
            print(verde, 'Empate', normal)
            total = poz + apu
            win_c = True
        else:
            print(verde, 'El ganador es el Crupier', normal)
            total = poz
            win_c = True

    else:
        if 21 >= puntosjugador < puntoscrupier:
            print(verde, 'El ganador es:', nom, normal)
            win_j = True
            total = apu * 2 + poz
        else:
            print(verde, 'El ganador es el Crupier', normal)
            total = poz
            win_c = True

    return total, win_j, win_c


def monto_may(a, b):
    if a > b:
        mayor = a
    else:
        mayor = b

    return mayor


def porcentaje_victorias(ganadas, total):
    porcentaje = ganadas * 100 // total
    return porcentaje


def principal():
    # Contadores inicio
    pozo, opcion = 0, 0
    # Contadores op1
    can_sumar = 0
    # Contadores op2
    # apuesta, pozo_modificado, nuevo_valor = 0, 0, 0
    carta_jugador, puntos_jugador, puntos_totales_jug, op_jug, rondas_ganadas_jug = 0, 0, 0, 0, 0
    primera, black_natural_jug, black_natural_cru = False, False, False
    carta_crupier, puntos_crupier, puntos_totales_cru, op_cru, cant_cartas_cru = 0, 0, 0, 0, 0
    # Contadores op3
    entrada, valor_maximo, mayor, cantidad_black_natural, rondas_totales, victorias_por = 0, 0, 0, 0, 0, 0
    racha_crupier, racha_mayor_cru, total_apuestas, monto_promedio, perdida_mayor = 0, 0, 0, 0, 0
    ganador_cru = False

    print(rojo, '*' * 80)
    print('\t\t\t\t\t\t\t', rojo, '♥', normal, negro, '♠', verde, 'BLACKJACK', rojo, '♦', normal, negro, ' ♣',
          normal)
    print(rojo, '*' * 80, normal)
    nombre = input(' Ingrese el nombre del jugador: ')
    pozo = float(input(' Ingrese el monto que va a tener de pozo: $ '))
    print('*' * 80)

    while pozo <= 0 or pozo >= 100000:
        if pozo <= 0:
            print(rojo, ' El pozo ingresado es menor a cero', normal)
        else:
            print(rojo, ' EL pozo ingresado supera al limite establecido por el Casino.', normal)
        pozo = float(input('Ingrese el monto que va a tener de pozo: $ '))
        print('*' * 80)

    while opcion != 3:
        print(verde, '1', normal, '-Apostar')
        print(verde, '2', normal, '-Jugar una Mano')
        print(verde, '3', normal, '-Salir')
        print('*' * 80)
        opcion = int(input(' Ingrese la opción a ejecutar: '))

        if opcion == 1:
            if pozo >= 100000:
                print('*' * 80)
                print(rojo, ' Pozo máximo, no puede ingresar mas dinero', normal)
                print('*' * 80)

            else:
                print('*' * 80)
                print(amarillo, '⚠ Atención el monto de la apuesta debe ser múltiplo de 5.', normal)
                print('*' * 80)

                while can_sumar > -1:
                    can_sumar = float(input(' Ingrese el dinero a depositar en su pozo: $ '))

                    if can_sumar % 5 == 0 and can_sumar > 0:
                        pozo += can_sumar
                        if pozo >= 100000:
                            print('*' * 80)
                            print(rojo, 'Pozo máximo, no puede ingresar esa cantidad de dinero\n'
                                        ' Intente nuevamente con un valor menor.', normal)

                            print('*' * 80)
                            pozo -= can_sumar
                        else:
                            print(' Saldo Actual: $ ', pozo)
                            print('*' * 80)
                            break

                    else:
                        if can_sumar < 0:
                            print(rojo, ' Valor ingresado es menor a cero', normal)
                            print('*' * 80)
                        else:
                            print(rojo, 'El valor ingresado no es múltiplo de 5', normal)

            can_sumar = 0

        elif opcion == 2:
            print('*' * 80)
            apuesta = float(input(' Ingrese el monto a apostar: $ '))
            print()

            if 0 < apuesta <= pozo:
                entrada += 1
                pozo_modificado = pozo - apuesta
                total_apuestas += apuesta
                print(verde, 'Cartas', nombre, ':', normal)
                # cartas jugador
                for i in range(2):
                    carta_jugador, palo_jugador, puntos_jugador = set_cartas()

                    # doble as
                    if i == 0 and puntos_jugador == 11:
                        primera = True
                        puntos_totales_jug += puntos_jugador

                    elif primera and puntos_jugador == 11:
                        puntos_totales_jug = puntos_jugador + 1

                    else:
                        # as y j/q/k
                        if primera and puntos_jugador == 10:
                            black_natural_jug = True
                            puntos_totales_jug += puntos_jugador

                        # otros
                        else:
                            puntos_totales_jug += puntos_jugador

                    print(' |', carta_jugador, palo_jugador + normal, end='|')
                print(' Puntos', nombre, ':', puntos_totales_jug)
                # Reiniciamos la bandera
                primera = False

                # carta del crupier
                carta_crupier, palo_crupier, puntos_crupier = set_cartas()
                puntos_totales_cru += puntos_crupier
                print(verde, '\n Cartas Crupier:\n', normal, '|', carta_crupier, palo_crupier + normal, end='|')
                print('Puntos Crupier: ', puntos_crupier)
                print('\n' + '*' * 80)

                if black_natural_jug is False:
                    while op_jug != 2 or puntos_totales_jug > 21:
                        if puntos_totales_jug != 21:
                            print(verde, nombre, normal)
                            op_jug = int(input(' Desea otra carta 1- Si / 2- No: '))
                            if op_jug == 1:
                                carta_jugador, palo_jugador, puntos_jugador = set_cartas()

                                # dos cartas qeu sumen menos 12 al as lo toma como 11
                                if puntos_jugador == 11 and 12 > puntos_totales_jug:
                                    puntos_totales_jug += 11

                                # si suma más de 12 con las dos cartas el as vale 1
                                elif puntos_jugador == 11:
                                    puntos_totales_jug += 1

                                else:
                                    # otros
                                    puntos_totales_jug += puntos_jugador

                                print(' |', carta_jugador, palo_jugador + normal, end='|')
                                print('Puntos', nombre, ': ', puntos_totales_jug)

                        if puntos_totales_jug >= 21:
                            break

                        # sigue juego del crupier

                if puntos_totales_cru <= 16:
                    while op_cru != 2:
                        print(verde, 'Crupier', normal)
                        op_cru = int(input(' Desea otra carta 1- Si / 2- No: '))

                        if op_cru == 1:
                            cant_cartas_cru += 1
                            carta_crupier, palo_crupier, puntos_crupier = set_cartas()

                            # doble as
                            if cant_cartas_cru == 1 and puntos_crupier == 11:
                                if puntos_totales_cru == 11:
                                    puntos_totales_cru = puntos_crupier + 1

                            # j/q/k as
                            if puntos_crupier == 10 and puntos_totales_cru == 11:
                                black_natural_cru = True
                                puntos_totales_cru += puntos_crupier

                            # as j/q/k
                            elif puntos_crupier == 11 and puntos_totales_cru == 10:
                                black_natural_cru = True
                                puntos_totales_cru += puntos_crupier

                            else:
                                # Suma de cartas menores a 12 sumamos el as como 11
                                if puntos_crupier == 11 and puntos_totales_cru < 12:
                                    puntos_totales_cru += 11
                                # suma de lsa cartas mayores a 12 el as vale 1
                                elif puntos_crupier == 11:
                                    puntos_totales_cru += 1

                                else:
                                    # otros
                                    puntos_totales_cru += puntos_crupier

                            print(' |', carta_crupier, palo_crupier + normal, end='|')
                            print(' Puntos Crupier: ', puntos_totales_cru)

                        if puntos_totales_cru >= 17:
                            break

                # Pozo máximo que obtuvo el jugador
                if entrada == 1:
                    mayor = pozo
                    racha_mayor_cru = racha_crupier

                elif pozo > mayor:
                    mayor = pozo

                print('*' * 80)
                print(verde, '\t\t\t\t\t\t\t\t RESULTADOS', normal)
                print('*' * 80)
                print(' Monto inicial del pozo: $ ', pozo)
                print(' Monto de la apuesta: $ ', apuesta)

                # Si en la partida salió BLACKJACK NATURAL
                if black_natural_jug is False and black_natural_cru is False:
                    nuevo_valor, ganador_jug, ganador_cru = verificar_ganador(puntos_totales_jug, apuesta,
                                                                              pozo_modificado, nombre,
                                                                              puntos_totales_cru)
                    if ganador_jug:
                        rondas_ganadas_jug += 1

                elif black_natural_jug and black_natural_cru is False:
                    print(verde, 'El ganador es', nombre, 'Alcanzo un blackjack natural', normal)
                    cantidad_black_natural += 1
                    nuevo_valor = apuesta * 2 + pozo_modificado
                    rondas_ganadas_jug += 1
                else:
                    if black_natural_jug and black_natural_cru:
                        print(verde, 'Ambos consiguieron un Blackjack natural. EMPATE', normal)
                        cantidad_black_natural += 1
                        nuevo_valor = pozo
                        ganador_cru = True
                    else:
                        print(verde, 'El ganador es el Crupier, alcanzo un blackjack natural', normal)
                        cantidad_black_natural += 1
                        nuevo_valor = pozo_modificado
                        ganador_cru = True
                print(' Monto actual del pozo: $ ', nuevo_valor)
                print('*' * 80)
                # Rondas jugadas
                rondas_totales += 1
                # Reiniciamos contadores
                puntos_totales_jug, op_jug, op_cru, puntos_totales_cru, can_sumar, cant_cartas_cru = 0, 0, 0, 0, 0, 0
                black_natural_jug, black_natural_cru = False, False

                # Racha crupier
                if ganador_cru:
                    racha_crupier += 1
                    ganador_cru = False

                # Mayor perdida de dinero del jugador
                if racha_crupier == 1:
                    perdida_mayor = apuesta
                elif apuesta > perdida_mayor:
                    perdida_mayor = apuesta

                # Incrementamos la ganancia de la apuesta
                pozo = nuevo_valor
                victorias_por = porcentaje_victorias(rondas_ganadas_jug, rondas_totales)
                racha_mayor_cru = monto_may(racha_mayor_cru, racha_crupier)
                monto_promedio = total_apuestas // rondas_totales

            else:
                if apuesta < 0:
                    print(rojo, 'la apuesta ingresada es menor a cero', normal)

                else:
                    print('*' * 80)
                    print(
                        rojo,
                        'El monto de la apuesta es mayor al saldo actual del pozo \n\t\t\t\t deposite mas dinero.',
                        normal)
                    print('*' * 80)

        elif opcion == 3:
            print(rojo, '*' * 80, normal)
            print(' Porcentaje de victorias del jugador: ', verde, victorias_por, '%.', normal)
            print(' Racha más larga de victorias del croupier: ', verde, racha_mayor_cru, 'victorias.', normal)
            print(' Cantidad de manos donde hubo un blackjack natural: ', verde, cantidad_black_natural, 'manos.',
                  normal)
            print(' Monto máximo que llegó a tener el jugador en el pozo: $', verde, mayor, normal)
            print(' Monto promedio del que dispuso el jugador para realizar apuestas: $', verde, monto_promedio, normal)
            print(' Pérdida más grande que sufrió el jugador es de: $', verde, perdida_mayor, normal)
            print(rojo, '*' * 80, normal)

        else:
            print('*' * 80)
            print(rojo, 'La opción ingresada es incorrecta', normal)
            print('*' * 80)


# Script principal
principal()
