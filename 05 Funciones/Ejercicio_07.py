## 7. Crear una función llamada operaciones_basicas(a, b) que reciba
## dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
## Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return (suma, resta, multiplicacion, division)

tupla_vacia=()

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

resultados=operaciones_basicas(num1, num2)

resultados=tupla_vacia+(resultados)

suma, resta, multiplicacion, division = resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
