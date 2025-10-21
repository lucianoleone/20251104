# Actividad: Función año bisiesto
# Consigna

# Realizar una función llamada año_bisiesto:

# Recibirá un año por parámetro

# Imprimirá “El año año es bisiesto” si el año es bisiesto

# Imprimirá “El año año no es bisiesto” si el año no es bisiesto

# Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

# Información a tener en cuenta:

# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

# Actividad: ¡Funciones!
# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

# 🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1.

# Si el primer número es menor que el segundo, debe devolver -1.

# Si ambos números son iguales, debe devolver un 0.


# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

# Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:

# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

# Comprueba el punto intermedio entre -12 y 24

# Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
# Devolver el límite inferior si el número es menor que éste

# Devolver el límite superior si el número es mayor que éste.

# Devolver el número sin cambios si no se supera ningún límite.

# Comprueba el resultado de recortar 15 entre los límites 0 y 10

#---------------------------------------------------------------------------------------------------------------
#Ejercicio 1 - Año bisiesto
# def anio_bisiesto(año):
#     if not anio.isnumeric():
#         print("Por favor, ingrese un número válido.")
#         return
#     anio = int(anio)
#     if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
#         print(f"El año {anio} es bisiesto")
#     else:
#         print(f"El año {anio} no es bisiesto")

# while True:
#     anio_bisiesto(input("Ingrese un año: "))

#---------------------------------------------------------------------------------------------------------------
#Ejercicio 2 - Área de un rectángulo
def area_rectangulo(base, altura):
    base= int(base)
    altura= int(altura)
    return base * altura

base= input("Ingrese la base del rectángulo: ")
altura= input("Ingrese la altura del rectángulo: ")
print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")