## 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
## El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma=0
num=int(input("Ingrese un numero entero: "))
if num!=0:
	suma=num+suma
	
while num!=0:
	num=int(input("Siga ingresando un numero, el programa se detendra cuando ingrese 0: "))
	suma=num+suma

print(f"La suma de los numeros ingresados es {suma}")
