#En un diccionario debemos almacenar usuario y contraseña. El programa debe mostrar un menu con las opciones: 1. Registrar usuario 2. Iniciar sesión 3. Mostrar usuarios 4. Salir
#4. Salir. El programa debe ejecutarse hasta que se elija la opción 4. Salir.
#1. Registrar usuario. Solicitar usuario y contraseña, si el usuario ya existe, mostrar un mensaje de error, sino, almacenar el usuario y la contraseña en el diccionario.
#2. Iniciar sesión. Solicitar usuario y contraseña, si el usuario no existe, mostrar un mensaje de error, si la contraseña no coincide, mostrar un mensaje de error, si todo es correcto, mostrar un mensaje de bienvenida.
#3. Mostrar usuarios. Mostrar todos los usuarios registrados (pero no las contraseñas).
#4. Salir. Salir del programa.

usuarios = {} # creamos un diccionario vacío para almacenar los usuarios y contraseñas

# Creamos una funcion para el menu, que retorna la opcion elegida
def print_menu():
    print("Menú de opciones:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios")
    print("4. Salir")
    opcion = input("Elija una opción (1-4): ")
    return opcion

# Creamos funcionar para cada una de las opciones del menu

# Opción 1: Registrar usuario
def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    # Verificamos si el usuario ya existe
    if usuario in usuarios:
        print("Error: El usuario ya existe.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios[usuario] = contrasena
        print(f"Usuario {usuario} registrado exitosamente.")

# Opción 2: Iniciar sesión
def iniciar_sesion():
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if usuario == '':  # Permite salir del bucle de inicio de sesión si se ingresa una cadena vacía
            break
        # Verificamos si el usuario existe
        elif usuario not in usuarios:
            print("Error: El usuario no existe.")
        else:
            # Si el usuario existe, solicitamos la contraseña
            contrasena = input("Ingrese su contraseña: ")
            if usuarios[usuario] != contrasena:
                print("Error: Contraseña incorrecta.")
            else:
                # Si la contraseña es correcta, mostramos un mensaje de bienvenida
                print(f"Bienvenido, {usuario}!")
                break

# Opción 3: Mostrar usuarios
def mostrar_usuarios():
    # Hacemos una verificación para ver si hay usuarios registrados
    if usuarios:
        # Si hay usuarios, los mostramos
        print("Usuarios registrados:")
        for usuario in usuarios.keys():
            print(usuario)
    else:
        print("No hay usuarios registrados.")
    
# Bucle principal del programa
while True:
    # Mostramos el menú y solicitamos una opción
    opcion = print_menu()
    
    # Ejecutamos la opción elegida
    if opcion == '1':
        registrar_usuario()
    
    elif opcion == '2':
        iniciar_sesion()
    
    elif opcion == '3':
        mostrar_usuarios()    
    
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    
    # Si la opció no es ninguna de las anteriores, mostramos un mensaje de error y volvemos a mostrar el menú
    else:
        print("Opción no válida. Intente nuevamente.")
