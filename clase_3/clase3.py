# Actividad: Colecciones 1
# Consigna:

# Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:

# gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista

# Transforma el texto en:

# Gordon lanzó su curva...

# Strawberry ha fallado por un pie! -gritó Joe Castiglione.

# Dos pies le corrigió Troop.

# Strawberry menea la cabeza como disgustado… -agrega el comentarista.

# Lo único prohibido es modificar directamente el texto

# Duración: 20 minutos

#--------------------------------------------
# Solución
#--------------------------------------------
#Declarar la variable con el mensaje original
mensaje= "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

#Separar el mensaje en partes usando el caracter "&"
partes = mensaje.split("&")
print(partes)  # mostrar la lista de partes

#Recorrer cada parte para formatearla correctamente
for i in range(len(partes)):
    if i == 0:
        partes[i] = '- '+partes[i].capitalize()+'..' # Primera letra en mayuscula y agregar "..."
    elif i == 1:
        partes[i] = partes[i][0].upper()+ partes[i][1:]  # Primera letra en mayuscula , no funciona capitalize porque la frase tiene mayusculas en medio
    elif i == 2:
        partes[i] = partes[i][0].upper()+ partes[i][1:] # Primera letra en mayuscula
    elif i == 3:
        partes[i] = partes[i].upper()[0]+ partes[i][1:]  # Primera letra en mayuscula
# Unir las partes formateadas en un solo mensaje con saltos de línea
mensaje_formateado = '.\n- '.join(partes)
print(mensaje_formateado)