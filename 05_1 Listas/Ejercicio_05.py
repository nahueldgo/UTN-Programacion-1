## 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
 
## Este codigo crea una lista de numeros, luego encuentra el valor mas alto de la lista con la funcion max(), (en este caso "22") 
## y lo elimina usando remove(). Finalmente, se verifica con print() que la nueva lista ya no contenga el elemento eliminado.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

## [8, 15, 3, 7]