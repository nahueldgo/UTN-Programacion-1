## 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
## y devuelva la cantidad de horas correspondientes. 
## Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas

tiempo=int(input("Ingrese los segundos a convertir: "))

horas=segundos_a_horas(tiempo)

print("De segundos a horas")
print(tiempo, "segundos son:", horas, "horas.")