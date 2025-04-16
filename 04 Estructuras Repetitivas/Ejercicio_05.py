## 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
## programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero = random.randint(0,9)
intentos = 1
eleccion = int(input("Adivine el numero: "))

while eleccion != numero:
    eleccion = int(input("Incorrecto! Vuelva a intentar: "))
    intentos+=1

print(f"Correcto! El numero secreto era {numero}")
print(f"El número de intentos fue {intentos}")
