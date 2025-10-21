# ¡Instrucciones e iteración!
# Realiza los ejercicios 1, 2, 3, 4, 5 y 6.

# Formato: Puedes completar estas consignas en un Google Docs o un link a tu Colabs.

# 1. Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

#   - Mostrar una suma de los dos números

#  - Mostrar una resta de los dos números (el primero menos el segundo)

#  - Mostrar una multiplicación de los dos números

#  - Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará

#  - En caso de no introducir una opción válida, el programa informará de que no es correcta.
#---------------------------------------------------------------------------------------------------------------

# 2. Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

# 3. Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100: 🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

# 4. Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

# 5. Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo: 🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

# 6. Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
#   - Todos los números del 0 al 10 [0, 1, 2, ..., 10]

#   - Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

#   - Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

#   - Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

#   - Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# 🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

#------------------------SOLUCIONES-------------------------------------------------------------------------------------------------

# 1.

# numero_1 = int(input("Ingrese el primer número: "))
# numero_2 = int(input("Ingrese el segundo número: "))
# print("Menú de opciones:")
# print("1. Sumar los dos números")
# print("2. Restar los dos números")
# print("3. Multiplicar los dos números")
# print("4. Salir")
# opcion = input("Elija una opción (1-4): ")
# if opcion == '1':
#     resultado = numero_1 + numero_2
#     print(f"La suma de {numero_1} y {numero_2} es: {resultado}")
# elif opcion == '2':
#     resultado = numero_1 - numero_2
#     print(f"La resta de {numero_1} menos {numero_2} es: {resultado}")
# elif opcion == '3':
#     resultado = numero_1 * numero_2
#     print(f"La multiplicación de {numero_1} y {numero_2} es: {resultado}")
# elif opcion == '4':
#     print("Saliendo del programa.")
# else:
#     print("Opción no válida.")

#---------------------------------------------------------------------------------------------------------------
# 2.
# while True:
#     numero_impar = int(input("Ingrese un número impar: "))
#     if numero_impar % 2 != 0:
#         print(f"Gracias por ingresar el número impar: {numero_impar}")
#         break
#     else:
#         print("El número ingresado no es impar. Intente nuevamente.")

#---------------------------------------------------------------------------------------------------------------
# 3.
# suma_impares = sum(range(1, 100, 2))
# print(f"La suma de todos los números enteros impares desde 0 hasta 100 es: {suma_impares}")

#---------------------------------------------------------------------------------------------------------------
# 4.
# cantidad_numeros = int(input("¿Cuántos números desea introducir? "))
# suma_numeros = 0
# for i in range(cantidad_numeros):
#     numero = float(input(f"Ingrese el numero {i+1} de {cantidad_numeros}: "))  # Solicita el ingreso de un número: "))
#     suma_numeros += numero
# media = suma_numeros / cantidad_numeros
# print(f"La media aritmética de los números introducidos es: {media}")
#---------------------------------------------------------------------------------------------------------------
# 5.
# numeros_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# valor_in_lista = True
# while valor_in_lista:
#     numero_usuario = float(input("Ingrese un número entero del 0 al 9: "))
#     if numero_usuario < 0 or numero_usuario > 9:
#         print("Número fuera de rango. Intente nuevamente.")
#     elif numero_usuario in numeros_lista:
#         print(f"El número {int(numero_usuario)} se encuentra en la lista.")
#         valor_in_lista = False
#     else:
#         print(f"El número no se encuentra en la lista. Intente nuevamente.")
#---------------------------------------------------------------------------------------------------------------
# 6.
# lista_0_10 = list(range(11))
# print("Números del 0 al 10: ")
# for num in lista_0_10: 
#     if num < len(lista_0_10)-1:
#         print(f"{num}", end=", ")
#     else:
#         print(f"{num}", end="\n") 

# lista_menos_10_0 = list(range(-10, 1))
# print("Números del -10 al 0:")
# for i, num in enumerate(lista_menos_10_0): 
#     if i < len(lista_menos_10_0)-1:
#         print(f"{num}", end=", ")
#     else:
#         print(f"{num}", end="\n")

# lista_pares_0_20 = list(range(0, 21, 2))    
# print("Números pares del 0 al 20:")
# for indice, num in enumerate(lista_pares_0_20): 
#     if indice < len(lista_pares_0_20)-1:
#         print(f"{num}", end=", ")
#     else:
#         print(f"{num}", end="\n")

# lista_impares_menos_20_0 = list(range(-19, 1, 2))
# print("Números impares entre -20 y 0:")
# for i, num in enumerate(lista_impares_menos_20_0):
#     if i < len(lista_impares_menos_20_0)-1:
#         print(f"{num}", end=", ")
#     else:
#         print(f"{num}", end="\n")

# lista_multiplos_5_0_50 = list(range(0, 51, 5))
# print("Números múltiples de 5 del 0 al 50:")
# for i, num in enumerate(lista_multiplos_5_0_50):
#     if i < len(lista_multiplos_5_0_50)-1:
#         print(f"{num}", end=", ")
#     else:
#         print(f"{num}", end="\n")


