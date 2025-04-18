## 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
## media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
## poder procesar 100 números cambiando solo un valor).

#se importa la libreria satistics
import statistics

#titulo del programa
print("Ingrese 100 numeros enteros:")

#se crea la lista vacia
lista_numeros=[]

#variable for de 0 a 100 numeros
for i in range(100):
    numeros=int(input("")) #se pide al usuario ingresar 100 numeros
    lista_numeros.append(numeros) #se agregan los numeros ingresados a la lista vacia "lista_numeros" con el .append

media = statistics.mean(lista_numeros) #se calcula la media

print(f"La media de los 100 numeros ingresados por el usuario es {media}") #se imprime la media
    



 
