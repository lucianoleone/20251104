partidos_ganados= int(input("Ingrese el número de partidos ganados: "))
partidos_perdidos = int(input("Ingrese el número de partidos perdidos: "))
partidos_empatados = int(input("Ingrese el número de partidos empatados: "))
if (partidos_ganados+partidos_perdidos+partidos_empatados) != 20  :
    print("Error: El total de partidos debe ser 20.")
    exit()

elif partidos_ganados < 0 or partidos_perdidos < 0 or partidos_empatados < 0:
    print("Error: El número de partidos no puede ser negativo.")
    exit()
else:

    puntos = partidos_ganados * 3 + partidos_empatados
print("El total de puntos es: ", puntos)

