## 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
## dependiendo de la opción que desee:
## 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
## 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
## 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
## El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
## usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
## lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingrese su nombre: "))

print("Presione 1 si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("Presione 2 si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("Presione 3 si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

numeros = int(input("Ingrese una opcion: "))

if numeros == 1:
    print(f"{nombre.upper()}")
elif numeros == 2:
    print(f"{nombre.lower()}")
elif numeros == 3:
    print(f"{nombre.title()}")
else:
    print("Opcion no valida")