##10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
## Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero: ")
invertido = numero[::-1]
print(f"Número invertido: {invertido}")