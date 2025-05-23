## 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
## Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

print("Conversor de grados Celsius a Fahrenheit")

def celsius_a_fahrenheit(celsius):
    fahrenheit=celsius*(9/5)+32
    return fahrenheit

grados_celsius=float(input("Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit=celsius_a_fahrenheit(grados_celsius)

print(grados_celsius,"°C equivalen a",round(grados_fahrenheit, 1),"°F")