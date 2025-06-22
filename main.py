import random
from art import logo

def selecciona_carta(baraja):
    carta = random.choice(baraja)
    baraja.remove(carta)
    return carta, baraja

def calcula_puntuacion(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0  # Blackjack
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)  

def comprobar_blackjack(puntuacion_jugador, puntuacion_casa):
    if puntuacion_jugador == puntuacion_casa:
        return "Empate"
    elif puntuacion_casa == 0:
        return "Casa gana con Blackjack"
    elif puntuacion_jugador == 0:
        return "Jugador gana con Blackjack"
    elif puntuacion_jugador > 21:
        return "Jugador se pasa, Casa gana"
    elif puntuacion_casa > 21:
        return "Casa se pasa, Jugador gana"
    elif puntuacion_jugador > puntuacion_casa:
        return "Jugador gana"
    else:
        return "Casa gana"
    
def jugar_blackjack():
    baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    cartas_jugador = []
    cartas_casa = []

    for _ in range(2):
        carta_jugador, baraja = selecciona_carta(baraja)
        cartas_jugador.append(carta_jugador)
        carta_casa, baraja = selecciona_carta(baraja)
        cartas_casa.append(carta_casa)

    juego_terminado = False

    while not juego_terminado:
        puntuacion_jugador = calcula_puntuacion(cartas_jugador)
        puntuacion_casa = calcula_puntuacion(cartas_casa)

        print(f"Cartas del jugador: {cartas_jugador}, Puntuación: {puntuacion_jugador}")
        print(f"Primera carta de la casa: {cartas_casa[0]}")

        if puntuacion_jugador == 0 or puntuacion_casa == 0 or puntuacion_jugador > 21:
            juego_terminado = True
        else:
            otra_carta = input("¿Quieres otra carta? (s/n): ").lower()
            if otra_carta == 's':
                carta_jugador, baraja = selecciona_carta(baraja)
                cartas_jugador.append(carta_jugador)
            else:
                juego_terminado = True

    while puntuacion_casa < 17 and puntuacion_casa != 0:
        carta_casa, baraja = selecciona_carta(baraja)
        cartas_casa.append(carta_casa)
        puntuacion_casa = calcula_puntuacion(cartas_casa)

    resultado = comprobar_blackjack(puntuacion_jugador, puntuacion_casa)
    print(f"Cartas finales del jugador: {cartas_jugador}, Puntuación: {puntuacion_jugador}")
    print(f"Cartas finales de la casa: {cartas_casa}, Puntuación: {puntuacion_casa}")
    print(resultado)

while input("¿Quieres jugar una partida de Blackjack? (s/n): ").lower() == 's':
    print("\n" * 20)
    print("\n" + logo)
    jugar_blackjack()