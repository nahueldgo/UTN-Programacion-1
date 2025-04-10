##5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
## (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
## pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
## pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
## de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
## como una lista o un string.

contraseña = str(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

while len(contraseña)<8 or len(contraseña)>14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    contraseña = str(input("Vuelva a intentar: "))

print("Ha ingresado una contraseña correcta")