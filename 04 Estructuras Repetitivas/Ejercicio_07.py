## 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
## número entero positivo indicado por el usuario.

num=(int(input("Ingrese un numero entero: ")))
suma=0

for i in range(0, num):
    suma=suma+i

print(f"La suma de los numeros comprendidos entre 0 y {num} es {suma}")