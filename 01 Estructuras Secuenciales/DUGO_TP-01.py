#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math
radio = float(input("Ingrese el radio del circulo: "))
area = (math.pi*radio**2)
print(f"El area es {area}")
perimetro = (2*math.pi) * radio
print(f"El perimetro del circulo es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = float(input("Ingrese los segundos: "))
minutos = segundos/60
horas = minutos/60
print(str(f"{segundos} segundos equivale a {horas} horas"))

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
num = int(input("Ingrese un numero entero para multiplicar: "))
for i in range(1, 11):
    tabla = num*i
    print(f"{num} x {i} = {tabla}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))

while num1==0 or num2==0:
    print("El numero debe ser distinto de 0, intentalo nuevamente")
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese otro numero entero: "))

if num1!=0 and num2!=0:
   
    suma = num1+num2
    print(f"{num1} + {num2} = {suma}")

    resta = num1-num2
    print(f"{num1} - {num2} = {resta}")

    multiplicacion = num1*num2
    print(f"{num1} x {num2} = {multiplicacion}")

    division = num1/num2
    print(str(f"{num1} / {num2} = {division}"))

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura)**2

(print(f"Su indice de masa corporal es de {imc}"))

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
print("CONVERSOR DE GRADOS CELSIUS(°C) A FAHRENHEIT(°F)")

celcius = float(input("Ingrese la temperatura en grados Celsius: "))
fahr = (celcius * 9/5) + 32
print(f"{celcius}°C son {fahr}°F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("Ingrese 3 numeros para calcular el promedio")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = float(num1+num2+num3) / 3

print(f"El promedio de los tres numeros es {promedio}")