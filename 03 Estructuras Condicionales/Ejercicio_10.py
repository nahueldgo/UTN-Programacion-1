##10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
## Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
## del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
## si el usuario se encuentra en otoño, invierno, primavera o verano

hemisferio = str(input("Ingrese el hemisferio donde se encuentra (N/S) : "))
dia = int(input("Ingrese el dia de la fecha: "))
mes = int(input("Ingrese el mes: "))

##Bloque del hemisferio norte:
if hemisferio.upper() == "N" and mes in [12, 1, 2, 3]:
    if mes == 12 and dia >= 21 and dia <=31:
        print("Usted se encuentra en Invierno")
    elif mes == 1 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Invierno")
    elif mes == 2 and dia >= 1 and dia <=29:
        print("Usted se encuentra en Invierno")
    elif mes == 3 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Invierno")
    else:
        print("Ingrese una fecha valida")

##Bloque del hemisferio norte:
if hemisferio.upper() == "N" and mes in [3, 4, 5, 6]:
    if mes == 3 and dia >= 21 and dia <=31:
        print("Usted se encuentra en Primavera")
    elif mes == 4 and dia >= 1 and dia <=30:
        print("Usted se encuentra en Primavera")
    elif mes == 5 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Primavera")
    elif mes == 6 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Primavera")
    else:
        print("Ingrese una fecha valida")

##Bloque del hemisferio norte:
if hemisferio.upper() == "N" and mes in [6, 7, 8, 9]:
    if mes == 6 and dia >= 21 and dia <=30:
        print("Usted se encuentra en Verano")
    elif mes == 7 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Verano")
    elif mes == 8 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Verano")
    elif mes == 9 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Verano")
    else:
        print("Ingrese una fecha valida")

##Bloque del hemisferio norte:
if hemisferio.upper() == "N" and mes in [9, 10, 11, 12]:
    if mes == 9 and dia >= 21 and dia <=30:
        print("Usted se encuentra en Otoño")
    elif mes == 10 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Otoño")
    elif mes == 11 and dia >= 1 and dia <=30:
        print("Usted se encuentra en Otoño")
    elif mes == 12 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Otoño")
    else:
        print("Ingrese una fecha valida")

##-----------------------------------------------------------
##-----------------------------------------------------------

##Bloque del hemisferio sur:
if hemisferio.upper() == "S" and mes in [12, 1, 2, 3]:
    if mes == 12 and dia >= 21 and dia <=31:
        print("Usted se encuentra en Verano")
    elif mes == 1 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Verano")
    elif mes == 2 and dia >= 1 and dia <=29:
        print("Usted se encuentra en Verano")
    elif mes == 3 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Verano")
    else:
        print("Ingrese una fecha valida")

##Bloque del hemisferio sur:
if hemisferio.upper() == "S" and mes in [3, 4, 5, 6]:
    if mes == 3 and dia >= 21 and dia <=31:
        print("Usted se encuentra en Otoño")
    elif mes == 4 and dia >= 1 and dia <=30:
        print("Usted se encuentra en Otoño")
    elif mes == 5 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Otoño")
    elif mes == 6 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Otoño")
    else:
        print("Ingrese una fecha valida")

##Bloque del hemisferio sur:
if hemisferio.upper() == "S" and mes in [6, 7, 8, 9]:
    if mes == 6 and dia >= 21 and dia <=30:
        print("Usted se encuentra en Invierno")
    elif mes == 7 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Invierno")
    elif mes == 8 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Invierno")
    elif mes == 9 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Invierno")
    else:
        print("Ingrese una fecha valida")

##Bloque del hemisferio sur:
if hemisferio.upper() == "S" and mes in [9, 10, 11, 12]:
    if mes == 9 and dia >= 21 and dia <=30:
        print("Usted se encuentra en Primavera")
    elif mes == 10 and dia >= 1 and dia <=31:
        print("Usted se encuentra en Primavera")
    elif mes == 11 and dia >= 1 and dia <=30:
        print("Usted se encuentra en Primavera")
    elif mes == 12 and dia >= 1 and dia <=20:
        print("Usted se encuentra en Primavera")
    else:
        print("Ingrese una fecha valida")