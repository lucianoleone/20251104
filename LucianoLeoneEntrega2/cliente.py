# Crear una clase Cliente:
#     - Minimo 4 atributosde los cuales 2 tienen que ser de instancia
#     - Metodo "__str__"
#     - Metodo "__init__"
#     - 2 metodos a eleccion
# - Esta clase va a estar en un modulo dentro de un paquete
# - Crear un archivo que haga uso de la clase Cliente

# - Crear el paquete redistribuible que se usa para el modelo de la clase.
# - Guardar este archivo y el .tar.gz creado en un archivo comprimido que tenga como nombre "LucianoLeoneEntrega2.zip"

class Cliente:
    cantidad_clientes = 0  # Atributo de clase
    def __init__(self, nombre:str, apellido:str, email:str, telefono:str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        Cliente.cantidad_clientes += 1


    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} \nEmail: {self.email} \nTeléfono: {self.telefono}"

    def actualizar_email(self, nuevo_email:str):
        self.email = nuevo_email

    def actualizar_telefono(self, nuevo_telefono:str):
        self.telefono = nuevo_telefono