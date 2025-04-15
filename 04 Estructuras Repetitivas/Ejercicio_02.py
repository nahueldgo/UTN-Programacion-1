numero = int(input("Ingrese un numero entero: "))

cantidad_digitos = 0

if numero == 0:
    print(1)
else:
    while numero > 0:
        numero=numero//10
        cantidad_digitos+=1
    print(f"{cantidad_digitos}")


