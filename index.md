---
title: Juego Piedra Papel Tijera
---

# Juego-Piedra-Papel-Tijera
Desarrollo del Juego Piedra Papel y Tijera en Python 

---

## Diagrama Funcional

[Descargar o ver el diagrama funcional en RAPTOR: Piedra.rap](Diagrama%20funciona%20Piedra.rap)  

Este diagrama muestra el flujo lógico básico del juego Piedra, Papel o Tijera, ayudando a entender cómo se toman las decisiones entre las opciones y determina el ganador de cada partida.

---

## Código Python del Juego Tradicional

```python
import random

# BUCLE DE INICIO DE JUEGO
while True:

    print("Bienvenido al juego Piedra, Papel o Tijera")

    # LISTA DE JUEGO
    opciones = ["Piedra", "Papel", "Tijera"]

    jugador = input("Elige Piedra, Papel o Tijera: ").title()
    computadora = random.choice(opciones)

    print("jugador:", jugador)
    print("computadora:", computadora)

    # CONDICIONES DE JUEGO
    if jugador == computadora:
        print("Empate!")
    elif (jugador == "Piedra" and computadora == "Tijera") or \
         (jugador == "Papel" and computadora == "Piedra") or \
         (jugador == "Tijera" and computadora == "Papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

    # REINICIAR JUEGO
    if input("¿Jugamos otra vez? (si/no): ").lower() == "si":
        print("Vamos de nuevo")
        continue
    else:
        print("Gracias por jugar")
        break
