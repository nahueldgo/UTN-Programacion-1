## 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
## Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    return promedio

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

resultado=calcular_promedio(num1,num2,num3)
print("El promedio de los tres numeros ingresados es ", round(resultado, 2))