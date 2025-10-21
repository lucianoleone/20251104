import sys
# print ("Hola Mundo")
# print (sys.argv)


# argumentos = sys.argv
# if "ejecutar" in argumentos:
#     print ("Ejecutando el script")
# else:
#     print ("No se ha pasado el argumento 'ejecutar'")

argumentos = sys.argv

if len(argumentos) == 3:
    texto = argumentos[1]
    repeticiones = argumentos[2]
    if not repeticiones.isnumeric():
        print ("El segundo argumento debe ser un número")
    else:
        for _ in range(int(repeticiones)):
            print (texto)
else:
    print ("Debe proporcionar exactamente dos argumentos: un texto y un número de repeticiones")

    