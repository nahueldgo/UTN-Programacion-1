##6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
## numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
## hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint (1, 100) for i in range (50)]
mi_lista = numeros_aleatorios

print(mode (mi_lista))
print(median(mi_lista))
print(mean(mi_lista))