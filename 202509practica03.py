lista = [29,-5,-12,17,5,12,23,16,12,5,-12,17]
print("Lista original:", lista)

#Quitar duplicados

no_duplicados = list(set(lista))
print("Lista sin duplicados:", no_duplicados)

#Ordenar la lista de mayor a menor

lista_ordenada =sorted(lista, reverse=True)
print("Lista ordenada:", lista_ordenada)

#Extraer los numeros pares de lista

lista_pares = []
for num in lista_ordenada:
    if num % 2 == 0:
        lista_pares.append(num)
print("Números pares:", lista_pares)

#Realizar una suma de todos los numeros que qeudan

suma = sum(lista)
print("Suma de todos los números:", suma)

#Colocar la suma al inicio de la lista

lista.insert(0, suma)

#Mostrar la lista con la suma añadida

print("Lista con la suma añadida:", lista)

#Comprobar que el indice 0 es igual a la suma de todos los numeros

if lista[0] == sum(lista[1:]):
    print("El índice 0 es igual a la suma de todos los números.")
else:
    print("El índice 0 no es igual a la suma de todos los números.")