## 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
## número como parámetro y imprima la tabla de multiplicar de ese
## número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

n = int(input("Ingrese un número para ver su tabla de multiplicar: "))

tabla_multiplicar(n)
