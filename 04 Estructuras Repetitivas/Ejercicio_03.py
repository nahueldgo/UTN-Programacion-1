##3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
## dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0

for i in range(num1+1, num2):
    suma=i+suma

print(suma)
