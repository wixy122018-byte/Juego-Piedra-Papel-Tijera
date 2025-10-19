import random

opciones = ("Piedra", "Papel", "Tijera")

# BUCLE DE INICIO DE JUEGO
while True:

    print("Bienvenido al juego Piedra, Papel o Tijera")
    print("El juego se decide al mejor de 3 rondas\n")  # Salto de línea agregado

    # LISTA DE JUEGO
    def Juego():
        jugador = input("Elige Piedra, Papel o Tijera: ").title()
        computadora = (random.choice(opciones))
        print()
        print("jugador:", jugador)
        print("computadora:", computadora)
        print()
        return jugador, computadora

    # CONDICIONES DE JUEGO
    def J1_C1(jugador, computadora):
        if jugador == computadora:
            print("¡Empate!\n")
            return 0
        elif (jugador == "Piedra" and computadora == "Tijera") or (jugador == "Papel" and computadora == "Piedra") or (jugador == "Tijera" and computadora == "Papel"):
            print("¡Ganaste!\n")
            return 1
        else:
            print("¡Perdiste!\n")
            return -1

    # MEJOR DE TRES
    def jugar_mejor_de_tres():
        puntaje_jugador = 0
        puntaje_computadora = 0

        while puntaje_jugador < 2 and puntaje_computadora < 2:
            jugador, computadora = Juego()
            resultado = J1_C1(jugador, computadora)

            if resultado == 1:
                puntaje_jugador += 1
            elif resultado == -1:
                puntaje_computadora += 1

            print(f"Puntaje: Jugador {puntaje_jugador}, Computadora {puntaje_computadora}")

        if puntaje_jugador > puntaje_computadora:
            print("¡El Jugador gana el mejor de 3!")
        else:
            print("¡La Computadora gana el mejor de 3!")

    # REINICIAR JUEGO
    def Reiniciar():
        if input("¿Jugamos Otra vez? (si/no): ").title() == "Si":
            print("Vamos de nuevo")
            return True  # Indicar que se reinicia
        else:
            print("Gracias por jugar")
            return False  # Indicar que no se reinicia

    # EJECUTAR JUEGO
    jugar_mejor_de_tres()

    # Preguntar si se juega otra vez
    if not Reiniciar():
        break