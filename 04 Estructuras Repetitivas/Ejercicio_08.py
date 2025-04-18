##8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
## programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
## negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
## menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("Ingrese 100 numeros enteros:")
positivos=0
negativos=0
pares=0
impares=0

for i in range(100):
    numeros = int(input(""))
    if numeros>0:
        positivos+=1
    elif numeros<0:
        negativos+=1
    
    if numeros % 2 == 0:
        pares+=1
    elif numeros % 2 != 0:
        impares+=1
     
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")

