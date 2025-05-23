## 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
## peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos 
## y llamar a la función para mostrar el resultado con dos decimales.

print("Calculadora de indice de masa corporal (IMC)")

def calcular_imc(peso, altura):
 imc=peso/altura**2
 return imc

peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print("Su indice de masa corporal es ", round(imc, 2))