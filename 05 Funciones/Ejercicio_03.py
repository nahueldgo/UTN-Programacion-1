## 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
## que reciba cuatro parámetros e imprima: 
## “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre=str(input("Ingrese su nombre: "))
apellido=str(input("Ingrese su apellido: "))
edad=int(input("Ingrese su edad: "))
residencia=str(input("Ingrese su lugar de residencia: "))

informacion_personal(nombre, apellido, edad, residencia)