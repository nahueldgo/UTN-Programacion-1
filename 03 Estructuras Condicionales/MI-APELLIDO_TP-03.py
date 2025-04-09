##7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
## termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
## pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
## pantalla.


cadena_de_texto = str(input("Escriba una frase o una palabra: "))

if cadena_de_texto[-1] =="a" or cadena_de_texto[-1] =="e" or cadena_de_texto[-1] =="i" or cadena_de_texto[-1] =="o" or cadena_de_texto[-1] =="u":
    print ("La ultima letra es vocal")
else:
    print("La ultima letra no es vocal")


