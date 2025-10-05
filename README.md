
### 2. Fondo negro y letras blancas  
El bloque de código ya aparece con fondo oscuro en GitHub. Si quieres que más partes del README tengan fondo negro y letras blancas, puedes usar HTML:

```markdown
<div style="background-color:#1a1a1a; color:white; padding:20px;">
  <h2>Sección personalizada</h2>
  <p>Este texto aparece con fondo negro y letras blancas.</p>
  <a href="https://www.python.org" style="color: #3498db;">Enlace azul a Python.org</a>
</div>
# Juego-Piedra-Papel-Tijera
Desarrollo del Juego Piedra Papel y Tijera en Python 


Para comenzar el desarrollo de este juego tradicional debemos abarcar la logica del programa por medio de distintos diagramas tales como son el Diagrama Funcional.

Diagrama Funcional:

[Descargar o ver el diagrama funcional en RAPTOR: Piedra.rap](Diagrama%20funciona%20Piedra.rap)  
Este diagrama muestra el flujo lógico básico del juego Piedra, Papel o Tijera, ayudando a entender cómo se toman las decisiones entre las opciones y determina el ganador de cada partida.

Una vez ya se puede evidenciar el proceso lógico que sigue el programa podemos avanzar el código en Python siguiendo la misma estructura del diagrama
## Agrega tu código Python aquí

```python
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
    
