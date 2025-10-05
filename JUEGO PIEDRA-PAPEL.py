import random
#BUCLE DE INICIO DE JUEGO
while True:

 print("Bienvenido al juego Piedra, Papel o Tijera")

#LISTA DE JUEGO
 opciones=["Piedra","Papel","Tijera"]

 jugador= input("Elige Piedra, Papel o Tijera: ").title()
 computadora=(random.choice(opciones))

 print("jugador:", jugador)
 print("computadora:", computadora)

#CONDICIONES DE JUEGO
 if jugador == computadora:
    print("Empate!")
 elif (jugador == "Piedra" and computadora == "Tijera") or (jugador == "Papel" and computadora == "Piedra") or (jugador == "Tijera" and computadora == "Papel"):
    print("¡Ganaste!")
 else:
    print("¡Perdiste!")

#REINICIAR JUEGO
 if input("Jugamos Otra vez? (si/no): ").title() == "Si:
    print("Vamos de nuevo")
    continue
 else:
    print("Gracias por jugar")
    break
    

    